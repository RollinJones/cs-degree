import pytest
from unit_conversion.volume import ft3_to_m3, m3_to_ft3

def test_ft3_to_m3():
    assert ft3_to_m3(100) == pytest.approx(2.83168466)
    assert ft3_to_m3(200) == pytest.approx(5.66336932)

def test_m3_to_ft3():
    assert m3_to_ft3(2.83168466) == pytest.approx(100)
    assert m3_to_ft3(5.66336932) == pytest.approx(200)