def contador_letras(x):
    d = {}
    for i in x:
        d[i] = d.get(i,0)+1
    return d

s = "eu gosto de batata"
for e in sorted(contador_letras("eu gosto de batata").items()):
    print(e[0], e[1])
