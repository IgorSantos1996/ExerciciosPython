numero = int(input("Informe um numero inteiro: "))
x = 1
l = []
multiplicador = 0
while x <= numero:
    produto = 3 * multiplicador
    multiplicador += 1
    x += 1
    l.append(multiplicador)
print(multiplicador)
