import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from metrics.key_rate import compute_key_rate

def test_key_rate():
    assert compute_key_rate(0.1) == 0.8
    assert compute_key_rate(0.6) == 0
