import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from metrics.chsh import compute_chsh

def test_chsh():
    data = [{"alice_angle": 0, "bob_angle": 0, "outcome": 1} for _ in range(100)]
    assert compute_chsh(data) > 2