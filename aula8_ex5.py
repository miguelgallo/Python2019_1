class Rectangle:
    """Representa um retangulo. 

    atributos: 
    - largura, do tipo float
    - altura, do tipo float 
    - canto, do tipo Ponto.
    """
    def __init__(self, altura, largura):
        """ Inicializa com a, l o novo retângulo criado pela classe. """
        self.a = altura
        self.l = largura
    def perim(self):
        """ Calcula o perímetro do retângulo. """
        return (2 * self.a) + (2 * self.l)
    def area(self):
        """ Calcula a área do retângulo.  """
        return self.a * self.l
    def isSquare(self):
        """ Discrimina retângulos de quadrados.  """
        return (self.a == self.l)

r = Rectangle(10,5)
print(r.perim())    #output: 30
print(r.area())     #output: 50
print(r.isSquare()) #output: False

p = Rectangle(5,5)  
print(p.isSquare()) #output: True
