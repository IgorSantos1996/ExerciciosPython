# Escreva um programa que leia três números e que imprima o maior e o menor
num1 = int(input("Informe um numero: "))
num2 = int(input("Informe o segundo numero: "))
num3 = int(input("Informe o terceiro numero: "))
maior = num1
menor = num1
if maior < num2:
    maior = num2
if maior < num3:
    maior = num3
if menor > num2:
    menor = num2
if menor > num3:
    menor = num3
print("O maior numero é o {}""".format(maior))
print("O menor numero é o {}""".format(menor))
