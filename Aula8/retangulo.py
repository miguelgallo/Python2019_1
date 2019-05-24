from ponto import Ponto

class Retangulo:
    """Representa um retangulo. 
    atributos: 
    - largura, do tipo float
    - altura, do tipo float 
    - canto, do tipo Ponto.
    """
    def __init__(self, altura, largura, canto = Ponto()):
        """ Inicializa com a, l e um ponto, o novo retângulo criado pela classe. """
        self.a = altura
        self.l = largura
        self.p = canto
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
