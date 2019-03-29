import math

print('Calculando o volume de uma esfera')

r = input('Insira o raio da esfera: ')
Volume = (4/3)*(math.pi)* float(r)**3

print('O volume é: ',"%.3f" % Volume)
