import turtle


def draw_spiral(t, n, length=3, a=0.1, b=0.0002):
    """Desenha uma espiral arquimediana começando na origem.

    Argumentos:
      n: quantidade de segmentos de linhas
      length: tamanho de cada segmento
      a: quão solta a espiral inicia (maior fica mais solto)
      b: quão frouxamente enrolada a espiral é (maior fica mais solto)

    """
    theta = 0.0

    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)

        t.lt(dtheta)
        theta += dtheta


# create the world and bob
bob = turtle.Turtle()
draw_spiral(bob, n=1000)

turtle.mainloop()
