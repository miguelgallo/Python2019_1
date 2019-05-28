import numpy as np

eta = [[1, 0, 0, 0], 
        [0, -1, 0, 0], 
        [0, 0, -1, 0], 
        [0, 0, 0, -1]]

gamma = [[1, 2, 3, 4], 
        [5, 6, 7, 8], 
        [9, 10, 11, 12], 
        [13, 14, 15, 16]]

beta = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
bgamma = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for ir in range(4):
    for ic in range(4):
        beta[ic][ir] = eta[ir][ic]

for ir in range(4):
    for ic in range(4):
        bgamma[ic][ir] = gamma[ir][ic]

print(eta)
print(beta)
print(gamma)
print(bgamma)



