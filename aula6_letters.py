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
    n = int(arc_length) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r): 
    arc(t, r, 360)

# Movimentos básicos (lv 0).

def fd(t, length):
    t.fd(length)

def bk(t, length):
    t.bk(length)

def lt(t, angle=90):
    t.lt(angle)

def rt(t, angle=90):
    t.rt(angle)

def pd(t):
    t.pd()

def pu(t):
    t.pu()

# Combinações dos movimentos básicos (lv 1).

def fdlt(t, n, angle=90):
    """Para frente e esquerda"""
    fd(t, n)
    lt(t, angle)

def fdbk(t, n):
    """Para frente e para trás, voltando ao ponto inicial"""
    fd(t, n)
    bk(t, n)

def skip(t, n):
    """Levanta a caneta, move a tartaruga e desce a caneta"""
    pu(t)
    fd(t, n)
    pd(t)

def stump(t, n, angle=90):
    """Linha vertical e deixa a tartaruga virada para direita"""
    lt(t)
    fd(t, n)
    rt(t, angle)

def hollow(t, n):
    """Vira a tartaruga, levanta a caneta, move verticalmente, abaixa a caneta e deixa a tartaruga virada para direita"""
    lt(t)
    skip(t, n)
    rt(t)

# Combinações (lv 2). Lv 2 sempre voltam a tartaruga para a origem.

def post(t, n):
    """Faz linhas verticais"""
    lt(t)
    fdbk(t, n)
    rt(t)

def beam(t, n, height):
    """Faz linhas horizontais dada altura"""
    hollow(t, n*height)
    fdbk(t, n)
    hollow(t, -n*height)

def hangman(t, n, height):
    """Faz uma linha vertical para dada altura e faz  uma linha horizontal na dada altura"""
    stump(t, n * height)
    fdbk(t, n)
    lt(t)
    bk(t, n*height)
    rt(t)

def diagonal(t, x, y):
    """Faz uma linha diagonal dados x e y"""
    from math import atan2, sqrt, pi
    angle = atan2(y, x) * 180 / pi
    dist = sqrt(x**2 + y**2)
    lt(t, angle)
    fdbk(t, dist)
    rt(t, angle)

def vshape(t, n, height):
    diagonal(t, -n/2, height*n)
    diagonal(t, n/2, height*n)

def bump(t, n, height):
    """Faz linha vertical seguida de um semi-círculo com raio n na posição altura*n"""
    stump(t, n*height)
    arc(t, n/2.0, 180)
    lt(t)
    fdlt(t, n*height+n)

# Condição inicial: tartaruga começa no canto inferior esquerdo da letra.
# Condição final: tartaruga termina no canto inferior direito, virado na direção em que começou.
# As letras tem dois argumentos, a tartaruga e o tamanho.

def draw_a(t, n):
    diagonal(t, n/2, 2*n)
    beam(t, n, 1)
    skip(t, n)
    diagonal(t, -n/2, 2*n)

def draw_b(t, n):
    bump(t, n, 1)
    bump(t, n, 0)
    skip(t, n/2)

def draw_c(t, n):
    hangman(t, n, 2)
    fd(t, n)

def draw_d(t, n):
    bump(t, 2*n, 0)
    skip(t, n)

def draw_ef(t, n):
    hangman(t, n, 2)
    hangman(t, n, 1)

def draw_e(t, n):
    draw_ef(t, n)
    fd(t, n)

def draw_f(t, n):
    draw_ef(t, n)
    skip(t, n)

def draw_g(t, n):
    hangman(t, n, 2)
    fd(t, n/2)
    beam(t, n/2, 2)
    fd(t, n/2)
    post(t, n)

def draw_h(t, n):
    post(t, 2*n)
    hangman(t, n, 1)
    skip(t, n)
    post(t, 2*n)

def draw_i(t, n):
    beam(t, n, 2)
    fd(t, n/2)
    post(t, 2*n)
    fd(t, n/2)

def draw_j(t, n):
    beam(t, n, 2)
    arc(t, n/2, 90)
    fd(t, 3*n/2)
    skip(t, -2*n)
    rt(t)
    skip(t, n/2)

def draw_k(t, n):
    post(t, 2*n)
    stump(t, n, 180)
    vshape(t, 2*n, 0.5)
    fdlt(t, n)
    skip(t, n)

def draw_l(t, n):
    post(t, 2*n)
    fd(t, n)

def draw_n(t, n):
    post(t, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)
    post(t, 2*n)

def draw_m(t, n):
    post(t, 2*n)
    draw_v(t, n)
    post(t, 2*n)

def draw_o(t, n):
    skip(t, n)
    circle(t, n)
    skip(t, n)

def draw_p(t, n):
    bump(t, n, 1)
    skip(t, n/2)

def draw_q(t, n):
    draw_o(t, n)
    diagonal(t, -n/2, n)

def draw_r(t, n):
    draw_p(t, n)
    diagonal(t, -n/2, n)

def draw_s(t, n):
    fd(t, n/2)
    arc(t, n/2, 180)
    fd(t, n/2)
    rt(t)
    rt(t)
    t.circle(n/2, -180, 10)
    bk(t, n/2)
    pu(t)
    bk(t, n/2)
    lt(t)
    fd(t, n)
    fd(t, n)
    pd(t)
    lt(t)

def draw_t(t, n):
    beam(t, n, 2)
    skip(t, n/2)
    post(t, 2*n)
    skip(t, n/2)

def draw_u(t, n):
    post(t, 2*n)
    fd(t, n)
    post(t, 2*n)

def draw_v(t, n):
    skip(t, n/2)
    vshape(t, n, 2)
    skip(t, n/2)

def draw_w(t, n):
    draw_v(t, n)
    draw_v(t, n)

def draw_x(t, n):
    diagonal(t, n, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)

def draw_v(t, n):
    skip(t, n/2)
    diagonal(t, -n/2, 2*n)
    diagonal(t, n/2, 2*n)
    skip(t, n/2)

def draw_y(t, n):
    skip(t, n/2)
    stump(t, n)
    vshape(t, n, 1)
    rt(t)
    fdlt(t, n)
    skip(t, n/2)

def draw_z(t, n):
    beam(t, n, 2)
    diagonal(t, n, 2*n)
    fd(t, n)

def draw_(t, n):
    # draw a space
    skip(t, n)

def draw_virgula(t, n):
    arc(t, n/4, 90)
    skip(t, -n/4)
    rt(t)
    skip(t, n)
     
size = 15
bob = turtle.Turtle()
bob.pu()
bob.bk(300)
bob.pd()

for f in [draw_b, draw_o, draw_a, draw_ ,draw_t, draw_a, draw_r, draw_d, draw_e, draw_virgula, draw_p, draw_e, draw_s, draw_s, draw_o, draw_a, draw_l]:
    f(bob, size)
    skip(bob, size)

turtle.mainloop()
