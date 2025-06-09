def compute_key_rate(qber):
    return max(0, 1 - 2 * qber)