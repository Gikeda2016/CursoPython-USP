import pytest


def gera_vogais():
    """ Lista com vogais, incluindo os acentuados e maiúsculos """
    vogais1 =['a','á','à','ã', 'â', 'e','é','ê', 'í','i','o','õ','ô','u','ú']
    vogais = vogais1 + [vogal.upper() for vogal in vogais1]
    return vogais

def e_vogal(x):
    vogais = gera_vogais()

    return  True if x in vogais else False    # True for x vogal


def le_data():
    data =[]
    with open('vogal.txt', 'r', encoding='utf-8') as arq:
        for linha in arq:
                if "x" not in linha:
                    data.append(eval(linha))
    return data


data1 = le_data()
# for item in data1:
#     print(item)

@pytest.mark.parametrize('entrada, esperado', data1)

def test_vogal(entrada, esperado):
    print(entrada,': ', esperado)
    assert e_vogal(entrada) == esperado

