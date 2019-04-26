def is_triangle(a,b,c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("Yes")
    else:
        print("No")

def write_numbers():
    print("Valor de a: ")
    a = eval(input('a: '))
    print("Valor de b: ")
    b = eval(input('b: '))
    print("Valor de c: ")
    c = eval(input('c: '))
    is_triangle(a, b, c)

write_numbers()
