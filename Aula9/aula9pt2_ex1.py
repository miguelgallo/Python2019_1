d = {}
with open("dados_alunos.txt") as f:
    for line in f:
       (key, val1, val2) = line.split()
       d[int(key)] = val

print(d)

