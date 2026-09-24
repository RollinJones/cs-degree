import pytest
from gas_calculator.fraction_to_h2s import fraction_to_h2s

def test_fraction_to_h2s():
    assert fraction_to_h2s(50, 0.02) == pytest.approx(0.01)
    
def test_negative_flow():
    with pytest.raises(ValueError): fraction_to_h2s(-1, 0.02)