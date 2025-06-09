def compute_qber(data):
    errors = sum(1 for d in data if d['outcome'] == 1)
    return errors / len(data)