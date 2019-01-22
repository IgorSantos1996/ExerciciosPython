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
