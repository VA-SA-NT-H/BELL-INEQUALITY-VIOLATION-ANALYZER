from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np

def run_bell_test(rounds, alice_angles, bob_angles):
    simulator = AerSimulator()
    alice_bits, bob_bits = [], []
    alice_bases, bob_bases = [], []
    final_key = []

    correlations = {}

    for i in range(3):
        for j in range(3):
            correlations[(i, j)] = []

    for _ in range(rounds):
        a_basis = np.random.randint(0, 3)  # 0 to 2
        b_basis = np.random.randint(0, 3)
        alice_bases.append(a_basis)
        bob_bases.append(b_basis)

        theta_a = alice_angles[a_basis]
        theta_b = bob_angles[b_basis]

        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.cx(0, 1)

        qc.ry(2 * theta_a, 0)
        qc.ry(2 * theta_b, 1)

        qc.measure([0, 1], [0, 1])

        compiled = transpile(qc, simulator)
        result = simulator.run(compiled).result()
        counts = result.get_counts()
        result_str = list(counts.keys())[0]

        alice_bit = int(result_str[1])
        bob_bit = int(result_str[0])

        alice_bits.append(alice_bit)
        bob_bits.append(bob_bit)

        if a_basis == b_basis:
            final_key.append(alice_bit)

        correlation = 1 if alice_bit == bob_bit else -1
        correlations[(a_basis, b_basis)].append(correlation)

    mismatches = sum(a != b for a, b in zip(alice_bits, bob_bits))
    qber = mismatches / rounds

    def mean_corr(vals):
        return sum(vals) / len(vals) if vals else 0

    # For 3x3 CHSH-like structure (custom Bell scenario)
    # Choose which 4 of the 9 correlations to compute S
    E_00 = mean_corr(correlations[(0, 0)])
    E_01 = mean_corr(correlations[(0, 1)])
    E_10 = mean_corr(correlations[(1, 0)])
    E_11 = mean_corr(correlations[(1, 1)])

    s_value = abs(E_00 - E_01 + E_10 + E_11)

    return {
        "s_value": s_value,
        "qber": qber,
        "final_key": final_key,
        "alice_bits": alice_bits,
        "bob_bits": bob_bits,
        "alice_bases": alice_bases,
        "bob_bases": bob_bases
    }


