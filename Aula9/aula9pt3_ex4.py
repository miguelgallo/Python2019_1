import numpy as np

eta = np.matrix([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
print('Matriz eta: \n', eta)
print('Elemento da linha 3 e coluna 3 da matriz eta: ', eta.item(10))
print('Transposta da matrix eta: \n', eta.transpose())

gamma = np.matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print('Matriz gamma: \n', gamma)
print('Transposta da matrix gamma: \n', gamma.transpose())
