import pytest
from unit_conversion.pressure import psig_to_psia, psia_to_psig

def test_psig_to_psia():
    assert psig_to_psia(1) == pytest.approx(15.696)
    assert psig_to_psia(10) == pytest.approx(24.696)

def test_psia_to_psig():
    assert psia_to_psig(15.696) == pytest.approx(1)
    assert psia_to_psig(24.696) == pytest.approx(10)