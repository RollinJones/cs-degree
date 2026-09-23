import pytest
from unit_conversion.flow import scfm_to_m3_hr, m3_hr_to_scfm

def test_ppmv_to_mg_m3():
    assert scfm_to_m3_hr(100) == pytest.approx(169.9)
    assert scfm_to_m3_hr(500) == pytest.approx(849.5)

def test_m3_hr_to_scfm():
    assert m3_hr_to_scfm(169.9) == pytest.approx(100)
    assert m3_hr_to_scfm(849.5) == pytest.approx(500)