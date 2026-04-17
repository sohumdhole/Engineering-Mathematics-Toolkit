import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Linear Algebra", page_icon="🧮", layout="wide")

st.title("🧮 Linear Algebra: Matrix Transformations")

# --- 1. Concept Summary ---
st.header("1. Concept Summary")
st.markdown("""
Linear Algebra is the mathematics of data and space. Core concepts include:
*   **Vectors:** Quantities with magnitude and direction, often represented as arrows or coordinate pairs.
*   **Matrices:** Grids of numbers that act as functions transforming vectors.
*   **Transformations:** When you multiply a vector by a matrix, the vector moves. A matrix represents a *linear transformation*, changing the space by rotating, scaling, or shearing it while keeping grid lines parallel and evenly spaced.
*   **Eigenvectors & Eigenvalues:** Special vectors that do not change direction during a specific transformation, only their magnitude (scaled by the eigenvalue).
""")

# --- 2. Interactive Visualisation ---
st.header("2. Interactive Visualisation")
st.markdown("Edit the 2x2 matrix to see how it transforms the standard 2D grid and the basis vectors $\\hat{i}$ and $\\hat{j}$.")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Transformation Matrix")
    st.markdown("Default is a shear matrix `[[1, 2], [0, 1]]`")
    
    # Input for 2x2 Matrix
    row1_col1 = st.number_input("M[0,0]", value=1.0)
    row1_col2 = st.number_input("M[0,1]", value=2.0)
    row2_col1 = st.number_input("M[1,0]", value=0.0)
    row2_col2 = st.number_input("M[1,1]", value=1.0)
    
    M = np.array([[row1_col1, row1_col2], 
                  [row2_col1, row2_col2]])
    
    st.latex(f"M = \\begin{{bmatrix}} {row1_col1} & {row1_col2} \\\\ {row2_col1} & {row2_col2} \\end{{bmatrix}}")
    
    det = np.linalg.det(M)
    st.markdown(f"**Determinant ($|M|$):** `{det:.2f}` (represents the scaling factor of areas)")
    
    # Display eigenvalues if they are real
    try:
        eigenvals, eigenvecs = np.linalg.eig(M)
        if np.isrealobj(eigenvals) or not np.any(np.iscomplex(eigenvals)):
            st.markdown(f"**Eigenvalues ($\\lambda$):** `{eigenvals[0].real:.2f}` and `{eigenvals[1].real:.2f}`")
        else:
            st.markdown(f"**Eigenvalues:** Complex (indicates rotation is present)")
    except Exception:
        pass

with col2:
    # Setup standard square
    square = np.array([[0, 1, 1, 0, 0], [0, 0, 1, 1, 0]]) # 2x5 array
    transformed_square = M @ square
    
    # Basis vectors
    i_hat = np.array([1, 0])
    j_hat = np.array([0, 1])
    
    t_i_hat = M @ i_hat
    t_j_hat = M @ j_hat
    
    fig = go.Figure()
    
    # Original Square
    fig.add_trace(go.Scatter(x=square[0,:], y=square[1,:], mode='lines', fill='toself', name='Original Space', fillcolor='rgba(0,0,255,0.1)', line=dict(color='blue', dash='dash')))
    
    # Transformed Square
    fig.add_trace(go.Scatter(x=transformed_square[0,:], y=transformed_square[1,:], mode='lines', fill='toself', name='Transformed Space', fillcolor='rgba(255,0,0,0.3)', line=dict(color='red')))
    
    # Add origin
    fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker=dict(color='black', size=10), showlegend=False))
    
    # Add Basis Vectors
    # Original i_hat, j_hat (using annotations to draw arrows)
    fig.add_annotation(x=i_hat[0], y=i_hat[1], ax=0, ay=0, xref='x', yref='y', axref='x', ayref='y', text='', showarrow=True, arrowhead=2, arrowsize=1.5, arrowcolor='blue')
    fig.add_annotation(x=j_hat[0], y=j_hat[1], ax=0, ay=0, xref='x', yref='y', axref='x', ayref='y', text='', showarrow=True, arrowhead=2, arrowsize=1.5, arrowcolor='green')
    
    # Transformed i_hat, j_hat
    fig.add_annotation(x=t_i_hat[0], y=t_i_hat[1], ax=0, ay=0, xref='x', yref='y', axref='x', ayref='y', text='', showarrow=True, arrowhead=2, arrowsize=1.5, arrowcolor='red')
    fig.add_annotation(x=t_j_hat[0], y=t_j_hat[1], ax=0, ay=0, xref='x', yref='y', axref='x', ayref='y', text='', showarrow=True, arrowhead=2, arrowsize=1.5, arrowcolor='orange')
    
    # Add text labels for basis vectors
    fig.add_trace(go.Scatter(x=[i_hat[0]/2, j_hat[0]/2, t_i_hat[0]/2, t_j_hat[0]/2], 
                             y=[i_hat[1]/2, j_hat[1]/2, t_i_hat[1]/2, t_j_hat[1]/2], 
                             mode='text', text=['i', 'j', "M(i)", "M(j)"], showlegend=False, textfont=dict(color=['blue', 'green', 'red', 'orange'])))
    
    axis_limit = max(4, np.max(np.abs(transformed_square)) + 1)
    
    fig.update_layout(
        title="2D Space Transformation",
        xaxis=dict(range=[-axis_limit, axis_limit], zeroline=True, zerolinewidth=2, zerolinecolor='black'),
        yaxis=dict(range=[-axis_limit, axis_limit], zeroline=True, zerolinewidth=2, zerolinecolor='black', scaleanchor="x", scaleratio=1),
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)

# --- 3. Worked Example ---
st.header("3. Worked Example")
st.markdown("""
**Problem:** Apply a 90-degree counter-clockwise rotation to the vector $\\vec{v} = \\begin{bmatrix} 2 \\\\ 1 \\end{bmatrix}$.

**Step-by-Step Solution:**
1.  **Define the Rotation Matrix:** The matrix for a rotation by angle $\\theta$ is:
    $$R_\\theta = \\begin{bmatrix} \\cos(\\theta) & -\\sin(\\theta) \\\\ \\sin(\\theta) & \\cos(\\theta) \\end{bmatrix}$$
2.  **Evaluate for 90 degrees ($\\pi/2$ radians):**
    $$R_{90} = \\begin{bmatrix} 0 & -1 \\\\ 1 & 0 \\end{bmatrix}$$
3.  **Perform Matrix Multiplication:** Multiply the matrix by the vector.
    $$R_{90} \\vec{v} = \\begin{bmatrix} 0 & -1 \\\\ 1 & 0 \\end{bmatrix} \\begin{bmatrix} 2 \\\\ 1 \\end{bmatrix} = \\begin{bmatrix} (0)(2) + (-1)(1) \\\\ (1)(2) + (0)(1) \\end{bmatrix} = \\begin{bmatrix} -1 \\\\ 2 \\end{bmatrix}$$
4.  **Conclusion:** The point $(2, 1)$ rotates to $(-1, 2)$.
""")

# --- 4. Common Mistakes ---
st.header("4. Common Mistakes")
st.markdown("""
*   **Order of Operations.** Matrix multiplication is non-commutative. $AB \\neq BA$. The transformation applied first must be written on the *right* side of the vector ($M_2 M_1 \\vec{v}$ applies $M_1$ first).
*   **Misinterpreting the Determinant.** A determinant of zero does *not* mean the vectors disappear. It means the 2D space has been squished down into a single 1D line or a point (loss of dimensionality). Areas become zero.
*   **Confusing rows and columns.** When writing out the transformation matrix, remember that the columns map to where the basis vectors land. The first column is where $\\hat{i}$ goes, and the second column is where $\\hat{j}$ goes.
""")

# --- 5. Real-World Application ---
st.header("5. Real-World Application")
st.markdown("""
**Engineering Application: Computer Graphics and Robotics**

*   **Computer Graphics:** Every time you rotate, scale, or move a 3D object in a video game or CAD software, the graphics engine is rapidly applying matrix multiplications to the thousands of coordinate vectors defining the object's vertices.
*   **Robotics:** The position of a robotic arm's end-effector (like a gripper) relative to its base is calculated using "forward kinematics". This involves multiplying a chain of Transformation Matrices, each representing the rotation and length of a joint segment.
""")
