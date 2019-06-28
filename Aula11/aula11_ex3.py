def contador_letras(x):
    x = "".join(x.strip(".").split()).lower()
    d = {}
    for i in x:
        d[i] = d.get(i,0)+1
    return d

for e in sorted(contador_letras("ThiS is String with Upper and lower case Letters").items()):
    print(e[0], e[1])
