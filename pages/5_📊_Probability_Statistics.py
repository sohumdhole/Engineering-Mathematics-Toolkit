import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import scipy.stats as stats

st.set_page_config(page_title="Probability & Statistics", page_icon="📊", layout="wide")

st.title("📊 Probability & Statistics: Uncertainty and Distributions")

# --- 1. Concept Summary ---
st.header("1. Concept Summary")
st.markdown("""
Probability and statistics provide the mathematical framework for handling uncertainty, making predictions, and drawing conclusions from data.

*   **Law of Large Numbers (LLN):** As the number of trials in an experiment increases, the average of the observed results will converge to the expected value (true probability).
*   **Normal Distribution:** The "bell curve". It describes many natural phenomena where data clusters around a central mean, with a symmetric drop-off on both sides.
*   **Central Limit Theorem (CLT):** One of the most important theorems in statistics. It states that the distribution of *sample means* approaches a normal distribution as the sample size gets larger, **regardless of the shape of the original population distribution**.
""")

# --- 2. Interactive Visualisation ---
st.header("2. Interactive Visualisation")

tab1, tab2, tab3 = st.tabs(["Law of Large Numbers", "Normal Distribution", "Central Limit Theorem"])

with tab1:
    st.subheader("Coin Toss Simulation: Law of Large Numbers")
    st.markdown("Watch how the cumulative proportion of 'Heads' approaches the theoretical $0.5$ probability as more coins are flipped.")
    
    trials_lln = st.slider("Number of Coin Tosses (Trials)", min_value=10, max_value=5000, value=100, step=10, key="lln_trials")
    
    # Simulate coin tosses (1 = Heads, 0 = Tails)
    tosses = np.random.binomial(1, 0.5, trials_lln)
    cumulative_heads = np.cumsum(tosses)
    cumulative_proportion = cumulative_heads / np.arange(1, trials_lln + 1)
    
    fig_lln = go.Figure()
    fig_lln.add_trace(go.Scatter(x=np.arange(1, trials_lln + 1), y=cumulative_proportion, mode='lines', name='Observed Proportion'))
    fig_lln.add_trace(go.Scatter(x=[1, trials_lln], y=[0.5, 0.5], mode='lines', line=dict(color='red', dash='dash'), name='Theoretical Expected (0.5)'))
    
    fig_lln.update_layout(title="Convergence of Coin Toss Probability", xaxis_title="Number of Tosses", yaxis_title="Proportion of Heads", yaxis_range=[0, 1], height=400)
    st.plotly_chart(fig_lln, use_container_width=True)

with tab2:
    st.subheader("Normal Distribution Viewer")
    col1_norm, col2_norm = st.columns([1, 2])
    
    with col1_norm:
        mu = st.slider("Mean ($\\mu$)", min_value=-10.0, max_value=10.0, value=0.0)
        sigma = st.slider("Standard Deviation ($\\sigma$)", min_value=0.1, max_value=5.0, value=1.0)
        st.markdown(f"**Formula:** \n\n $$f(x) = \\frac{{1}}{{\\sigma\\sqrt{{2\\pi}}}} e^{{-\\frac{1}{2}(\\frac{{x-\\mu}}{{\\sigma}})^2}}$$")

    with col2_norm:
        x_norm = np.linspace(mu - 4*sigma, mu + 4*sigma, 500)
        y_norm = stats.norm.pdf(x_norm, mu, sigma)
        
        fig_norm = go.Figure()
        fig_norm.add_trace(go.Scatter(x=x_norm, y=y_norm, mode='lines', fill='tozeroy', fillcolor='rgba(0,100,250,0.3)'))
        fig_norm.update_layout(title=f"Normal Distribution ~ N({mu:.1f}, {sigma:.1f}²)", xaxis_title="x", yaxis_title="Probability Density", height=400)
        
        # Add sigma lines
        for i in range(-3, 4):
            if i == 0: continue
            line_x = mu + i * sigma
            line_y = stats.norm.pdf(line_x, mu, sigma)
            fig_norm.add_shape(type="line", x0=line_x, y0=0, x1=line_x, y1=line_y, line=dict(color="red", width=1, dash="dot"))
            
        st.plotly_chart(fig_norm, use_container_width=True)

with tab3:
    st.subheader("Central Limit Theorem in Action")
    st.markdown("We will draw random samples from a heavily skewed **Exponential Distribution** and plot the distribution of their means.")
    
    col1_clt, col2_clt = st.columns([1, 2])
    with col1_clt:
        sample_size = st.slider("Size of each sample ($n$)", min_value=1, max_value=100, value=2, help="As 'n' gets larger, the resulting distribution becomes more normal.")
        num_samples = st.slider("Number of samples to draw", min_value=100, max_value=5000, value=1000)
    
    with col2_clt:
        # We sample from an exponential distribution (scale=1, mean=1, highly non-normal)
        population_scale = 1.0
        
        # Collect means of multiple samples
        sample_means = []
        for _ in range(num_samples):
            sample = np.random.exponential(scale=population_scale, size=sample_size)
            sample_means.append(np.mean(sample))
            
        fig_clt = go.Figure()
        # Histogram of sample means
        fig_clt.add_trace(go.Histogram(x=sample_means, histnorm='probability density', nbinsx=30, name="Sample Means", marker_color='green'))
        
        # Overlay ideal normal curve predictions
        ideal_mean = population_scale
        ideal_std = population_scale / np.sqrt(sample_size)
        x_ideal = np.linspace(min(sample_means), max(sample_means), 200)
        y_ideal = stats.norm.pdf(x_ideal, ideal_mean, ideal_std)
        fig_clt.add_trace(go.Scatter(x=x_ideal, y=y_ideal, mode='lines', line=dict(color='red', width=3), name="Theoretical Normal"))
        
        fig_clt.update_layout(title=f"Distribution of Sample Means (n={sample_size})", xaxis_title="Sample Mean", yaxis_title="Density", height=400)
        st.plotly_chart(fig_clt, use_container_width=True)


# --- 3. Worked Example ---
st.header("3. Worked Example")
st.markdown("""
**Problem:** In a factory producing resistors, the resistance values follow a Normal Distribution with mean $\\mu = 100\\Omega$ and standard deviation $\\sigma = 2\\Omega$. What percentage of resistors will have a resistance between $98\\Omega$ and $102\\Omega$?

**Step-by-Step Solution:**
1.  **Understand the bounds in terms of standard deviations.** 
    *   $98\\Omega$ is $100 - 2 = \\mu - 1\\sigma$
    *   $102\\Omega$ is $100 + 2 = \\mu + 1\\sigma$
2.  **Apply the Empirical Rule (68-95-99.7 Rule):**
    For any perfectly normal distribution:
    *   $\approx 68\\%$ of the data falls within $1\\sigma$ of the mean.
    *   $\approx 95\\%$ of the data falls within $2\\sigma$ of the mean.
    *   $\approx 99.7\\%$ of the data falls within $3\\sigma$ of the mean.
3.  **Conclusion:** Because the range $98$ to $102$ represents precisely $\\mu \pm 1\\sigma$, approximately **68%** of the resistors will fall within this acceptable range.
""")

# --- 4. Common Mistakes ---
st.header("4. Common Mistakes")
st.markdown("""
*   **Gambler’s Fallacy.** Believing that if a coin lands on heads 5 times in a row, it is "due" for a tails. The coin has no memory; each independent flip still has a 50% probability under the Law of Large Numbers.
*   **Misunderstanding the Central Limit Theorem.** The CLT states that the distribution of *the sample mean* becomes normal. It does **not** mean that as you collect more data, the *population* distribution magically becomes normal.
*   **Confusing Probability with Density.** For continuous distributions (like the Normal Distribution), evaluating the function at a single exact point (e.g., $P(X = 1.000)$) yields exactly 0 probability. We instead measure the *area under the curve* for a given range (e.g., $P(1.0 < X < 1.1)$).
""")

# --- 5. Real-World Application ---
st.header("5. Real-World Application")
st.markdown("""
**Engineering Application: Quality Control and Reliability**

*   **Manufacturing Quality Control (Six Sigma):** Engineers constantly monitor production lines. If a machine cutting bolts drifts so its product distribution shifts, the statistics alert the factory before defective products are shipped. "Six Sigma" targets a defect rate where the failure limits are $6\\sigma$ away from the mean.
*   **System Reliability & Risk Assessment:** Given failure rates for individual components (like engines on airplanes or servers in a data center), probability models compute the overall chance of a catastrophic system failure, defining maintenance schedules.
*   **Signal Processing:** When receiving a transmission from a satellite, the signal is buried in thermal "Gaussian Noise" (Normal Distribution). Statistics are used to filter the noise and recover the valid data stream.
""")
