l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
p = int(input("Digite o valor a procurar:"))
v = int(input("Digite o segundo valor a procurar: "))
x = 0
achouP = False
achouV = False
primeiro = 0
while x < len(l):  # percorrer a lista
    if l[x] == p:  # se o numero que li é igual ao elemento da posição em questão
        achouP = True
        if not achouV:
            primeiro = 1
    if l[x] == v:
        achouP = True
        if not achouP:
            primeiro = 2
    x = x + 1
if achouP:
    print("p: %d encontrado" % p)
else:
    print("%d não encontrado." % p)
if achouV:
    print("v: %d encontrado" % v)
else:
    print("v: %d não encontrado" % v)
if primeiro == 1:
    print("p foi achado antes de v")
elif primeiro == 2:
    print("v foi achado antes de p")
