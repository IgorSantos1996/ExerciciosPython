valor_casa = float(input("Informe o valor da casa: "))
salario = float(input("Informe o salario: "))
qtd_anos = int(input("Informe a quantidade de anos a pagar: "))

meses = qtd_anos * 12  # meses
salario = salario * 30 / 100
prestacao = valor_casa / meses

if prestacao < salario:
    print("A prestação é de %7.2f: " % prestacao)
else:
    print("a prestacao é muito alta")
