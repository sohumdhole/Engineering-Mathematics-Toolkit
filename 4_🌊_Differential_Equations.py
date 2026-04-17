import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy.integrate import odeint

st.set_page_config(page_title="Differential Equations", page_icon="🌊", layout="wide")

st.title("🌊 Differential Equations: Modeling Dynamic Systems")

# --- 1. Concept Summary ---
st.header("1. Concept Summary")
st.markdown("""
An algebraic equation describes relationships between stationary values (e.g., $2x = 10$). A **Differential Equation** describes relationships between a function and its *rates of change* (its derivatives).

*   **Ordinary Differential Equations (ODEs):** Involve functions of only one single variable (like time $t$).
*   **General form:** An equation like $\\frac{dy}{dt} = f(y, t)$. It states how fast $y$ is changing at any given state $y$ and time $t$.
*   **Solving an ODE:** Instead of finding a number, the solution to an ODE is a *function* $y(t)$ that satisfies the relationship.
""")

# --- 2. Interactive Visualisation ---
st.header("2. Interactive Visualisation: Exponential Growth and Decay")
st.markdown("""
The simplest differential equation is the **First-Order Linear ODE**, often used for population growth or radioactive decay:
$$ \\frac{dy}{dt} = k \\cdot y $$
This says: "The rate of change of $y$ is proportional to the current amount of $y$".
""")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("System Parameters")
    # Default k=0.5, y0=1
    k = st.slider("Growth/Decay Rate (k)", min_value=-2.0, max_value=2.0, value=0.5, step=0.1)
    y0 = st.slider("Initial Value (y_0)", min_value=-5.0, max_value=10.0, value=1.0, step=0.5)
    t_max = st.slider("Time range to simulate (t)", min_value=1, max_value=20, value=10)
    
    st.latex(f"\\frac{{dy}}{{dt}} = {k}y")
    st.latex(f"y(0) = {y0}")
    
    # Analytical solution text
    if k > 0:
        st.info("System behavior: **Exponential Growth**")
    elif k < 0:
        st.info("System behavior: **Exponential Decay**")
    else:
        st.info("System behavior: **Static Equilibrium**")

with col2:
    # Time array
    t = np.linspace(0, t_max, 200)
    
    # Numerical Solution using scipy.integrate.odeint
    def model(y, t, k):
        return k * y
    
    y_vals = odeint(model, y0, t, args=(k,))
    
    # Analytical solution for validation: y(t) = y0 * e^(kt)
    y_analytical = y0 * np.exp(k * t)
    
    fig = go.Figure()
    
    # Plot numerical result
    fig.add_trace(go.Scatter(x=t, y=y_vals.flatten(), mode='lines', name='y(t) (Numerical)', line=dict(color='blue', width=4)))
    
    # Plot analytical result as dots to show agreement
    fig.add_trace(go.Scatter(x=t[::10], y=y_analytical[::10], mode='markers', name='Analytical Check', marker=dict(color='orange', size=8)))
    
    fig.update_layout(
         title="System Response Over Time",
         xaxis_title="Time (t)",
         yaxis_title="Amount (y)",
         height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

# --- 3. Worked Example ---
st.header("3. Worked Example")
st.markdown("""
**Problem:** Solve the differential equation $\\frac{dy}{dt} = -0.1y$ with the initial condition $y(0) = 100$.

**Step-by-Step Solution (Separation of Variables):**
1.  **Separate the variables:** Move all $y$ terms to one side, and $t$ terms to the other.
    $$ \\frac{1}{y} dy = -0.1 dt $$
2.  **Integrate both sides:**
    $$ \\int \\frac{1}{y} dy = \\int -0.1 dt $$
    $$ \\ln|y| = -0.1t + C $$
3.  **Solve for y:** Exponentiate both sides to get rid of the natural log.
    $$ y(t) = e^{-0.1t + C} = e^C e^{-0.1t} $$
    Since $e^C$ is just an arbitrary constant, we can call it $C_1$.
    $$ y(t) = C_1 e^{-0.1t} $$
4.  **Apply Initial Condition:** We know $y(0) = 100$. Plug in $t=0$.
    $$ 100 = C_1 e^{-0.1(0)} = C_1(1) \\implies C_1 = 100 $$
5.  **Final Analytical Solution:**
    $$ y(t) = 100 e^{-0.1t} $$
""")

# --- 4. Common Mistakes ---
st.header("4. Common Mistakes")
st.markdown("""
*   **Forgetting or Ignoring Initial Conditions.** A differential equation gives you a *family* of curves (a general solution). The initial condition is required to pick the specific curve (the particular solution) that models your actual physical system.
*   **Assuming linear responses.** Just because an equation looks simple, students often assume variables scale linearly. In systems with feedback (where the rate depends on the current state, like above), the behavior is often exponential, not linear.
*   **Units Mismatch.** When setting up physical systems (like fluid mixing or heat transfer), making sure all terms in the equation have identical units (e.g. $kg/s$) is a crucial sanity check that is often neglected.
""")

# --- 5. Real-World Application ---
st.header("5. Real-World Application")
st.markdown("""
**Engineering Application: Thermodynamics and Control Systems**

*   **Newton's Law of Cooling:** The rate at which an object cools is proportional to the difference between its temperature and the ambient environment: $\\frac{dT}{dt} = -k(T - T_{ambient})$. This is vital for HVAC engineering or electronics thermal management.
*   **RC Circuits:** In an electrical circuit with a resistor ($R$) and capacitor ($C$), the voltage discharging across the capacitor follows a differential equation $\\frac{dV}{dt} + \\frac{1}{RC}V = 0$, resulting in exponential decay.
*   **Control Theory:** Engineers use coupled differential equations to mathematically model robots or aircraft arrays. PID controllers then calculate corrective forces to push the system state toward a desired target value.
""")
