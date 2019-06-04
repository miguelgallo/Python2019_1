import matplotlib.pyplot as plt 

d0 = 0
dfin = 5
v = 12
t = [i for i in range(0,30)] #intervalos de 1 minuto, 30 minutos
d = [d0+v/60 * ti for ti in t]

print(d)

plt.plot(t,d)
plt.show()

i = d.index(5)
print("O atleta percorreu {0} kilómetros em {1} minutos".format(d[i],t[i]))
