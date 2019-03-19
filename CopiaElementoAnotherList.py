v = list(range(1, 8, 1))
P = []
I = []
for elemento in v:
    if elemento % 2 == 0:
        P.append(elemento)
    else:
        I.append(elemento)
print("Pares: ", P)
print("Impares: ", I)
