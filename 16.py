n = 1
soma = 0

while n <= 10:
    x = int(input("Digite o %d número: " % n))
    soma = soma + x  # acumulador
    n = n + 1  # contador
print("Soma: %d" % soma)

