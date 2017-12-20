km = float(input("informe a km percorrida pelo carro: "))
tempDay = int(input("informe a quantidade de dias que o carro foi alugado: "))
precoToPay = tempDay * 60 + 0.15 * km
print("O preco a pagar é de : %5.2f reais" % precoToPay )
