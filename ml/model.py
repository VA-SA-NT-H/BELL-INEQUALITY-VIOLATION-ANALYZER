from sklearn.ensemble import IsolationForest

def train_model(data):
    X = [[d['alice_angle'], d['bob_angle'], d['outcome']] for d in data]
    model = IsolationForest()
    model.fit(X)
    return model
