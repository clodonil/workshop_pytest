# Testando com Pytest

documentação para o workshop de PyTest

# Porque Testar

1. Códigos são escritos por seres humanos e seres humanos erram;

2. Programas contém erros (Bugs)
    - Sintaxe
    - Lógica

3. Bugs podem causar catástrofes;

4. Bugs podem causar desconforto;


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
# pip install pytest
```

Antes de criar o nosso primeiro exemplo, vamos organizar o código da aplicação na pasta `src` e os testes ficaram na pasta `tests`.

```
# mkdir tests src
```

Para dizermos para o python que essas pastas são módulos do nosso sistemas, vamos criar o arquivo `__init__.py` dentro de cada diretório. Esses arquivos não tem conteúdo.

```
# touch tests\__init__.py
# touch src\__init__.py
```

Agora estamos prontos para criar o primeiro programa na pasta `src`. 

```
def soma(x: float,y: float) -> float:
    return (x+y)
```

Agora na `tests` vamos criar o nosso primeiro teste.

```
from src.exemplo1 import soma

def test_deve_retorna_a_soma():
    assert soma(10,30) == 50
    assert soma(1,2) == 1

```

Agora que temos os testes criados, podemos executar para validar se estão passando.

```
# pytest exemplo1.py
```

Também é possível executar utilizando o comando:

```
# python -m pytest exemplo1.py
```

| Exit Code | Descrição |
|-----------|-----------|
| Exit code 0 | All tests were collected and passed successfully |
| Exit code 1 | Tests were collected and run but some of the tests failed |
| Exit code 2 | Test execution was interrupted by the user |
| Exit code 3 | Internal error happened while executing tests |
| Exit code 4 | pytest command line usage error |
| Exit code 5 | No tests were collected |


O `pytest`pode executar inumeros testes e podemos organizar em arquivos/diretórios separados desde que siga os seguintes padrões:

* test_*.py
* *_test.py

Vamos criar o diretório `tests` e colocar todos os testes nesse subdiretório.

exemplo2

exemplo3


Paramêtros:

pytest -x   # stop after first failure
pytest --maxfail=2# stop after two failures


# Testando recursos AWS com o Moto

# pip install moto

* S3
* 

# Coverage


# Mutante Test

# Referência
1. [Pytest](https://docs.pytest.org/_/downloads/en/3.4.2/pdf/ )
2. [Moto](https://github.com/spulec/moto)