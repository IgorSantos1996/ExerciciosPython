notas = [6, 7, 5, 8, 9] # criação das listas
soma = 0 #
x = 0
while x < len(notas): # continua até quando x for menor que 5.
    soma = soma + notas[x]
    x = x + 1
print("Media: %5.2f" % (soma/x))
