from analyzer.qkd_tools import calculate_qber, calculate_keyrate

def test_qber():
    assert calculate_qber([0,1,0], [0,1,1]) == 1/3

def test_keyrate():
    assert calculate_keyrate(100, 0.1) == 100 * (1 - 0.2)