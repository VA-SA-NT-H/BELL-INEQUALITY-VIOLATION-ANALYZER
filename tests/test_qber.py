import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from metrics.qber import compute_qber

def test_qber():
    data = [{"outcome": 1}]*30 + [{"outcome": 0}]*70
    assert abs(compute_qber(data) - 0.3) < 1e-6
