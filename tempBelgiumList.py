T = [-10, -8, 0, 1, 2, 5, -2, -4]
maiorTemp = T[0]
menorTemp = T[0]
soma = 0
for v in T:  
    if v > maiorTemp:
        maiorTemp = v
    else:
        menorTemp = v
    soma += v
print("Maior temperatura é: %d C" % maiorTemp)
print("Menor temperatura é: %d C" % menorTemp)
media = (soma / len(T))
print("Media é: ", media)
