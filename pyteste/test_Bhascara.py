
from calculo  import Mathik
import pytest
 
    
class Test_Bhaskara:

    @pytest.fixture
    def mat(self):
         return Mathik()
    
    # dados parametrizados
    testdata = [( 1, -2,  1, 1, 1, ''),
                ( 1, -5,  6, 2, 3,  2),
                (10, 10, 10, 0,'', ''),
                (10, 20, 10, 1, -1,'')
                 ]
                
    @pytest.mark.parametrize('a , b, c ,  nraiz, x1, x2 ', testdata)
    # teste de Bhaskara
    
    def testa_Bhaskara(self, mat, a, b , c , nraiz, x1, x2 ):
        if nraiz == 0:
            assert   mat.calcula_raiz(a, b, c) == (nraiz)      
        elif nraiz == 1:
             assert  mat.calcula_raiz(a, b, c) == (nraiz, x1)             
        elif nraiz == 2:
             assert  mat.calcula_raiz(a, b, c) == (nraiz, x1, x2)       
                      
     
##    def testa_uma_raiz(self, b):   # inserido b, recebe a fixture B
##           # codigo repetido b
##        assert b.calcula_raiz(1,-2,1) == (1, 1)
##
##    def testa_duas_raizes(self, b):
##        assert b.calcula_raiz(1,-5, 6) == (2, 3, 2)
##
##    def testa_zero_raizes(self, b):
##        assert b.calcula_raiz(10,10, 10) == (0)
##
##    def testa_raiz_negativa(self, b):
##        assert b.calcula_raiz(10,20, 10) == (1,-1)
###                

