print('Este código calcula os zeros da função y = 3 *x^2 - 4 *x -10')

a = 3
b = -4
c = -10
delta = (b ** 2) - 4 * a * c
x_1 = (-b + ((delta)**(1/2)))/(2*a)
x_2 = (-b - ((delta)**(1/2)))/(2*a)

print('Os zeros da função ocorrem com os seguintes valores: x_1 = ', "%.3f" % x_1 , ' e x_2 = ' , "%.3f" % x_2)
