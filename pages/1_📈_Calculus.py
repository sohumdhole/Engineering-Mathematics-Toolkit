import streamlit as st
import numpy as np
import sympy as sp
import plotly.graph_objects as go
from sympy.utilities.lambdify import lambdify

st.set_page_config(page_title="Calculus", page_icon="📈", layout="wide")

st.title("📈 Calculus: Rates of Change & Accumulation")

# --- 1. Concept Summary ---
st.header("1. Concept Summary")
st.markdown("""
Calculus is the mathematical study of continuous change. It has two major branches:
*   **Differential Calculus:** Focuses on the *Derivative*, which measures the instantaneous rate of change of a quantity (how fast something is changing at a specific moment). Geometrically, it represents the slope of the tangent line to a curve.
*   **Integral Calculus:** Focuses on the *Integral*, which measures the accumulation of quantities (how much of something has piled up over time/space). Geometrically, it represents the area under a curve.

The **Fundamental Theorem of Calculus** connects these two, showing that differentiation and integration are inverse operations.
""")

# --- 2. Interactive Visualisation ---
st.header("2. Interactive Visualisation")
st.markdown("Enter a mathematical function of $x$ to visualize its derivative and integral.")

user_func_str = st.text_input("Enter function f(x):", value="sin(x)")
x_val = st.slider("Select an x-value to evaluate the derivative:", min_value=-10.0, max_value=10.0, value=2.0)

try:
    # Setup SymPy
    x = sp.Symbol('x')
    f_sym = sp.sympify(user_func_str)
    
    # Compute symbolic derivative and integral
    f_prime_sym = sp.diff(f_sym, x)
    f_int_sym = sp.integrate(f_sym, x)
    
    # Lambdify for numerical evaluation
    f_num = lambdify(x, f_sym, modules=['numpy'])
    f_prime_num = lambdify(x, f_prime_sym, modules=['numpy'])
    
    st.latex(f"f(x) = {sp.latex(f_sym)}")
    st.latex(f"f'(x) = \\frac{{d}}{{dx}}[{sp.latex(f_sym)}] = {sp.latex(f_prime_sym)}")
    st.latex(f"\\int f(x) dx = {sp.latex(f_int_sym)} + C")
    
    # Generate data for plotting
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_num(x_vals)
    y_prime_vals = f_prime_num(x_vals)
    
    # Handle constants (if lambdify returns a scalar instead of array)
    if not isinstance(y_vals, np.ndarray):
        y_vals = np.full_like(x_vals, y_vals)
    if not isinstance(y_prime_vals, np.ndarray):
        y_prime_vals = np.full_like(x_vals, y_prime_vals)

    # Calculate tangent line at x_val
    y_val_at_x = f_num(x_val)
    slope_at_x = f_prime_num(x_val)
    tangent_line = slope_at_x * (x_vals - x_val) + y_val_at_x
    
    # Create tabs for Derivative and Integral views
    tab1, tab2 = st.tabs(["Derivative Visualizer", "Integration Visualizer"])
    
    with tab1:
        fig_deriv = go.Figure()
        fig_deriv.add_trace(go.Scatter(x=x_vals, y=y_vals, name="f(x)", line=dict(color='blue')))
        fig_deriv.add_trace(go.Scatter(x=x_vals, y=y_prime_vals, name="f'(x)", line=dict(color='red', dash='dash')))
        fig_deriv.add_trace(go.Scatter(x=x_vals, y=tangent_line, name=f"Tangent at x={x_val}", line=dict(color='green', dash='dot')))
        fig_deriv.add_trace(go.Scatter(x=[x_val], y=[y_val_at_x], mode='markers', name=f"Point ({x_val}, {y_val_at_x:.2f})", marker=dict(color='green', size=10)))
        
        # Determine dynamic y-range based on the main function around the region to avoid huge asymptotes blowing up the chart
        y_min = np.percentile(y_vals[~np.isnan(y_vals)], 5) - 2
        y_max = np.percentile(y_vals[~np.isnan(y_vals)], 95) + 2
        
        fig_deriv.update_layout(title="Function and its Derivative", xaxis_title="x", yaxis_title="y", yaxis_range=[y_min, y_max], height=500)
        st.plotly_chart(fig_deriv, use_container_width=True)

    with tab2:
        fig_int = go.Figure()
        fig_int.add_trace(go.Scatter(x=x_vals, y=y_vals, name="f(x)", line=dict(color='blue')))
        
        # Shade area under curve from -10 to x_val
        x_shade = np.linspace(-10, x_val, 200)
        y_shade = f_num(x_shade)
        if not isinstance(y_shade, np.ndarray):
            y_shade = np.full_like(x_shade, y_shade)
            
        fig_int.add_trace(go.Scatter(x=np.concatenate([x_shade, x_shade[::-1]]), 
                                     y=np.concatenate([y_shade, np.zeros_like(y_shade)]), 
                                     fill='toself', fillcolor='rgba(0, 0, 255, 0.2)', 
                                     line=dict(color='rgba(255,255,255,0)'),
                                     name=f"Area up to x={x_val}"))
                                     
        fig_int.update_layout(title="Area Under the Curve (Definite Integral)", xaxis_title="x", yaxis_title="y", yaxis_range=[y_min, y_max], height=500)
        st.plotly_chart(fig_int, use_container_width=True)

except Exception as e:
    st.error(f"Could not parse or evaluate the function. Error: {e}")
    st.info("Please try using standard Python math syntax, e.g., 'x**2', 'sin(x)', 'exp(-x)'.")

# --- 3. Worked Example ---
st.header("3. Worked Example")
st.markdown("""
**Problem:** Find the maximum height of a projectile whose upward velocity is given by $v(t) = 20 - 9.8t$ (in m/s), assuming starting height $h(0) = 0$.

**Step-by-Step Solution:**
1.  **Understand the relationship:** The height $h(t)$ is the integral (accumulation) of velocity over time. $h(t) = \\int v(t) dt$.
2.  **Integrate:** 
    $$h(t) = \\int (20 - 9.8t) dt = 20t - \\frac{9.8t^2}{2} + C = 20t - 4.9t^2 + C$$
3.  **Apply Initial Conditions:** Since $h(0) = 0$, then $20(0) - 4.9(0)^2 + C = 0$, so $C = 0$.
    $$h(t) = 20t - 4.9t^2$$
4.  **Find Maximum Height:** Max height occurs when the velocity is zero (it stops going up and starts falling).
    $$v(t) = 20 - 9.8t = 0 \\implies t = \\frac{20}{9.8} \\approx 2.04 \\text{ seconds}$$
5.  **Evaluate:** Plug $t = 2.04$ into $h(t)$:
    $$h(2.04) = 20(2.04) - 4.9(2.04)^2 \\approx 40.8 - 20.4 = 20.4 \\text{ meters}$$
""")

# --- 4. Common Mistakes ---
st.header("4. Common Mistakes")
st.markdown("""
*   **Forgetting the constant of integration ($+C$).** When taking an indefinite integral, always add $+C$. An integral represents a family of curves, shifted vertically.
*   **Applying the Power Rule incorrectly to fractions or negatives.** Remember that $\\int \\frac{1}{x} dx = \\ln|x|$, not using the power rule to get $x^0 / 0$.
*   **Chain Rule errors in differentiation.** When differentiating a nested function like $\\sin(2x)$, students often forget to multiply by the derivative of the inner function (yielding $\\cos(2x)$ instead of $2\\cos(2x)$).
""")

# --- 5. Real-World Application ---
st.header("5. Real-World Application")
st.markdown("""
**Engineering Application: Kinematics and Dynamics**

Calculus is the foundation of classical mechanics.
*   **Automotive Engineering:** The acceleration of a car is the derivative of its velocity. To find out how far a car has traveled over a given time interval while braking, engineers integrate the velocity curve.
*   **Structural Engineering:** The deflection (bending) of a beam under a load is calculated through multiple integrations of the load distribution function. 
*   **Electrical Engineering:** The voltage across an inductor is proportional to the *derivative* of the current passing through it ($V = L \\frac{di}{dt}$), while the voltage across a capacitor is proportional to the *integral* of the current ($V = \\frac{1}{C} \\int i dt$).
""")
