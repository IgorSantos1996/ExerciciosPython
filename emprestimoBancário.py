# Escreva um programa para aprovar o emprestimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação mesal não pode ser superior a 30% do salário.
# Calcule o  valor da prestação como sendo a valor da casa a comprar dividido pelo número de meses a pagar
valorHouse = float(input("Informe o valor da casa: "))
salario = float(input("Informe o salário: "))
qtdAnosaaPagar = int(input("Quantidade de anos a pagar: "))
minSalario = (salario /100) * 30
print("30% do salario é {}".format(minSalario))
prestacao = valorHouse / (qtdAnosaaPagar * 12)
if prestacao < salario:
    print("Sua prestação é :%6.2f reais" % prestacao)
else:
    print("O valor da prestação não pode ser superior a 30% do salário.")
