prato = 5
pilha = list(range(1, prato + 1))
while True:
    print("\nExistem %d pratos na pilha" % len(pilha))
    print("Pilha atual: ", pilha)
    print("Digite E para empilhar um novo prato, ")
    print("ou D para desempilhar. S para sair." )
    operacao = input("Operacao (E, D ou S):")
    if operacao == "D":
        if (len(pilha) > 0):
            lavado = pilha.pop(-1)
            print("Prato % lavado " % lavado)
        else:
            print("Pilha vazia! Nada para lavar...")
    elif operacao == "E":
        prato = prato + 1 # novo prato
        pilha.append(prato)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas E, D ou S!")

