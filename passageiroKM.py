# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até de 200 km, e R$ 0,45 para viagens mais longas.
km = float(input("Qual distancia em km deseja percorrer: "))
if km < 200:
    km = km * 0.50

if km > 200:
    km *= 0.45

print("O preço da viagem é de : {} reais""".format(km))
