import matplotlib.pyplot as plt 

d0 = 0    #distancia inicial
dac = 2   #distancia percorrida com aceleração
dfin = 7  #distancia final
v0 = 12   #velocidade inicial
v1 = 15   #velocidade após acelerar 
a = 20.25 #acelaração

tac = [i for i in range(0,10)]  #intervalos de 1 minuto, 9 minutos (onde ocorre a aceleração)
dac = [d0+v0/60 * ti +(((a/3600) * ti**2)/2) for ti in tac]
d1 = dac[9]
t = tac + [i for i in range(10,30)]  #intervalos de 1 minuto, indo de 10 a 30 min (onde não há aceleração)
d = dac[0:8] + [d1+v1/60 * tin for tin in t]

print(d)

plt.plot(t,d)
plt.show()

#i = d.index(7.0278125)
#print("O atleta percorreu {0} kilómetros em {1} minutos".format(d[i],t[i]))
