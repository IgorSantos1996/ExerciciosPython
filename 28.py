# Modifique o programa anterior de forma a ler um numero n.
# Imprima os n primeiros números primos.
while True:
    numero = int(input("Informe o número: "))
    if numero < 0:
        print("Inválido numero negativo")
    else:
        if numero >= 1:
            print("2")
            y = 3
            p = 1
            while p < numero:
                x = 3
                while x < y:
                    if y % x == 0:
                        break
                    x = x + 2
                if x == y:
                    print(x)
                    p = p + 1
                y = y + 2
