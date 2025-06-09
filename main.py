import streamlit as st
import pandas as pd
import json
import os
from qkd.simulate import run_simulation
from metrics.chsh import compute_chsh
from metrics.qber import compute_qber
from metrics.key_rate import compute_key_rate
from ml.detector import detect_anomalies
from visual.visualize import plot_metrics

st.set_page_config(page_title="Bell Inequality Violation Analyzer", layout="centered")

st.title("🔐 Bell Inequality Violation Analyzer (E91-QKD)")
st.markdown("---")

# Sidebar for configuration
rounds = st.sidebar.slider("Number of Rounds", 100, 5000, 1000, step=100)
threshold = st.sidebar.slider("Anomaly Threshold", 0.0, 1.0, 0.5)

# Run simulation
st.info("Running simulation...")
data = run_simulation(rounds)

# Compute metrics
st.success("Simulation complete. Calculating metrics...")
s_value = compute_chsh(data)
qber = compute_qber(data)
key_rate = compute_key_rate(qber)

# Show metrics
st.metric("CHSH S Value", f"{s_value:.2f}")
st.metric("QBER", f"{qber:.2f}")
st.metric("Key Rate", f"{key_rate:.2f}")

# Detect anomalies
st.markdown("### 🔍 Anomaly Detection")
anomalies = detect_anomalies(data)
st.write(f"🚨 Anomalies detected: {len(anomalies)}")

# Convert list of dicts to DataFrame
anomaly_df = pd.DataFrame(anomalies)

# Display
if not anomaly_df.empty:
    st.dataframe(anomaly_df)
else:
    st.success("✅ No anomalies detected.")

# Visualize
st.markdown("### 📊 Visualizations")
fig = plot_metrics(s_value, qber, key_rate, anomalies)
st.pyplot(fig)

# Optional: Save results
if st.button("💾 Save Results"):
    os.makedirs("data", exist_ok=True)
    
    # Save raw simulation data as JSON
    with open("data/sample_run.json", "w") as f:
        json.dump(data, f, indent=2)
    
    # Convert anomalies list to DataFrame before saving
    if anomalies:
        anomalies_df = pd.DataFrame(anomalies)
        anomalies_df.to_csv("data/anomaly_results.csv", index=False)
        st.success("✅ Results saved to `data/` folder.")
    else:
        st.info("No anomalies to save.")