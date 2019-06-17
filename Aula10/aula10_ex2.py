import math
import matplotlib.pyplot as plt

S0 = math.exp(0)-math.exp(-10)

#Esquerda

x=range(0, 10)
y=[math.exp(-xi) for xi in x]  # isto se chama "list comprehension"

plt.bar(x,y,color="red",align="edge",width=1)
x1=[i/100 for i in range(0,1000)]
y1=[math.exp(-xi) for xi in x1]

S1= 0
for xi in x1:
    S1 = S1+ math.exp(-xi) * 0.01
print("Soma de 1000 caixinhas = ",S1)

print("Resultado analítico = ",S0)

precisao = (abs(S1-S0) / S0) * 100

print('A precisão do alinhamento à esquerda é de', precisao)

plt.plot(x1,y1)
plt.show()

#Direita

x=range(1, 11)
y=[math.exp(-xi) for xi in x]  # isto se chama "list comprehension"

plt.bar(x,y,color="red",align="edge",width=1)
x1=[i/100 for i in range(1,1001)]
y1=[math.exp(-xi) for xi in x1]

S1= 0
for xi in x1:
    S1 = S1+ math.exp(-xi) * 0.01
print("Soma de 1000 caixinhas = ",S1)

print("Resultado analítico = ",S0)

precisao = (abs(S1-S0) / S0) * 100

print('A precisão do alinhamento à direita é de', precisao)

plt.plot(x1,y1)
plt.show()
