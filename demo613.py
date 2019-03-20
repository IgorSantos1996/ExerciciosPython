v = list(range(0,1200))
p = []
i = []
for e in v:
    if e % 2 == 0:
        p.append(e)
    else:
        i.append(e)
print("Pares: " , p)
print("Impares: " , i)