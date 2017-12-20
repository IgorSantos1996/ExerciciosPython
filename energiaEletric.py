# Escreva um programa que calcule o preço a pagar peloo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.
# Calcule o preço a pagar de acordo com a tabela a seguir.
qtdkWhConsumida = float(input("Informe a qtd de kWh consumida:"))
tipoInstalacao = input("Informe o tipo de instalação: ")
if tipoInstalacao == "R":
    if qtdkWhConsumida <= 500:
        qtdkWhConsumida = qtdkWhConsumida * 0.40
    else:
        qtdkWhConsumida = qtdkWhConsumida * 0.65
elif tipoInstalacao == "C":
    if qtdkWhConsumida <= 1000:
        qtdkWhConsumida = qtdkWhConsumida * 0.55
    else:
        qtdkWhConsumida = qtdkWhConsumida * 0.60
elif tipoInstalacao == "I":
    if qtdkWhConsumida <= 5000:
        qtdkWhConsumida *= 0.55
    else:
        qtdkWhConsumida *= 0.60
print("O tipo de instalaçao é %s e o valor a pagar é de %4.2f reais " % (tipoInstalacao, qtdkWhConsumida))
