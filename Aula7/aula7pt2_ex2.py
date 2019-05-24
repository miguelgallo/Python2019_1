import math

def check_fermat(a, b, c, n):
    ''' Esta função checa o último teorema de Fermat.
    Não existem números inteiros a, b e c tais que
    a^n + b^n = c^n
    para quaisquer valores de n maiores que 2.  
    '''
    left_side = pow(a, n) + pow(b, n)
    right_side = pow(c, n)
    if (n > 2) and (left_side == right_side):
        print("Holy Smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def write_numbers():
    ''' Esta função pede ao usuário para digitar valores a, b, c e n e usar check_fermat para verificar se violam o teorema de Fermat. 
    '''
    print("Valor de a: ")
    a = eval(input('a: '))
    print("Valor de b: ")
    b = eval(input('b: '))
    print("Valor de c: ")
    c = eval(input('c: '))
    print("Valor de n: ")
    n = eval(input('n: '))
    check_fermat(a, b, c, n)

write_numbers()
