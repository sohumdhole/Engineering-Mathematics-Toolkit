import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Trigonometry", page_icon="📐", layout="wide")

st.title("📐 Trigonometry: The Unit Circle & Identities")

# --- 1. Concept Summary ---
st.header("1. Concept Summary")
st.markdown("""
Trigonometry originally emerged from the study of triangles, establishing relationships between their angles and side lengths. In modern engineering, it is defined more broadly using the **Unit Circle**.

*   **Unit Circle:** A circle with a radius of $1$ centered at the origin $(0,0)$.
*   For any point $(x, y)$ on the unit circle formed by an angle $\\theta$ from the positive x-axis:
    *   **$\\cos(\\theta) = x$** (the horizontal position)
    *   **$\\sin(\\theta) = y$** (the vertical position)
    *   **$\\tan(\\theta) = \\frac{\\sin(\\theta)}{\\cos(\\theta)} = \\frac{y}{x}$** (the slope of the line)
*   **Radians vs Degrees:** Radians measure angle by the arc length on the unit circle. $360^\\circ = 2\\pi \\text{ radians}$.
""")

# --- 2. Interactive Visualisation ---
st.header("2. Interactive Visualisation")
st.markdown("Explore the unit circle. Adjust the angle to see how the sine (y-coordinate) and cosine (x-coordinate) change.")

# Interactive controls
angle_deg = st.slider("Select Angle (Degrees)", min_value=0, max_value=360, value=45)
angle_rad = np.radians(angle_deg)

col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader("Values")
    sin_val = np.sin(angle_rad)
    cos_val = np.cos(angle_rad)
    
    # Handle tangent asymptotes
    if angle_deg in [90, 270]:
        tan_val_str = "Undefined (\\infty)"
    else:
        tan_val = np.tan(angle_rad)
        tan_val_str = f"{tan_val:.3f}"
        
    st.latex(f"\\theta = {angle_deg}^\\circ = \\frac{{{angle_deg}}}{{180}}\\pi \\text{{ rad}}")
    st.latex(f"\\sin({angle_deg}^\\circ) = {sin_val:.3f}")
    st.latex(f"\\cos({angle_deg}^\\circ) = {cos_val:.3f}")
    st.latex(f"\\tan({angle_deg}^\\circ) = {tan_val_str}")

with col2:
    # Plotting Unit Circle
    theta = np.linspace(0, 2 * np.pi, 200)
    x_circle = np.cos(theta)
    y_circle = np.sin(theta)
    
    fig = go.Figure()
    
    # Draw circle
    fig.add_trace(go.Scatter(x=x_circle, y=y_circle, mode='lines', line=dict(color='gray', dash='dot'), name="Unit Circle"))
    
    # Draw point on circle
    point_x = np.cos(angle_rad)
    point_y = np.sin(angle_rad)
    fig.add_trace(go.Scatter(x=[point_x], y=[point_y], mode='markers', marker=dict(color='black', size=10), name=f"({cos_val:.2f}, {sin_val:.2f})"))
    
    # Draw angle line
    fig.add_trace(go.Scatter(x=[0, point_x], y=[0, point_y], mode='lines', line=dict(color='black', width=3), name="Hypotenuse (r=1)"))
    
    # Draw projections (sine and cosine components)
    # Cosine (x-axis component)
    fig.add_trace(go.Scatter(x=[0, point_x], y=[0, 0], mode='lines', line=dict(color='blue', width=4), name=f"cos({angle_deg}°) (x)"))
    
    # Sine (y-axis component)
    fig.add_trace(go.Scatter(x=[point_x, point_x], y=[0, point_y], mode='lines', line=dict(color='red', width=4), name=f"sin({angle_deg}°) (y)"))
    
    # Layout configuration
    fig.update_layout(
        title="Unit Circle Visualizer",
        xaxis=dict(range=[-1.5, 1.5], zeroline=True, zerolinewidth=2, zerolinecolor='black'),
        yaxis=dict(range=[-1.5, 1.5], scaleanchor="x", scaleratio=1, zeroline=True, zerolinewidth=2, zerolinecolor='black'),
        height=500,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)

# --- 3. Worked Example ---
st.header("3. Worked Example")
st.markdown("""
**Problem:** Prove the Pythagorean Identity: $\\sin^2(\\theta) + \\cos^2(\\theta) = 1$.

**Step-by-Step Solution:**
1.  **Start with the Unit Circle:** The equation of a circle centered at the origin with radius $r$ is $x^2 + y^2 = r^2$.
2.  **Define constraints:** Since it is a *unit* circle, the radius $r = 1$. Therefore, the equation is $x^2 + y^2 = 1$.
3.  **Substitute Trigonometric Definitions:** From the unit circle definitions, we know that for any angle $\\theta$:
    *   $x = \\cos(\\theta)$
    *   $y = \\sin(\\theta)$
4.  **Final Substitution:** Replace $x$ and $y$ in the circle equation.
    *   $(\\cos(\\theta))^2 + (\\sin(\\theta))^2 = 1$
    *   Written conventionally: $\\cos^2(\\theta) + \\sin^2(\\theta) = 1$.  \\*(Q.E.D)*
""")

# --- 4. Common Mistakes ---
st.header("4. Common Mistakes")
st.markdown("""
*   **Radians vs Degrees.** Trying to calculate `np.sin(90)` in Python hoping for `1.0`. Standard math libraries assume radians, so `90` radians is evaluated, yielding an incorrect result. Always convert `np.radians(90)`.
*   **Inverse Trig Range.** Forgetting that the inverse functions (like arcsin or arccos) only return values within a specific range (e.g., $[-\\pi/2, \\pi/2]$ for arcsin). The equation $\\sin(\\theta) = 0.5$ has infinite solutions, but $\\arcsin(0.5)$ gives only one angle in the first quadrant.
*   **Sign Quadrant Mistakes.** Forgetting the "All Students Take Calculus" mnemonic. Sine is positive in Q1, Q2. Cosine is positive in Q1, Q4. Tangent is positive in Q1, Q3.
""")

# --- 5. Real-World Application ---
st.header("5. Real-World Application")
st.markdown("""
**Engineering Application: AC Circuits and Signal Processing**

*   **Alternating Current (AC):** The voltage coming out of a standard wall socket is not constant; it follows a sinusoidal wave over time. $V(t) = V_{peak} \\sin(2\\pi f t + \\phi)$. Trigonometry is essential for calculating power, phase offsets, and impedance in these circuits.
*   **Signal Processing (Fourier Transforms):** Nearly any real-world signal (audio, radio waves, vibrations) can be mathematically decomposed into a sum of simple sine and cosine waves of different frequencies. 
""")
