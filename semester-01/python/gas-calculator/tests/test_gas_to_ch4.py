import pytest
from gas_calculator.gas_to_ch4 import gas_to_ch4

def test_gas_to_ch4():
    assert gas_to_ch4(50, 60) == pytest.approx(30)
    
def test_negative_flow():
    with pytest.raises(ValueError): gas_to_ch4(-1, 60)

def test_methane_high():
    with pytest.raises(ValueError): gas_to_ch4(50, 101)

def test_methane_low():
    with pytest.raises(ValueError): gas_to_ch4(50, -1)