#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o preço a pagar

preco = float(input("Informe o preço da mercadoria: "))
print(" ")
desconto = float(input("Qual o percentual de desconto: "))
vdesconto = (preco*desconto)/100
paytotake = preco - vdesconto
print("O valor do desconto é de %3.2f reais e o preco a pagar é de : %5.2f reais " % (vdesconto,paytotake))