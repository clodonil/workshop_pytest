from src.exemplo1 import soma, produto
import pytest


@pytest.mark.numeros
def test_deve_retorna_a_soma():
    assert soma(10, 30) == 40
    assert soma(1, 2) == 3


@pytest.mark.strings
@pytest.mark.skip(reason="Não esta funcionando ainda")
def test_deve_retornar_a_soma_de_string():
    assert soma('a', 'b') == 'ab'


def test_deve_retornar_o_produto_de_dois():
    assert produto(2, 2) == 4
