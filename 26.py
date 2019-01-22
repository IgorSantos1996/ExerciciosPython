<<<<<<< HEAD
while True:  
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplcicação")
    print("4 - Divisão")
    print("5 - Sair")
    op = int(input("Informe sua opção: "))
    if op == 5:
        break
    else:
        if op >= 1 and op < 5:
            n = int(input("Tabuada o qual numero: "))
            x = 1
            while x <= 10:
                if op == 1:
                    print("%d x %d = %d " % (n, x, n + x))
                elif op == 2:
                    print("%d x %d = %d " % (n, x, n - x))
                elif op == 3:
                    print("%d x %d = %d "% (n, x, n * x))
                elif op == 4:
                    print("%d x %d = %d "%(n, x, n / x))
                x = x + 1
        else:
            print("Opção inválida")
=======
# Faça um programa que exiba uma lista de opções (menu): adição, subtração, divisao, multiplicação e sair.
# Imprima a tabuada da operação escolhida. Repita até que a opção saida seja escolhida

while True:
    print(
        "1 - Adição\n"
        "2 - Subtração\n"
        "3 - Multiplicação\n"
        "4 - Divisão\n"
        "5 - Sair"
    )
    op = int(input("Informe sua opção: "))
    if op == 5:
        break
    elif op >= 1 and op < 5:
        numero = int(input("Informe o numero: "))
        x = 1
        while x <= 10:
            if op == 1:
                print("%d + %d = %d" % (numero, x, numero + x))
            elif op == 2:
                print("%d + %d = %d" % (numero, x, numero - x))
            elif op == 3:
                print("%d + %d = %d" % (numero, x, numero * x))
            elif op == 4:
                print("%d + %d = %d" % (numero, x, numero / x))
            x = x + 1
    else:
        print("opção inválida!")
>>>>>>> 6b56d86626e99067a61eade909707592b1a7181d
