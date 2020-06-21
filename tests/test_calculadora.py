from src.exemplo2 import Calculadora, CalculadoraError
import pytest


class TestCalculadora:

    def test_deve_retornar_uma_soma(self):
        obj = Calculadora()
        assert obj.soma(10, 10) == 20

    def test_deve_retornar_um_execption(self):
        obj = Calculadora()
        with pytest.raises(CalculadoraError):
            obj.soma('um', 1)

    def test_deve_retornar_um_execption_na_soma_de_duas_palavras(self):
        obj = Calculadora()
        with pytest.raises(CalculadoraError):
            obj.soma('um', 'dois')

    def test_deve_retonar_uma_subtrair(self):
        obj = Calculadora()
        assert obj.subtrair(20, 10) == 10

    def test_deve_retonar_uma_dividir(self):
        obj = Calculadora()
        assert obj.dividir(10, 2) == 5

    def test_deve_retornar_um_execption_divisao_por_zero(self):
        obj = Calculadora()
        with pytest.raises(CalculadoraError):
            obj.dividir(10, 0)

    def test_deve_retonar_uma_multiplicacao(self):
        obj = Calculadora()
        assert obj.multiplicar(2, 2) == 4

    def test_deve_retornar_true_para_numeros(self):
        obj = Calculadora()
        assert obj.check_isnumber(10) == True
        assert obj.check_isnumber(10.1) == True
        assert obj.check_isnumber('um') == False

    @pytest.mark.parametrize(
        ("n", "resultado"),
        [
            (10, True),
            (10.1, True),
            ('string', False),
            ([], False)
        ]
    )
    def test_deve_validar_parametros(self, n, resultado):
        obj = Calculadora()
        assert obj.check_isnumber(n) == resultado
