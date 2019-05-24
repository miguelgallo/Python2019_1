import math

def velocidade_media(d_f,d_i,t):
    v_m = "%.2f" % ((d_f - d_i)/ t)
    print(v_m)

def velocidade_objeto(a,t):
    v_obj = "%.2f" % ((a * t))
    print(v_obj)

def velocidade_queda(h):
    g = 9.8
    v_queda = "%.2f" % (math.sqrt(2*g*h))
    print(v_queda)

d_i = float(input('Insira a posição inicial: '))
d_f = float(input('Insira a posição final: '))
t = float(input('Insira o tempo: '))
a = float(input('Insira a aceleração do objeto: '))
h = float(input('Insira a altura de queda: '))

print("Velocidade média do objeto")
velocidade_media(d_f,d_i,t)

print("Velocidade do objeto no tempo ", t)
velocidade_objeto(a,t)

print("Um objeto que cai de uma altura ", h, " chega ao solo com uma velocidade de ", )
velocidade_queda(h)
