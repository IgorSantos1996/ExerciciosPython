T = [-10, -8, 0, 1, 2, 5, -2, -4]
maximo = T[0]
minimo = T[0]
soma = 0
for x in T:
    if x < minimo:
        minimo = x
    if x > maximo:
        maximo = x
    soma = soma + x
print("Temperatura máxima: %d °C" % maximo)
print("Temperatura mínima: %d °C" % minimo)
print("Temparatuda média : %d ºC " % (soma/len(T)))