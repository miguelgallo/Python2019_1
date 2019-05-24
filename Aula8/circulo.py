import math
from ponto import *

class Circulo:
    """Representa um círculo. 

    atributos: 
    - centro, do tipo Ponto
    - raio, do tipo float 
    """
    def __init__(self, raio, centro = Ponto()):
        """ Inicializa com r e um centro, o novo círculo criado pela classe. """
        self.r = raio
        self.p = centro
        
    def ponto_no_circulo(self, alvo):
        """ Diz se o ponto está inserido no círculo. """
        d = alvo.distancia_dois_pontos(self.p)
        return d <= self.r

