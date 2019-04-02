import turtle

jn = turtle.Screen()                 # Configurar a janela e seus atributos
jn.bgcolor("lightblue")              # Selecionar cor de fundo
jn.title("Teca & Joana")             # Definir título

bob = turtle.Turtle()                  # Criar Bob
bob.shape("turtle")                    # Selecionar formato         
bob.color("black")                     # Selecionar cor
bob.pensize(5)                         # Selecionar largura       
bob.speed("normal")                    # Selecionar velocidade


def square(t):
    for i in range(4):
        t.forward(50)                # Fazer Bob desenhar um quadrado
        t.left(90)


square(bob)
