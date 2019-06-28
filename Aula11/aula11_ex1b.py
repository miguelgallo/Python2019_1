# Cria um dicionário com linha e coluna indexadas pelas chaves (r, c)

class matriz5x5:

    def __init__(self, mat):
        self.mat = mat
        # dictionary comprehension
        self.dic = {(rx, cx): c for rx, r in enumerate(self.mat)\
                for cx, c in enumerate(r)}
        
    def  __str__(self):
        x = int(input('Insira a linha desejada (0 a 4): '))
        y = int(input('Insira a coluna deseja (0 a 4): '))
        return "({0}, {1}): {2}".format(x, y, self.dic.get((x,y)))

a = [
[0, 0, 0, 1, 0],
[0, 0, 0, 0, 0],
[0, 2, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 3, 0]
]
matriz = matriz5x5(a)
print(matriz)
