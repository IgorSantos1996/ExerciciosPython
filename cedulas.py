# Suponha que um caixa bancário tenha cédulas de R$1.00
# R$2.00, R$5.00 e R$10.00. Faça um programa que retorne
# a menor quantidade de cédulas de cada valor a ser sacado.
valor = float(input('Digite o valor do dinheiro:'))

if (valor>=10):
     valor = valor -100
     n100=n100+1;
elif (valor>=50):
    valor=valor-50
    n50=n50+1
elif (valor>=25):
    valor=valor-25
    n25=n25+1
elif (valor>=10):
    valor=valor-10
    n10=n10+1
elif (valor>=5):
    valor=valor-5
    n5=n5+1
else: Q=Q-1; n1=n1+1
print(
    '''A quantidade de notas de 10 é {} , de 5 é {} , de 2 é {} e de 1 é {}'''.format(qtd_nota10, qtd_nota5, qtd_nota2,
                                                                                      qtd_nota1))
