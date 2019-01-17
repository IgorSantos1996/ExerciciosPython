# Escreva um programa que pergunte o valor inicial de uma divida e o juros mensal.
# Pergunte também o valor mensal que será pago.
# Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago
divida = float(input("Informe o valor inicial da divida: "))
taxa = float(input("Informe o juros mensal: "))
pagamento = float(input("Informe o valor mensal que será pago: "))
meses = 0
if (
    divida * (taxa / 100) >= pagamento
):  # a sua divida é maior que o seu pagamento mensal
    print("Sua divida não jamais será paga, pois os juros são superiores ao pagamento mensal!")
else:
    saldo = divida 
    juros_pago = 0
    while saldo > pagamento:  # ou seja, ta devendo
        juros = saldo * taxa / 100
        saldo = saldo + juros - pagamento
        juros_pago = juros_pago + juros
        print("Saldo da dívida no mes %d é de R$%6.2f: " % (meses, saldo))
        meses = meses + 1
    print("Para pagar uma dívida de R$%8.2f, a %5.2f %% de juros," % (divida, taxa))
    print(
        "você precisará de %d meses, pagando um total de R$%8.2f de juros."
        % (meses - 1, juros_pago)
    )
    print("No último mês, você teria um saldo residual de R$%8.2f a pagar." % (saldo))
