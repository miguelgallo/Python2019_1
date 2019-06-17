import math
import matplotlib.pyplot as plt

S0 = math.exp(0)-math.exp(-10)

n = 10 #Número de trapézios

x=range(0, 10)
y=[math.exp(-xi) for xi in x] # isto se chama "list comprehension"

plt.bar(x,y,color="red",align="edge",width=1)
x1=[i for i in range(1,n)]
y1=[math.exp(-xi) for xi in x1]

for xi in x1:
	soma = 2*math.exp(-xi)

S1 = 1 + soma + math.exp(-(n+1))

plt.plot(x1,y1)
plt.show()

print('Resultado numérico (100 trapézios) =', S1)
print("Resultado analítico = ", S0)

precisao = (abs(S1 - S0) / S0) * 100
print("A precisão é de {0}%".format(precisao))
