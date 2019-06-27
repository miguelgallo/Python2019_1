# Cria um dicionário com linha e coluna indexadas pelas chaves (r, c)

from pprint import pprint # pprint printa o output de maneira mais legível 
# Cria um dicionário  5x5 de uma matrix 5x5
matriz5x5 = [
[0, 0, 0, 1, 0],
[0, 0, 0, 0, 0],
[0, 2, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 3, 0]
]
# dictionary comprehension
dic_rc5x5 = {(rx, cx): c for rx, r in enumerate(matriz5x5)\
                for cx, c in enumerate(r)}
pprint(matriz5x5, width=30)
print('-'*32)
# Mostra o dicionário da matriz
pprint(dic_rc5x5)
print('-'*30)
