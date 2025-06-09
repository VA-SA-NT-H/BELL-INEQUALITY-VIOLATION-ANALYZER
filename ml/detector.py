from ml.model import train_model

def detect_anomalies(data):
    model = train_model(data)
    X = [[d['alice_angle'], d['bob_angle'], d['outcome']] for d in data]
    preds = model.predict(X)
    return [d for d, p in zip(data, preds) if p == -1]