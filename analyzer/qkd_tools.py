def calculate_qber(alice_bits, bob_bits):
    errors = sum([a != b for a, b in zip(alice_bits, bob_bits)])
    return errors / len(alice_bits) if alice_bits else 0.0

def calculate_keyrate(length, qber):
    r0 = length  # assume 1 key bit 
    return r0 * (1 - 2 * qber)