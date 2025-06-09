import numpy as np
from qkd.angles import get_angles

def run_simulation(rounds=1000):
    alice_angles, bob_angles = get_angles()
    results = []
    for _ in range(rounds):
        a = np.random.choice(alice_angles)
        b = np.random.choice(bob_angles)
        outcome = int(np.random.rand() > 0.5)
        results.append({"alice_angle": a, "bob_angle": b, "outcome": outcome})
    return results