notas = [0, 0, 0, 0, 0, 0, 0]  # lista de notas com cinco elementos, todos zero
soma = 0
x = 0
while x < 7:
    # ler notas e armazená-las na lista de notas
    notas[x] = float(input("Nota %d: " % x))
    soma = notas[x]  # acumulador para as notas
    x = x + 1  # contador para o indice
x = 0
while x < 7:
    print("Nota %d: %6.2f " % (x, notas[x]))
    x = x + 1
print("Média: %5.2f " % (soma/x))
