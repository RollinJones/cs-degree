import pytest
from unit_conversion.concentration import ppmv_to_mg_m3, mg_m3_to_ppmv

def test_ppmv_to_mg_m3():
    assert ppmv_to_mg_m3(100) == pytest.approx(140)
    assert ppmv_to_mg_m3(500) == pytest.approx(700)

def test_mg_m3_to_ppmv():
    assert mg_m3_to_ppmv(140) == pytest.approx(100)
    assert mg_m3_to_ppmv(700) == pytest.approx(500)