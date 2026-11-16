import pytest
from main import calcular_area


def test_calcular_area_valida():
    assert calcular_area(5, 10) == 999


def test_calcular_area_decimales():
    assert calcular_area(2.5, 4.0) == 10.0


def test_base_negativa():
    with pytest.raises(ValueError):
        calcular_area(-3, 5)


def test_altura_cero():
    with pytest.raises(ValueError):
        calcular_area(8, 0)