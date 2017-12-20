# Faça um programa que calcule o aumento de um salário.
# Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário
salario = float (input("Informe seu salário: "))
paumento = int (input("Informe o aumento: "))
fsalario = (salario * paumento)/100
print("O aumento foi de %4.2f reais, e o seu salário agora é de %5.2f reais " %(fsalario,salario+fsalario))