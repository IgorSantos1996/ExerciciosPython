# Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
# Esse valor será depositado no início de cada mês,e vc deve considerá-lo para o calculo
# de juros do mês seguinte.
deposito = float(input("Informe o deposito: "))
taxa = float(input("Informe o deposito: "))
investimento = float("Qual o valor deposito mensalmente: ")
mes = 1
saldo = deposito
while mes < 24:
    saldo = saldo + (saldo * (taxa / 100)) + investimento
    print("No mes %d voce tem %5.2f: " % (mes, saldo))
    mes += 1
print("Ao fim dos 24 meses, você conseguiu %5.2f: " % (saldo - deposito))

