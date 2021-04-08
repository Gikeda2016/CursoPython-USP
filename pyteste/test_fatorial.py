
import pytest

def fatorial(n):
    """[Fatorial de n ou n!]
    Args:
        n ([int]): [número inteiro qualquer]
    Returns:
        [int]: [retorna n!]
    """
    if n < 1:
        return 1
    else:
        return n * fatorial(n-1)
 
data = [
    (0, 1),
    (1, 1),
    (-10, 1),
    (4, 24),
    (5, 120),
    (2, 2)
    ]


@pytest.mark.parametrize('entrada, esperado', data)
                         
def test_fatorial(entrada, esperado):        # teste mais compacto
    assert fatorial(entrada) ==  esperado 


#  === 5 passed in 0.07s ==


##def test_fatorial4()         # foi substituido pelo 'parametrize'
##    assert fatorial(4) == 24
##
##def test_fatorial5()
##    assert fatorial(5) == 120
    

