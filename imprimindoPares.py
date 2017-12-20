fim = int(input('(Mostra Impar) Digite um número: '))
x = 1
while x <= fim:
    if x % 3 == 0:
        print(x)
        x += 1
    x += 1
