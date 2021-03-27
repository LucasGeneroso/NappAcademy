import pytest
from exercicio6 import calculo_porcentagem_entre_0_e_1

def test_exercicio06_cenario_1():
    assert calculo_porcentagem_entre_0_e_1(100, 0) == 0

def test_exercicio06_cenario_2():
    assert calculo_porcentagem_entre_0_e_1(100, 0.25) == 25

def test_exercicio06_cenario_3():
    assert calculo_porcentagem_entre_0_e_1(100, 0.50) == 50

def test_exercicio06_cenario_4():
    assert calculo_porcentagem_entre_0_e_1(100, 0.75) == 75

def test_exercicio06_cenario_5():
    assert calculo_porcentagem_entre_0_e_1(100, 1) == 100