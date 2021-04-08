
from calculo import Triangulo
import pytest

class Testa_triangulo:
    @pytest.fixture
    def tri(self):
         return Triangulo()  # inicializa a classe Triângulo
        
    # dados parametrizados (lados, tipo, retangulo, perímetro, área)
    testdata = [( 3, 4,  5, 'escaleno',   True,  12,    6), 
                ( 6, 8, 10, 'escaleno',   True,  24,   24),
                ( 5,12, 13, 'escaleno',   True,  30,   30),
                ( 7,24, 25, 'escaleno',   True,  56,   84),
                (14,48, 50, 'escaleno',   True, 112,  336.0),
                ( 7, 9,  7, 'isósceles', False,  23,   24.128),
                ( 5, 4,  4, 'isósceles', False,  13,    7.806),
                ( 5, 5,  5, 'equilátero',False,  15,   10.825),
                ( 7, 7,  7, 'equilátero',False,  21,   21.217),
                (13,13, 13, 'equilátero',False,  39,   73.179)
                  ]
    
    @pytest.mark.parametrize('a, b, c, tipo, retan, perim, area', testdata )        

    # teste de triângulo
    def test_triangulo1(self, tri, a, b, c, tipo, retan, perim, area):
        tri.put(a,b,c)  # carrega lados do triangulo - com o método put   
           
        assert tri.tipo_lado() == (tipo) and  tri.retangulo() == (retan)\
          and tri.perimetro() == (perim) and abs(tri.area() - (area)) <= 0.01 # usar parentesis no resultado

##    '''
##    platform win32 -- Python 3.9.0, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
##    rootdir: C:\Users\55119\python
##    collected 10 items
##
##    tes_triangulo.py ..........   27/11/2020                                                                                                                                                                                                        [100%]
##
##    ============================================================================================================ 10 passed in 0.08s ============================================================================================================
##    '''
# PS C:\Users\55119\Plataforma\Python\curso_py> pytest test_triangulo.py
# ============================================= test session starts ==============================================
# platform win32 -- Python 3.8.6, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
# rootdir: C:\Users\55119\Plataforma\Python\curso_py
# collected 10 items

# test_triangulo.py .........25/01/2021.   
