from ponto import Ponto

class Rectangle:
    """Representa um retangulo. 
    atributos: 
    - largura, do tipo float
    - altura, do tipo float 
    - canto, do tipo Ponto.
    """
    def __init__(self, altura, largura, pp = Ponto()):
        """ Inicializa com a, l e um ponto, o novo retângulo criado pela classe. """
        self.a = altura
        self.l = largura
        self.p = pp
    def perim(self):
        """ Calcula o perímetro do retângulo. """
        return (2 * self.a) + (2 * self.l)
    def area(self):
        """ Calcula a área do retângulo.  """
        return self.a * self.l
    def isSquare(self):
        """ Discrimina retângulos de quadrados.  """
        return (self.a == self.l)
    def whichPoint(self):
        """Printa o ponto de cada retângulo. """
        print(self.p)

a = Ponto(3,5)

r = Rectangle(10,5,a)
print(r.perim())    #output: 30
print(r.area())     #output: 50
print(r.isSquare()) #output: False
r.whichPoint()

b = Ponto(8,7)

p = Rectangle(5,5,b)  
print(p.isSquare()) #output: True
p.whichPoint()
