# 📚 Engineering Mathematics Toolkit

An interactive, multi-page visualization application designed to serve as a high-quality teaching tool for undergraduate engineering mathematics. Built with **Python** and **Streamlit**, this application combines symbolic computation through **SymPy** and dynamic visualizations using **Plotly** and **SciPy**.

## 🎯 Project Overview

This toolkit helps students bridge the gap between abstract mathematical theory and applied engineering concepts. It currently supports the following modules:

- **📈 Calculus:** Explore rates of change and accumulation. Features an interactive symbolic Derivative and Integral visualizer.
- **🧮 Linear Algebra:** Understand 2D space manipulations through interactive Matrix transformation graphs mapping basis vectors.
- **📐 Trigonometry:** Master the Unit Circle visually, and reference proofs for core trigonometric identities.
- **🌊 Differential Equations:** Simulate dynamic systems (like exponential growth/decay) and compare numerical approximation methods against analytical solutions.
- **📊 Probability & Statistics:** Visualize uncertainty through a Law of Large Numbers coin toss simulator, a Normal Distribution explorer, and a Central Limit Theorem sampling visualizer.

Each module follows a strict pedagogical structure:
1. **Concept Summary:** Intuitive introduction to the topic.
2. **Interactive Visualisation:** Dynamic tools where students input variables and see the mathematics react in real-time.
3. **Worked Example:** A step-by-step breakdown of a sample problem.
4. **Common Mistakes:** Crucial warnings regarding frequent student pitfalls.
5. **Real-World Application:** Concrete engineering examples linking theory to practice.

## 🛠️ Installation & Setup

To run this project locally, you will need Python installed on your machine.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/EngineeringMathToolkit.git
   cd EngineeringMathToolkit
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv .venv
   
   # Activate on Windows:
   .venv\Scripts\activate
   # Activate on macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python -m streamlit run app.py
   ```
   The application will automatically pop up in your default web browser at `http://localhost:8501`.

## 💻 Technology Stack

- **Streamlit:** UI Framework and rapid web prototyping.
- **Plotly:** Interactive, responsive graphing library.
- **SymPy:** Symbolic mathematics (parsing text to math, algebraic differentiation/integration).
- **NumPy & SciPy:** High-performance numerical computations and statistical distributions.

## 👨‍💻 Author
Sohum Dhole
MSc. in Business Analytics
Dublin Business School.
