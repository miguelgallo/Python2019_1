# Primeiro, precisamos carregar os módulos
from pylab import plot, show, ylim, xlim, xlabel, ylabel, grid, scatter, legend
# Para converter os dados de coordenadas polares para cartesianas, 
# vamos precisar das funções seno e cosseno
from math import cos, sin, pi

# Vamos precisar da constante universal de gravitação.
# Vamos usar a constante gravitacional heliocêntrica.
k = 0.01720209395
GM = k**2

# Precisamos definir as condições iniciais. 
# As distâncias são dadas em UA e o tempo em dias.
r = 1.0 
theta = - pi/2
v = 0.008
omega = 2*pi/365.25

# O momento angular é uma constante de movimento
L = omega*r*r

# Podemos calcular também a energia mecânica total
# Se E > 0, então a orbita será aberta
# Se E < 0, a orbita será fechada
Energia = 0.5*(v**2 + (L/r)**2) - GM/r

# Para os gráficos em coordenadas cartesianas (x,y),
# temos que preparar as listas x e y, 
# as quais são inicialmente vazias.
x = [ ]
y = [ ]

# Definimos o passo de integração. 
dt = 0.01

# Para órbitas fechadas, basta percorrer uma volta.
theta_inicial = theta
theta_final = theta_inicial + 2*pi

# Por enquanto, o cálculo é para órbitas fechadas.
if (Energia< 0):
    while(theta <theta_final):
        a = (L**2)/(r**3) - GM/(r**2)
        v = v + a*dt
        r = r + v*dt
        omega = L/r**2
        theta = theta + omega*dt
        # Transformamos (r, theta) para (x,y)
        # e preenchemos as listas x e y.
        x.append(r*cos(theta))
        y.append(r*sin(theta))

#Preparativos para o gráficos
lim_max = max([max(x), max(y)])
lim_max = 1.10*lim_max  # Para que a curva não toque a borda
lim_min = -1*lim_max    # Para que os eixos x e y tenham o mesmo tamanho
ylim(lim_min, lim_max)
xlim(lim_min, lim_max)
xlabel("x (UA)")
ylabel("y (UA)")
plot(x,y, label = "Energia B")

# Calculo analítico
x = []
y = []
theta = 0
A = 1.0
epsilon = 0.01

print("epsilon: ", epsilon)

if (Energia< 0):
    while (theta < 2*pi):
        r = A/(1 + epsilon*cos(theta))
        theta += 0.01
        x.append(r*cos(theta))
        y.append(r*sin(theta))

plot(x,y)

# Podemos repetir os cálculos acima, porém com outros parâmetros iniciais

# Condições iniciais (distâncias em UA e tempo em dias)
# Para preservar Veff, muda-se somente a velocidade radial inicial.
r = 1.0
theta = - pi/2
v = 0.0
omega = 2*pi/365.25

# Devemos cálcular L novamente se Veff for modificado. 
L = omega*r*r

# Calculamos a energia mecânica novamente.
Energia = 0.5*(v**2 + (L/r)**2) - GM/r

# Preparamos as listas inicialmente vazias para as coordenadas x e y. 
x = []
y = []

# Passo de integração 
dt = 0.01

# E repetimos o cálculo percorrendo a trajetória fechada
theta_inicial = theta
theta_final = theta_inicial + 2*pi
# Precisamos verificar se a órbita é fechada antes do loop. 
if (Energia< 0):
    while(theta <theta_final):
        a = (L**2)/(r**3) - GM/(r**2)
        v = v + a*dt
        r = r + v*dt
        omega = L/r**2
        theta = theta + omega*dt
        # A seguir, transfomamos os dados em coordenas cartesianas
        # e acrescentamos as novas posições em x e e y.
        x.append(r*cos(theta))
        y.append(r*sin(theta))


plot(x,y, label = "Energia A")

# Colocamos o Sol no posição x = 0 e y = 0.
scatter(0,0, s = 200, c = 'yellow', alpha = 0.8)

legend(loc = 2)
grid()
show()
