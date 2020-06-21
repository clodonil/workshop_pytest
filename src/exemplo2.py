from numbers import Number
import sys


class CalculadoraError(Exception):
    pass


class Calculadora:
    def soma(self, n1, n2):
        if not self.check_isnumber(n1) and not self.check_isnumber(n2):
            raise(CalculadoraError())
        try:
            return n1 + n2
        except TypeError as error:
            raise CalculadoraError(error)

    def check_isnumber(self, n1):
        if isinstance(n1, Number):
            return True
        else:
            return False

    def check_number(self, n1):
        if not isinstance(n1, Number):
            raise(CalculadoraError(f'{n1} nao eh numero.'))

    def subtrair(self, n1, n2):
        self.check_number(n1)
        self.check_number(n2)
        return n1 - n2

    def dividir(self, n1, n2):
        self.check_number(n1)
        self.check_number(n2)
        try:
            return n1 / n2
        except ZeroDivisionError as error:
            raise CalculadoraError("nao pode dividir por zero!")

    def multiplicar(self, n1, n2):
        self.check_number(n1)
        self.check_number(n2)
        return n1 * n2


# if __name__ == "__main__":
#     calculadora = Calculadora()
#     operacoes = [
#         calculadora.soma,
#         calculadora.subtrair,
#         calculadora.multiplicar,
#         calculadora.dividir,
#     ]

#     while True:
#         print(" Vamos Calcular ".center(50, '-'))

#         for i, operacao in enumerate(operacoes, start=1):
#             print(f'{i}: {operacao.__name__}')

#         print('q: Sair')
#         op = input("Escolha a operacao: ")

#         if op == 'q':
#             sys.exit()

#         n1 = float(input("Valor de N1? "))
#         n2 = float(input("Valor de N2? "))
#         op_index = int(op)
#         print(''.center(50, '#'))
#         try:
#             result = operacoes[op_index - 1](n1, n2)
#             print(f'Resultado: {result}'.center(50, ' '))
#         except CalculadoraError as error:
#             print(f'Resultado: {error}'.center(50, ' '))
#         print(''.center(50, '#'))
