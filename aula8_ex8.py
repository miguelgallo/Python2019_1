from circulo import *
import turtle

def desenhar_circulo(t, crc):
    t.pu()
    t.setx(crc.p.x)     #Define ponto x do centro
    t.sety(crc.p.y)     #Define ponto y do centro
    t.fd(crc.r)         
    print(t.position())
    t.lt(90)
    t.pd()
    t.circle(crc.r)

jn = turtle.Screen()                 # Configurar a janela e seus atributos
jn.bgcolor("white")                  # Selecionar cor de fundo
jn.title("Bob")                      # Definir título

bob = turtle.Turtle()                # Criar Bob
bob.shape("turtle")                  # Selecionar formato                       
bob.pensize(5)                       # Selecionar largura       
bob.speed("fastest")                 # Selecionar velocidade

p = Ponto(150,20)

crc = Circulo(75, p)

desenhar_circulo(bob, crc)

turtle.mainloop()
    
