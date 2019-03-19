ultimo = 0
fila1 = []
fila2 =[]
while True:
    print("Existem %d elementos na fila1  e %d na fila2. " % (len(fila1), len(fila2)))
    print("Fila atual: ", fila1)
    print("Fila atual: ", fila2)
    print("\nDigite F para add um cliente ao fim da fila1 (ou G para a fila2) .")
    print("\nou A para realizar o atendimento a fila 1 (ou B para fila 2).")
    print("\n(S) Para encerrar.")
    op = input("Informe sua opção: (F, G, A, B ou S): ")
    x = 0
    sair = False
    while x < len(op):
        if op[x] == "A" or op[x] == "F":
            fila  = fila1
        else:
            fila = fila2
        if op[x] == "A" or op[x] == "B":
            if (len(fila)) > 0:
                atendido = fila.pop(0)  # remove da frente, ou seja da primeira posição
                print("Cliente %d atendido. " % atendido)
            else:
                print("Fila vazia! ninguem para entender")
        elif op[x] == "F" or op[x] == "G":
            ultimo += 1
            fila.append(ultimo)
        elif op[x] == "S":
            sair = True
            break
        else:
            print("Operação inválida: %s na posicao %d! Digite apenas F, A ou S!" % (op[x], x))
        x = x + 1
    if sair:
        break