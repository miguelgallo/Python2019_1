from vpython import *

# Para converter os dados de coordenadas polares para cartesianas
from math import sqrt, cos, sin, pi

# Vamos precisar da constante universal de gravitacao.
# Vamos usar a constante gravitacional heliocentrica.
GM =  0.000295912036265

# Importante para o tamanho da tela da animacao
# Se nao definir o tamanho da tela, poderah haver atuozoon
def afelio(E, L):
    delta = GM*GM  + 2*E*L*L
    return((-sqrt(delta) -GM)/(2*E))

# Precisamos definir as condicoes iniciais. 
# As distancias sao dadas em UA e o tempo em dias.
r = 1.0 
theta = -pi/2
v = 0.012
omega = 2*pi/365.25

# O momento angular eh uma constante de movimento
L = omega*r*r

# Podemos calcular tambem a energia mecanica total
# Se E > 0, entao a orbita serah aberta
# Se E < 0, a orbita serah fechada
Energia = 0.5*(v**2 + (L/r)**2) -GM/r

scene.y = 450
scene.x = 20

#scene.width = 1024
#scene.width = 760
#scene.center = (0,0,0)

f1 = gcurve(color = color.cyan)
f2 = gcurve(color = color.red)
f3 = gcurve(color = color.orange)
myWindow1 = graph(xtitle = "tempo (dias)", ytitle = "Energia")

scene.title = "Orbitas de planetas"
# Colocamos o Sol no posicao x =0,  y =0, e z = 0.
Sun = sphere(pos=vector(0,0,0), color = color.yellow, radius = 0.3, texture = None)
Earth = sphere(pos=vector(r*cos(theta), r*sin(theta), 0), color = color.black, radius = 0.1, make_trail = True)

# Definimos o passo de integracao.
dt = 0.01

# Por enquanto, o calculoeh para orbitas fechadas.
# Se a orbita eh fechada, entao pode-se calcular o afelio
# r_maxeh usado para determinar o tamanho maximo da tela
# Evitando assim o autozoon
if (Energia < 0):
    r_max = afelio(Energia, L)
    # Vamos garantir que o tamanho da tela contenha a orbita completa
    Earth.pos.x = r_max
    Earth.pos.x = -r_max
    Earth.pos.y = r_max
    Earth.pos.y = -r_max
else:
    print("Verifique os valores iniciais para condicionar o calculo para orbitas fechadas!")
    exit()

scene.autoscaling = False
Earth.color = color.blue
Earth.trail = curve(color = color.green)

# O fator 0.6 que multiplica o tamanho do vetor eh arbitrario
Force = arrow(pos = vector(Earth.pos), axis = vector(-0.6*Earth.pos/(r*r)), color = color.red)
vx = v*cos(theta)-omega*r*sin(theta)
vy = v*sin(theta) +  omega*r*cos(theta)
Velocidade = arrow(pos = vector(Earth.pos), axis = vector(50*vx,50*vy,0), color = color.white)
t = 0

while 1:
    rate(1000)
    a = (L**2)/(r**3) -GM/(r**2)
    v = v + a*dt
    r = r + v*dt
    omega = L/r**2
    theta = theta + omega*dt
    # As posicoes do planeta sao atualizadas em cada iteracao
    Earth.pos.x = r*cos(theta)
    Earth.pos.y = r*sin(theta)
    # O planeta deixa um rastro na animacao
    Earth.trail.append(pos=vector(Earth.pos))
    # A seguir as coordenadas do vetor Force
    Force.pos = vector(Earth.pos)
    vx = v*cos(theta) - omega*r*sin(theta)
    vy = v*sin(theta) +  omega*r*cos(theta)
    Velocidade.pos = vector(Earth.pos)
    Velocidade.axis = vector(50*vx,50*vy,0)
    Force.axis = vector(-0.6*Earth.pos/(r*r))
    #A seguir os graficos de energia sao atualizados
    t += dt
    K = 0.5*(v*v + r*r*omega*omega)
    U = Energia - K
    
f1.plot(pos = vector(t, K, 0), label = "Cinetica")
f2.plot(pos = vector(t, U, 0), label = "Potencial")
f3.plot(pos = vector(t, Energia, 0), label = "Total")


