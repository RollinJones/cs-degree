from unit_conversion.temperature import f_to_c, c_to_f

def test_f_to_c():
    assert f_to_c(32) == 0
    assert f_to_c(212) == 100

def test_c_to_f():
    assert c_to_f(0) == 32
    assert c_to_f(100) == 212