import pytest
from unit_conversion.mass import lb_to_kg, kg_to_lb

def test_lb_to_kg():
    assert lb_to_kg(1000) == pytest.approx(453.59237)
    assert lb_to_kg(5000) == pytest.approx(2267.96185)

def test_kg_to_lb():
    assert kg_to_lb(453.59237) == pytest.approx(1000)
    assert kg_to_lb(2267.96185) == pytest.approx(5000)