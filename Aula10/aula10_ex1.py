import math
import matplotlib.pyplot as plt
math.exp(0)-math.exp(-10)

x=range(0,10)
y=[math.exp(-xi) for xi in x]  # isto se chama "list comprehension"
print(x)
print(y)

plt.bar(x,y,color="red",align="edge",width=1)
x1=[i/100 for i in range(0,1000)]
y1=[math.exp(-xi) for xi in x1]
plt.plot(x1,y1)
#plt.show()

S1= 0
dx = 0.01
I_a = 0.9999546000702375

S1 = (0.01*I_a) + I_a 
print(S1)

S1 = 0
j = 0

for xi in x1:
    if S1 != 1.0099541460709398:
        S1 = S1+ math.exp(-xi) * j
    else:
        continue
    j = j+1
print("Soma 1000 caixinhas = ",S1)
