import pytest
from gas_calculator.ppm_to_fraction import ppm_to_fraction

def test_ppm_to_fraction():
    assert ppm_to_fraction(200) == pytest.approx(0.02)

def test_ppm_high():
    with pytest.raises(ValueError): ppm_to_fraction(1000001)

def test_ppm_low():
    with pytest.raises(ValueError): ppm_to_fraction(-1)