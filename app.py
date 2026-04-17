import streamlit as st

st.set_page_config(
    page_title="Engineering Mathematics Toolkit",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("📚 Engineering Mathematics Toolkit")
st.subheader("Interactive Teaching Tool for Undergraduate Engineering Students")

st.markdown("""
Welcome to the **Engineering Mathematics Toolkit**. This application is designed to be a high-quality, interactive learning environment to help undergraduate students master core mathematical concepts used in engineering.

### 🎯 How to Use This Toolkit

Navigate using the sidebar to explore different mathematical modules. Every module is structured to guide your learning process step-by-step:

1.  **Concept Summary:** A brief, intuitive explanation of the topic.
2.  **Interactive Visualisation:** Dynamic tools where you can input parameters to see how the mathematics works in real-time.
3.  **Worked Example:** A clear, step-by-step breakdown of a sample problem.
4.  **Common Mistakes:** Typical pitfalls and errors students make, and how to avoid them.
5.  **Real-World Application:** How this mathematical concept is applied in real engineering scenarios.

---

### 🧰 Available Modules

*   **📈 Calculus:** Visualize derivatives and integrals. Understand rates of change and accumulation.
*   **🧮 Linear Algebra:** Explore 2D matrix transformations and understand how space is manipulated.
*   **📐 Trigonometry:** Master the unit circle and see proofs of core trigonometric identities.
*   **🌊 Differential Equations:** Model dynamic systems such as exponential growth and decay.
*   **📊 Probability & Statistics:** Simulate coin tosses, understand the Normal Distribution, and observe the Central Limit Theorem in action.

---
*Created for educational purposes.*
""")

# Sidebar info
with st.sidebar:
    st.info("Select a module from the pages above to begin learning.")
