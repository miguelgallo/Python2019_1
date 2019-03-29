def test_range(n):
    if n in range(0,99):
        print( " %s está no intervalo "%str(n))
    else :
        print("O número está fora do intervalo")

n = eval(input('Adicione o número a ser testado: '))

test_range(n)
