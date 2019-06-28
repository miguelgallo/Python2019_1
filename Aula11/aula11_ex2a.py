def contador_letras(x):
    d = {}
    for i in x:
        d[i] = d.get(i,0)+1
    return d

s = "eu gosto de batata"
print(contador_letras(s))

