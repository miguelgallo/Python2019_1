import matplotlib.pyplot as plt
import math 

def a(v0,v1,x0,x1): 
    """ aceleração usando Torricelli """
    return (0.5*(v1**2 - v0**2))/(x1 - x0)

x0 = 5     #distancia inicial
x1 = 5.2   #distancia percorrida com aceleração
xfin = 7   #distancia final
v0 = 12    #velocidade inicial
v1 = 15    #velocidade após acelerar
a = a(v0,v1,x0,x1)/3600
print(a)

t1 = [i for i in range(0,2)]  #intervalos de 1 minuto (onde ocorre a aceleração)
v=[]
v.append(12/60)
x=[]
x.append(5)
dt1 = t1[1]-t1[0]

t2 = [i for i in range(2,9)]
dt2 = t2[1] - t2[0]

for i in range(1,2):
    xi = x[i-1] + v[i-1]*dt1
    x.append(xi)
    vi = v[i-1] + a*dt1
    v.append(vi)

print(v)

for j in range(2,9):
    xj = x[j-1] + v[-1]*dt2
    x.append(xj)

t = t1 + t2

plt.plot(t,x)
plt.xlabel("tempo(min)")
plt.ylabel("distancia(km)")
plt.show()
