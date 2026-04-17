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

## Screenshots
<img width="1920" height="871" alt="Screenshot (938)" src="https://github.com/user-attachments/assets/eadaefb5-67ac-4c10-9d2d-2960c5660ac1" />
<img width="1920" height="995" alt="Screenshot (939)" src="https://github.com/user-attachments/assets/7001b0c6-506c-47b3-a92c-a27f602060e0" />
<img width="1920" height="975" alt="Screenshot (940)" src="https://github.com/user-attachments/assets/120239aa-48be-4583-a0f5-8fca17f76919" />
<img width="1920" height="1008" alt="Screenshot (941)" src="https://github.com/user-attachments/assets/f1786d9d-d3a5-4973-830b-991ed5a6dd00" />
<img width="1920" height="1004" alt="Screenshot (942)" src="https://github.com/user-attachments/assets/a473bed6-f620-42c4-9345-ca83595ae603" />
<img width="1920" height="1011" alt="Screenshot (943)" src="https://github.com/user-attachments/assets/e4ab6149-68b8-4467-a387-6382d6a2e5cc" />
<img width="1920" height="881" alt="Screenshot (944)" src="https://github.com/user-attachments/assets/84dacf26-fda9-4358-a4cf-f9221a35a959" />
<img width="1920" height="1017" alt="Screenshot (945)" src="https://github.com/user-attachments/assets/4ecf77f6-b503-4124-90b7-d5f25769b2cc" />
<img width="1920" height="1010" alt="Screenshot (946)" src="https://github.com/user-attachments/assets/95d86c2e-30ba-4bcb-aaf3-39e379bf1292" />
<img width="1920" height="999" alt="Screenshot (947)" src="https://github.com/user-attachments/assets/5511ee0a-dd39-4f30-b000-dbf10a54df43" />
<img width="1920" height="988" alt="Screenshot (948)" src="https://github.com/user-attachments/assets/3d619552-7827-4217-b1b5-7b573cd14b93" />








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
