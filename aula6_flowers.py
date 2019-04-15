import turtle
import math

def polyline(t, n, length, angle):
    """Desenha n segmentos de linha"""
    for i in range(n):
        t.fd(length)
        t.lt(angle)
 
def polygon(t, n, length):
    """Desenha um polígono com n lados"""
    angle = 360/n
    polyline(t, n, length, angle)
 
def arc(t, r, angle):
    """Desenha um arco com dado raio e ângulo"""
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
 
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def petal(t, r, angle):
    """Desenha uma pétala com dois arcos"""
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle):
    """Desenha uma flor com n pétalas"""
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)

jn = turtle.Screen()                 # Configurar a janela e seus atributos
jn.bgcolor("lightblue")              # Selecionar cor de fundo
jn.title("Bob")                      # Definir título

bob = turtle.Turtle()                # Criar Bob
bob.shape("turtle")                  # Selecionar formato         
bob.color("black")                   # Selecionar cor
bob.pensize(5)                       # Selecionar largura       
bob.speed("fastest")                 # Selecionar velocidade

flower(bob, 20, 200, 20)

jn.exitonclick()
