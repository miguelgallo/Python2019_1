import math

class Ponto:
    """ Cria um novo Ponto, com coordenadas x, y """

    def __init__(self, x=0, y=0):
        """ Inicializa em x, y o novo ponto criado pela classe """
        self.x = x
        self.y = y
        
    def distancia_da_origem(self):
        """ Calcula minha distânica da origem """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def distancia_dois_pontos(self, alvo):
        """ Calcula a distancia entre dois pontos """
        return (((self.x - alvo.x) ** 2) + ((self.y - alvo.y) ** 2)) ** 0.5
    
    def ponto_medio(self, alvo):
        """ Retorna o ponto medio entre esse ponto e o alvo """
        mx = (self.x + alvo.x)/2
        my = (self.y + alvo.y)/2
        return Ponto(mx, my)
    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

p = Ponto(3, 4)
q = Ponto(5, 12)
print("distancia entre p e q: ", p.distancia_dois_pontos(q)) 
