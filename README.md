# Testando com Pytest

documentação para o workshop de PyTest

* Unittest
* Nose
* pytest

# Porque Testar


1. Códigos são escritos por seres humanos e seres humanos erram;

2. Programas contém erros (Bugs)
    - Sintaxe
    - Lógica

3. Bugs podem causar catástrofes;

4. Bugs podem causar desconforto;

5. Testes automatizados reduzem Bugs em features;

6. Desenvolver com testes da segurança no lançamento de novas features;


# Regras gerais

1. Uma unidade de teste deve se concentrar em um pequeno número de funcionalidades e provar que tudo está correto.

2. Cada unidade de teste deve ser totalmente independente. Cada teste deve ser capaz de executar sozinho, e também dentro do conjunto de teste, independentemente da ordem em que são chamados. 

3. Tente arduamente fazer testes que funcionem rapidamente. Se um único teste precisa de mais de alguns milissegundos para executar, o desenvolvimento será diminuído ou os testes não serão executados com a frequência desejável.

4. Aprenda suas ferramentas e aprenda como executar uma única prova ou um caso de teste. Então, ao desenvolver uma função dentro de um módulo, execute os testes dessa função freqüentemente, idealmente automaticamente quando você salvar o código.

5. É uma boa ideia implementar um hook que executa todos os testes antes de enviar o código para um repositório compartilhado.

6. O primeiro passo quando você estiver depurando o seu código é escrever um novo teste identificando o bug. Embora nem sempre seja possível, esses testes de detecção de falhas estão entre os mais valiosos itens de código do seu projeto.

7. Use nomes longos e descritivos para testar funções. 


# Instalação:

Para começarmos a realizar os testes dos nossos projetos, precisamos instalar o framework `pytest`

```
$ pip install pytest
```

Antes de criar o nosso primeiro exemplo, vamos organizar o código da aplicação na pasta `src` e os testes ficaram na pasta `tests`.

```
$ mkdir tests src
```

Para dizermos para o python que essas pastas são módulos do nosso sistemas, vamos criar o arquivo `__init__.py` dentro de cada diretório. Esses arquivos não tem conteúdo.

```
$ touch tests\__init__.py
$ touch src\__init__.py
```

Agora estamos prontos para criar o primeiro programa na pasta `src`. 

```
def soma(x, y):
    return (x+y)


def produto(x, y):
    return x * y
```

Agora na `tests` vamos criar o nosso primeiro teste.

```
from src.exemplo1 import soma, produto
import pytest


def test_deve_retorna_a_soma():
    assert soma(10, 30) == 40
    assert soma(1, 2) == 3


def test_deve_retornar_a_soma_de_string():
    assert soma('a', 'b') == 'ab'


def test_deve_retornar_o_produto_de_dois():
    assert produto(2, 2) == 4
```

Agora que temos os testes criados, podemos executar para validar se estão passando.

```
$ pytest testes/test_soma.py
```

Também é possível executar utilizando o comando:

```
$ python -m pytest exemplo1.py
```

| Exit Code | Descrição |
|-----------|-----------|
| Exit code 0 | Todos os estão passando com sucesso |
| Exit code 1 | Algum teste esta falhando |
| Exit code 2 | A execução do teste foi interrompida pelo usuário |
| Exit code 3 | Ocorreu um erro interno ao executar testes |
| Exit code 4 | Erro na linha de comando do pytest |
| Exit code 5 | Nenhum teste encontrado |


O `pytest`pode executar inumeros testes e podemos organizar em arquivos/diretórios separados desde que siga os seguintes padrões:

* test_*.py
* *_test.py

Paramêtros do pytest:

| Paramêtros | Descrição |
|------------|-----------|
|pytest -q   | Executa o teste no modo silencioso|
|pytest -v   | Executa o teste no modo verboso|  
|pytest -k  "soma or string" | Executa os testes que contenha a palavra "soma"|  
|pytest -m 'numeros' | Executa que `mark` definido| 
|pytest -x   |  Interrompe o teste na primeira falha |
|pytest --maxfail=2|  Define o número de falhas suportadas|
|pytest -v -rsx | mostra o motivo do skip do teste|
|pytest -s | Mostra os `print` incluidos nos testes|


# Exemplo2

Vamos explorar um pouco mais do pytest no exemplo2. 

* pytest.mark.skip
* pytest.mark.parametrize

Vamos desenvolver uma `calculadora` e para isso vamos começar pelos testes.

Nesse exemplo queremos agrupar todos os testes da `calculadora` e para isso vamos utilizar uma  `class`.

No diretório `tests` vamos criar o arquivo `test_calculadora.py`:

```
from src.exemplo2 import Calculadora
import pytest


from src.exemplo2 import Calculadora, CalculadoraError
import pytest


class TestCalculadora:

    def test_deve_retornar_uma_soma(self):
        obj = Calculadora()
        assert obj.soma(10, 10) == 20


    @pytest.mark.skip
    def test_deve_retonar_uma_subtrair(self):
        obj = Calculadora()
        assert obj.subtrair(20, 10) == 10

    @pytest.mark.skip
    def test_deve_retonar_uma_dividir(self):
        obj = Calculadora()
        assert obj.dividir(10, 2) == 5

    @pytest.mark.skip
    def test_deve_retonar_uma_multiplicacao(self):
        obj = Calculadora()
        assert obj.multiplicar(2, 2) == 4
```

No diretório `src` vamos desenvolver a classe da `Calculadora`:

```
from numbers import Number
import sys

class Calculadora:
    def soma(self, n1, n2):
        return n1 + n2

    def subtrair(self, n1, n2):
        return n1 - n2

    def dividir(self, n1, n2):
        return n1 / n2

    def multiplicar(self, n1, n2):
        return n1 * n2

```

# Coverage

```
$ pip install coverage
```


```
$ coverage run --source=.  --omit=venv/* -m pytest
$ coverage report -m
```

# Mutante Test

```
$ pip install mutmut
```

```
$ mutmut run
```

```
$ mutmut results
```

```
$ mutmut show x
```


# Testando Recursos da AWS

Testando recursos AWS com o Moto

```
$ pip install moto
```

* S3
* SQS 
* dynamoDB



# Referência
1. [Pytest](https://docs.pytest.org/_/downloads/en/3.4.2/pdf/ )
2. [Moto](https://github.com/spulec/moto)
3. [MutMut](https://pypi.org/project/mutmut/)