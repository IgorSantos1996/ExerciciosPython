# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança
# Exiba os valores mês a mês para os 24 primeiros meses. Escreva o toral de ganho com juros no período
depo = float(input("Informe o deposito inicial: "))
taxa_juros = float(input("Informe a taxa de juros: "))
i = 1
saldo = depo
while i < 24:
    saldo = saldo + (saldo * (taxa_juros / 100))
    print("Mes %d, você tem %5.2f" % (i, saldo))
    i = i + 1
print("Ao fim dos 24 meses, seu ganho com os juros foi : %8.2f" % (saldo-depo))
