''' Classe matematica '''
import math

class Mathik:
    ''' Classe de funções matemáticas do usuário '''
    
    def fatorial(self, n):
        """[Calcula fatorial de n ou n!]
        Args:
            n ([int]): [um número n inteiro]
        Returns:
            [int]: [fat - Retorna o fatorial de n]
        """
        fat = 1
        if n > 1:
            for i in range(1,n+1):
                fat *= i 
        return fat

    def calcula_raiz( self, a, b, c):   # otimizado para testes
        ''' Calcula raizes polinôminio de segundo grau '''
        delta = b**2 - 4*a*c  
        if delta < 0:
                return 0 
                               
        elif delta == 0:
                x = -b/(2*a)           
                return 1, x

        elif delta>0:        
                raiz = math.sqrt(delta)
                x = (-b + raiz) /(2*a)
                y = (-b - raiz) /(2*a)
                return 2, x, y 

    def binomial(self, n ,k):
        ''' Calcula a combinação de n elementos k,k  '''
        nk = 1
        if n >= k:
            nk = self.fatorial(n)//(self.fatorial(k)*self.fatorial(n-k))
        else:
            nk = 'erro'
        return nk

    def mdc( self, a , b):
        ''' (int, int) -> int
            recebe dois inteiros diferentes de zero e retorna o maximo
            divisor comum entre a e b'''
        if b == 0: return a
        if a == 0: return b
        while a%b != 0:
            a, b = b, a%b
        return b


class Racional:

    def __init__(self, Mathik , n=0, d=1):
        div = Mathik.mdc(n, d) 
        self.put(n/div, d/div)
        
    def __str__(self):
        return "%d/%d"%(self.num, self.den)
    
    def get(self):
        return self.num, self.den
    	
    def put(self, n=0, d=1):
        self.num, self.den = n, d

    def __mul__(self, other):
            n = self.num * other.num
            d = self.den * other.den
            return Racional(n, d)
        
    def __truediv__(self, other):
            n = self.num * other.den
            d = self.den * other.num
            return Racional(n, d)    

    def __add__(self, other):
            n = self.num * other.den + other.num * self.den
            d = self.den * other.den
 
    def __sub__(self, other):
            n = self.num * other.den - other.num * self.den
            d = self.den * other.den
            return Racional(n, d)             

class Triangulo:
    ''' Classe Triângulo de lados a, b, c '''

    def __init__(self, a=1, b=1, c=1):
        self.a = a
        self.b = b
        self.c = c
        self.perimetro_ = self.perimetro()
        self.area_ = self.area()
        
    
    def get(self):   
        """ Obtém os lados do triângulo """
        return self.a, self.b, self.c
    	
    def put(self, a=1, b=1, c=1):  
        """ Carrega os lados do triângulo """
        self.a, self.b, self.c = a, b, c

    def perimetro(self):
        ''' Cálcula perímetro do triângulo 2p= a + b + c '''
        return self.a + self.b + self.c

    def area(self):
        ''' Cálcula área do triângulo tendo lados (a,b,c)- formula de Heron - '''
        p = self.perimetro() / 2
        return math.sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))
        
    def tipo_lado(self):
        ''' classifica o triangulo em escaleno, isósceles, equilátero '''
        if self.a == self.b and self.a == self.c:
            return 'equilátero'
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return 'isósceles'
        else:
            return 'escaleno'

    def retangulo(self):
        ''' Verifica se o triângulo é retângulo '''
        lista = [self.a, self.b, self.c]
        lista.sort()   # classifica em ordem crescente
        if lista[2]**2 == lista[1]**2 + lista[0]**2:
            return True
        else:
            return False

    def semelhantes(self, tri):
        ''' Compara triângulos e verifica se são semelhantes  '''
        lista1 = [self.a, self.b, self.c]
        lista2 = [tri.a, tri.b, tri.c]
        lista1.sort()
        lista2.sort()
        razao = lista2[0]/lista1[0]       
        if lista2[1] == razao * lista1[1] and lista2[2] == razao * lista1[2]:
            return True
        else:
            return False
   
class Ponto3D:

    def __init__(self, x=0, y=0, z=0):
        self.put(x, y, z)
    
    def __str__(self):
        return "%d ,%d, %d"%(self.x, self.y, self.z)
    
    def get(self):
        return self.x, self.y, self.z
    	
    def put(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z

    def distancia_origem(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def distancia_entre_pontos(self, outro):
        return math.sqrt((self.x-outro.x)**2 + (self.y-outro.y)**2 + (self.z-outro.z)**2)                         

    def ponto_medio(self, outro):
        return Ponto3D((self.x + outro.x)/2, (self.y + outro.y)/2, (self.z + outro.z)/2)
       
