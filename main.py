import streamlit as st
from analyzer.bell_test import run_bell_test
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import math

def plot_metric_bar(s_value, qber, key_rate):
    metrics = ['CHSH S-Value', 'QBER', 'Key Rate']
    values = [s_value, qber, key_rate]

    colors = ['green' if s_value > 2 else 'red', 'orange', 'blue']

    fig = go.Figure([go.Bar(
        x=metrics,
        y=values,
        marker_color=colors,
        text=[f"{v:.4f}" for v in values],
        textposition="auto"
    )])

    fig.update_layout(
        title='📊 CHSH, QBER & Key Rate Overview',
        yaxis_title='Value',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

#Raw data representation
def plot_interactive_raw_bits(alice_bits, bob_bits):
    rounds = list(range(len(alice_bits)))
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=rounds, y=alice_bits,
        mode='lines+markers',
        name='Alice Bits',
        line=dict(color='blue'),
        marker=dict(symbol='circle', size=6)
    ))

    fig.add_trace(go.Scatter(
        x=rounds, y=bob_bits,
        mode='lines+markers',
        name='Bob Bits',
        line=dict(color='red'),
        marker=dict(symbol='x', size=6)
    ))

    fig.update_layout(
        title='🧪 Interactive Raw Bits Over Rounds',
        xaxis_title='Round',
        yaxis_title='Bit Value (0 or 1)',
        yaxis=dict(tickmode='array', tickvals=[0, 1]),
        legend=dict(x=0, y=1.1, orientation='h'),
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)


# Define the plot function
def plot_bit_matches(alice_bits, bob_bits):
    rounds = list(range(len(alice_bits)))
    match_status = ['Match' if a == b else 'Mismatch' for a, b in zip(alice_bits, bob_bits)]

    df = pd.DataFrame({
        "Round": rounds,
        "Match Status": match_status,
        "Bit Value": alice_bits,  # show Alice's bits
    })

    fig = px.scatter(
        df,
        x="Round",
        y="Bit Value",
        color="Match Status",
        color_discrete_map={"Match": "green", "Mismatch": "red"},
        title="🟢 Bit Match vs 🔴 Mismatch per Round",
        height=400
    )
    fig.update_layout(yaxis=dict(tickmode='array', tickvals=[0, 1]))
    st.plotly_chart(fig, use_container_width=True)

# Optional: Page setup
st.set_page_config(page_title="BIV Analyzer", layout="wide")
st.title("🔐 Bell Inequality Violation Analyzer (BIVA)")

# Slider for round selection
rounds = st.slider("🔄 Number of Rounds", min_value=10, max_value=1000, value=100, step=1)

st.subheader("📐 Measurement Angles (in degrees)")

col1, col2 = st.columns(2)

with col1:
    alice_angle_deg_0 = st.number_input("Alice Angle 0 (°)", value=0.0)
    alice_angle_deg_1 = st.number_input("Alice Angle 1 (°)", value=45.0)
    alice_angle_deg_2 = st.number_input("Alice Angle 2 (°)", value=90.0)

with col2:
    bob_angle_deg_0 = st.number_input("Bob Angle 0 (°)", value=22.5)
    bob_angle_deg_1 = st.number_input("Bob Angle 1 (°)", value=67.5)
    bob_angle_deg_2 = st.number_input("Bob Angle 2 (°)", value=112.5)

# Convert to radians
alice_angles = [math.radians(alice_angle_deg_0),
                math.radians(alice_angle_deg_1),
                math.radians(alice_angle_deg_2)]

bob_angles = [math.radians(bob_angle_deg_0),
              math.radians(bob_angle_deg_1),
              math.radians(bob_angle_deg_2)]

# Run analysis
results = None
if st.button("▶️ Run Analysis"):
    results = run_bell_test(rounds, alice_angles, bob_angles)

# If results are available
if results is not None:
    st.subheader("📈 Quantum Results")

    s_value = results.get("s_value", None)
    if s_value is not None:
        st.metric("CHSH S-Value", s_value)
        if s_value > 2:
            st.success("✅ Bell Violation Detected — Entanglement Confirmed")
        else:
            st.error("❌ No Violation — Not Entangled")
    else:
        st.warning("⚠️ CHSH S-Value not computed in this run.")

    # st.metric("CHSH S-Value", results['s_value'])
    st.metric("QBER (Quantum Bit Error Rate)", f"{results['qber']*100:.2f}%")
    st.metric("Final Key Length", len(results['final_key']))
    # st.metric("Final Key ", results['final_key'])
    st.text(f"🔑 Final Key: {''.join(map(str, results['final_key']))}")

    # 📉 Compute key rate (key bits / rounds)
    key_rate = len(results['final_key']) / rounds

    # 📊 Bar chart for overview
    plot_metric_bar(results['s_value'], results['qber'], key_rate)


    # Line chart
    st.subheader("📊 Raw Quantum Bits (Interactive Chart)")
    plot_interactive_raw_bits(results["alice_bits"], results["bob_bits"])

    st.subheader("🎯 Bit Agreement Visualization (Match vs Mismatch)")
    plot_bit_matches(results["alice_bits"], results["bob_bits"])

    # Table display
    df = pd.DataFrame({
        "Round": list(range(1,rounds+1)),
        "Alice Bit": results["alice_bits"],
        "Bob Bit": results["bob_bits"],
        "Alice Basis": results["alice_bases"],
        "Bob Basis": results["bob_bases"]
    })
    st.subheader("🧾 Round-wise Bit Data")
    st.dataframe(df)

else:
    st.info("Click ▶️ Run Analysis to start the test.")
