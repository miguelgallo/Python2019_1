def div_21(n):
    """ Encontra o primeiro numero divisivel por 21 entre 101 e n escolhido pelo usuario
    """
    for value in range(101, n):
        if value % 21 != 0:
            print("Numero nao divisivel por 21: ", value)
        else:
            print("Numero divisivel por 21: ", value)
            return
        
n = eval(input('Digite um numero maior que 101: '))
div_21(n)
