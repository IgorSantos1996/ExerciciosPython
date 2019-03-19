l = [1, 2, 3, 4, 5, 6, 8, 9]
maximo = l[0]
menor = l[0]
for elemento in l:
    if elemento > maximo:
        maximo = elemento
    else:
        menor = elemento
print("Maior elemento é: ", maximo)
print("Menor elemento é:", menor)
