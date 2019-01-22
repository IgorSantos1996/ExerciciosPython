first = []
second = []

while True:
    x = int(input("Digite um valor para a primeira lista (0) para sair: "))
    if x == 0:
        break
    first.append(x)  # insere o numero no final da lista que foi lido
while True:
    x = int(input("Digite um valor para a segunda lista (0) para sair: "))
    if x == 0:
        break
    second.append(x)
    third = first[:]  # copia os elementos da primeira lista
    third.extend(second)
x = 0
while x < len(third):
    print("%d: %d " % (x, third[x]))
    x += 1
