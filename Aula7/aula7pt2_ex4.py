def recurse(n, s):
    ''' Função recursiva para pegar e printar o valor de s.
    n é um inteiro positivo e s é um inteiro.
    '''
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0) #Saída é 6 (3+2+1=6)

#Resposta da questão 1: recurse(-1,0) vai gerar uma recursividade infinita, pois n == 0 nunca será um resultado. 
#Logo, o loop sempre irá para o else, diminuindo o valor de n em passos de 1.
