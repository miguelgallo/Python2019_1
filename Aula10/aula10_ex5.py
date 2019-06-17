import math

n = 10  # Número de trapézios
i = 0  # Limite inferior
f = 10  # Limite superior
h = (f - i) / n  # Largura dos trapézios

S0 = math.cosh(10)-math.cosh(0)
C0 = math.sinh(10)-math.sinh(0)

soma1 = 0
for c in range(1, 10):
	soma1 = soma1 + math.sinh(c*h)
S1 = h * (math.sinh(i) / 2 + soma1 + math.sinh(f) / 2)

soma2 = 0
for c in range(1, 11):
	soma2 = soma2 + math.sinh(c*h)
S2 = h * soma2

soma3 = 0
for c in range(1, 10):
	soma3 = soma3 + math.cosh(c*h)
C1 = h * (math.cosh(i) / 2 + soma3 + math.cosh(f) / 2)

soma4 = 0
for c in range(1, 11):
	soma4 = soma4 + math.cosh(c*h)
C2 = h * soma4

print("Integral de senh(x) de 0 a 2pi")
print("Resultado analítico = ", S0)
print('Soma de Riemann à direita (10 retângulos)')
print('Resultado numérico  =', S2)
print('Regra dos trapézios (10 trapézios)')
print('Resultado numérico  =', S1)
print('')
print("Integral de cosh(x) de 0 a 2pi")
print("Resultado analítico = ", C0)
print('Soma de Riemann à direita (10 retângulos)')
print('Resultado numérico  =', C2)
print('Regra dos trapézios (10 trapézios)')
print('Resultado numérico  =', C1)
