salario = float(input("Digite o salario para calculo do imposto: "))
base = salario
imposto = 0
if base > 300:
    imposto = imposto + ((base - 300) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print("Salário: R$%6.2f Imposto a pagar: R$%6.2f " % (salario, imposto))