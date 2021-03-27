import pytest
from exercicio7 import calculo_porcentagem_entre_0_e_100

def test_exercicio07_cenario_1():
    with pytest.raises(ValueError) as error:
        calculo_porcentagem_entre_0_e_100(100, 0)
    assert str(error.value) == "Porcentagem precisa estar entre 0 e 100"

def test_exercicio07_cenario_2():
    assert calculo_porcentagem_entre_0_e_100(100, 25) == 25

def test_exercicio07_cenario_3():
    assert calculo_porcentagem_entre_0_e_100(100, 50) == 50

def test_exercicio07_cenario_4():
    assert calculo_porcentagem_entre_0_e_100(100, 75) == 75

def test_exercicio07_cenario_5():
    with pytest.raises(ValueError) as error:
        calculo_porcentagem_entre_0_e_100(100, 100)
    assert str(error.value) == "Porcentagem precisa estar entre 0 e 100"