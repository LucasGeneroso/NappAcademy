import pytest
from exercicio8 import juros_compostos

def test_exercicio08_cenario_1():
    assert juros_compostos(100, 1, 12) == 112.68

def test_exercicio08_cenario_2():
    assert juros_compostos(100, 25, 12) == 1455.19

def test_exercicio08_cenario_3():
    assert juros_compostos(100, 50, 12) == 12974.63

def test_exercicio08_cenario_4():
    assert juros_compostos(100, 75, 12) == 82500.5

def test_exercicio08_cenario_5():
    assert juros_compostos(100, 99, 12) == 385688.7