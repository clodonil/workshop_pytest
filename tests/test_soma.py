from src.exemplo1 import soma
import pytest


def test_deve_retorna_a_soma():
    assert soma(10, 30) == 40
    assert soma(1, 2) == 3
