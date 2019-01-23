primeira = []
segunda = []

# vamos iterar a primeira lista
while True:
    e = int(input("Informe o numero que quer add na primeira lista. (0) para sai"))
    if e == 0:
        break
    primeira.append(e)

# vamos iterar a segunda lista
while True:
    e = int(
        input("Informe o numero que quer add na segunda lista. (0) tecle 0 para sair")
    )
    if e == 0:
        break
    segunda.append(e)

terceira = primeira[:]  # Copia os elementos da primeira lista
terceira.extend(segunda) # extend para add elementos de uma lista na outra

while x < len(terceira):
    print("%d: %d " % (x, terceira))
    x += 1
