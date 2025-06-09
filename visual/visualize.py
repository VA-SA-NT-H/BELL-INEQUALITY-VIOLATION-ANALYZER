import matplotlib.pyplot as plt

def plot_metrics(s_value, qber, key_rate, anomalies):
    fig, ax = plt.subplots(figsize=(6, 4))  # or adjust size as needed
    
    metrics = ["S Value", "QBER", "Key Rate"]
    values = [s_value, qber, key_rate]
    bars = ax.bar(metrics, values, color=["skyblue", "salmon", "lightgreen"])

    # Annotate bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.01, f"{yval:.2f}",
                ha='center', va='bottom')

    ax.set_title("Quantum Metrics")
    ax.set_ylim(0, 3)
    
    return fig 