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

    def reflexao_x(self):
        """ Retorna o reflexo do ponto no eixo x """
        refx = self.x
        refy = -self.y
        return Ponto(refx, refy)

    def inclinacao_origem(self):
        """ Calcula a inclinação entre um ponto e a origem """
        return (self.y)/(self.x)
    
    def a(self, alvo):
        """ Calcula a inclinação entre um ponto e a origem """
        return (self.y - alvo.y)/(self.x - alvo.x)

    def b(self, alvo):
        return self.y - self.a(alvo)*self.x

    def parametros_reta(self, alvo):
        a = self.a(alvo)
        b = self.b(alvo)
        return (a, b)

print(Ponto(4,11).parametros_reta(Ponto(6,15)))
        

    
