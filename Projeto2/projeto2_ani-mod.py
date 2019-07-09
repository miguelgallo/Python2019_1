from vpython import *

# Para converter os dados de coordenadas polares para cartesianas
from math import sqrt, cos, sin, pi

# Estamos usando o sistema CGS de unidades.

# Vamos precisar da constante universal de gravitação.
k = 0.01720209395
# Vamos usar a constante gravitacional heliocêntrica.
GM = k**2

# Importante para o tamanho da tela da animação.
# Se não definir o tamanho da tela, poderá haver autozoom.
# Afélio - ponto mais distante em relação ao Sol. 
# Logo, setando o afélio para definir o tamanho da tela.
def afelio(E, L):
    delta = GM*GM  + 2*E*L*L
    return((-sqrt(delta) -GM)/(2*E))

# Precisamos definir as condições iniciais.
# As distâncias são dadas em unidades astronômicas e o tempo em dias.

# Distância do Sol a Terra (UA).
r = 1.0
# Ângulo de abertura (relacionado a Segunda lei de Kepler) (rad).
theta = - pi/2
# Velocidade de translação (rad*UA/dias).
v = 0.0
# Velocidade angular (rad/dias).
omega = 2*pi/365.25

# Variando valores de v, podemos distinguir todos os corpos celestes, podendo colocar m = 1.

# O momento angular é uma constante de movimento.
L = omega*r*r

# Podemos calcular também a energia mecânica total.
# Se E > 0, então a orbita será aberta;
# Se E < 0, a orbita será fechada.
Energia = 0.5*(v**2 + (L/r)**2) - GM/r

# Canvas onde ocorrerá a animação, onde setamos as posições iniciais de x e y.
scene.y = 450
scene.x = 20

# Define o título do canvas animado.
scene.title = "Orbitas de planetas"
# Colocamos o Sol no posicao x =0,  y =0, e z = 0.
Sun = sphere(pos=vector(0,0,0), color = color.yellow, radius = 0.3)
Earth = sphere(pos=vector(r*cos(theta), r*sin(theta), 0), color = color.black, radius = 0.1, make_trail = True)

# Definimos o passo de integração.
dt = 0.01

# Como a órbita é fechada, entao pode-se calcular o afélio.
# r_max é usado para determinar o tamanho máximo da tela.
if (Energia < 0):
    r_max = afelio(Energia, L)
    # Vamos garantir que o tamanho da tela contenha a órbita completa.
    Earth.pos.x = r_max
    Earth.pos.x = -r_max
    Earth.pos.y = r_max
    Earth.pos.y = -r_max
else:
    print("Verifique os valores iniciais para condicionar o calculo para orbitas fechadas!")
    exit()

# Para evitar que o autozoom ocorra, usamos autoscaling = False.
scene.autoscaling = False
Earth.color = color.blue
Earth.trail = curve(color = color.green)

# Força gravitacional - O fator 0.6 que multiplica o tamanho do vetor é arbitrário e o sinal negativo pois a força sempre aponta para o centro.
Force = arrow(pos = vector(Earth.pos), axis = vector(-0.6*Earth.pos/(r**2)), color = color.red)
# Velocidade tangente a trajetória.
vx = v*cos(theta) - omega*r*sin(theta)
vy = v*sin(theta) +  omega*r*cos(theta)
Velocidade = arrow(pos = vector(Earth.pos), axis = vector(50*vx,50*vy,0), color = color.white)
# Tempo inicial. 
t = 0

# while serve para que a animação continue rodando sem pausa.
while 1:
    rate(1000)
    a = (L**2)/(r**3) -GM/(r**2)
    v = v + a*dt
    r = r + v*dt
    omega = L/r**2
    theta = theta + omega*dt
    # As posições do planeta são atualizadas em cada iteração.
    Earth.pos.x = r*cos(theta)
    Earth.pos.y = r*sin(theta)
    # O planeta deixa um rastro na animação.
    Earth.trail.append(pos=vector(Earth.pos))
    # A seguir as coordenadas do vetor Force.
    Force.pos = vector(Earth.pos)
    vx = v*cos(theta) - omega*r*sin(theta)
    vy = v*sin(theta) +  omega*r*cos(theta)
    Velocidade.pos = vector(Earth.pos)
    Velocidade.axis = vector(50*vx,50*vy,0)
    Force.axis = vector(-0.6*Earth.pos/(r**2))
    #A seguir os graficos de energia sao atualizados
    #t += dt
    #K = 0.5*(v**2 + (r*omega)**2)
    #U = Energia - K
    
#f1.plot(pos = vector(t, K, 0))
#f2.plot(pos = vector(t, U, 0))
#f3.plot(pos = vector(t, Energia, 0))



