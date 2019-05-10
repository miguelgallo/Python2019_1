from retangulo import *
import turtle

def desenhar_ret(t, ret):
    t.pu()               #Levanta a caneta
    t.goto(ret.p.x, ret.p.y)           #Seleciona posição da tartaruga
    print(t.position())  #Printa a posição escolhida

    t.seth(0)            
    t.pd()               
    t.fd(ret.l)
    print(t.position())

    t.seth(90)
    t.fd(ret.a)
    print(t.position())
    t.seth(180)
    t.fd(ret.l)
    print(t.position())
    t.seth(270)
    t.fd(ret.a)

jn = turtle.Screen()                 # Configurar a janela e seus atributos
jn.bgcolor("white")                  # Selecionar cor de fundo
jn.title("Bob")                      # Definir título

bob = turtle.Turtle()                # Criar Bob
bob.shape("turtle")                  # Selecionar formato                       
bob.pensize(5)                       # Selecionar largura       
bob.speed("fastest")                 # Selecionar velocidade

p = Ponto(50,50)

ret = Retangulo(100, 200, p)

desenhar_ret(bob, ret)

turtle.mainloop()
