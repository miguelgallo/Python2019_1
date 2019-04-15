import math
import turtle

def isosceles(t, d, angle):
    """Desenha um triângulo isosceles."""
    
    #d: tamanho dos lados iguais do triângulo.
    #angle: ângulo entre os dois lados iguais.

    y = d * math.sin(angle * math.pi / 180)

    t.right(angle)
    t.forward(d)
    t.left(90+angle)
    t.forward(2*y)
    t.left(90+angle)
    t.forward(d)
    t.left(180-angle)

def pie(t, n, r):
    """Desenha uma torta divida em segmentos radiais."""

    #n: número de segmentos.
    #r: tamanho do raio radial.
    
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        t.left(angle)    


bob = turtle.Turtle()

pie(bob, 5, 40)

turtle.mainloop()
