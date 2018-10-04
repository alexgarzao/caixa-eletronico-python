# Caixa eletrônico

Este é o clássico puzzle do [caixa eletrônico](http://dojopuzzles.com/problemas/exibe/caixa-eletronico/), resolvido em Python.

## Como executar o projeto

Os requisitos para instalar são:
* Python 3.5 (ou superior)
* Virtualenv

No exemplo abaixo será utilizado o python 3.7:

    git clone https://github.com/alexgarzao/caixa-eletronico-python.git
    cd caixa-eletronico-python
    virtualenv -p python3.7 .env
    source .env/bin/activate
    pip install -r requirements.txt

Para validar se os testes estão ok, execute o seguinte comando:

    nosetests .


Para executar a aplicação, execute o seguinte comando:

    python main.py 1250

No exemplo acima, 1250 seria o valor a ser sacado.
