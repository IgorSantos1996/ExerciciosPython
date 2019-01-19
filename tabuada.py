tabuada = 1
for tabuada in range(tabuada, 10, 1):
    numero = 1
    for numero in range(numero, 10, 1):
        print("%d x %d = %d" % (tabuada, numero, tabuada * numero))
        numero = numero + 1
    tabuada = tabuada + 1
