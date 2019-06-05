import matplotlib.pyplot as plt 

d0 = 5    #distancia inicial
dac = 5.2   #distancia percorrida com aceleração
dfin = 7  #distancia final
v0 = 12   #velocidade inicial
v1 = 15   #velocidade após acelerar 
a = 202.5 #acelaração

tac = [i for i in range(0,2)]  #intervalos de 1 minuto (onde ocorre a aceleração)
dac = [d0 + (v0/60)*ti + (((a/3600)*(ti**2))/2) for ti in tac]
t2 = [i for i in range(2,8)]  #intervalos de 1 minutos, entre 1 a 7min (onde não tem mais acelaração)
d2 = [dac[1] + (v1/60)*tin for tin in t2]
t = tac + t2
d = dac + d2

print(tac)
print(dac)
print(t2)
print(d2)
print(t)
print(d)
print(len(t))
print(len(d))

plt.plot(t,d)
plt.xlabel("tempo(min)")
plt.ylabel("distancia(km)")
plt.show()

