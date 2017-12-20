# Escreva um programa que leia dois npumeros e que pergunte qual operação você deseja realizar.Você deve poder
# calcular a soma (+), subtração (-), multiplicação ( x ) e divisão (/). Exiba o resultado da operação solicitada
numero1 = int(input("Informe o primeiro numero: "))
numero2 = int(input("Informe o segundo numero: "))
operação = input("Qual operação deseja realizar:? +,-,*,/ : ")
if operação == '+':
    print(" A adição de {} com {} é {} ".format(numero1,numero2,numero1+numero2))
if operação == "-":
    print('A subtração de {} com {} é  {} '.format(numero1,numero2,numero1 - numero2))
if operação == "*":
    print("A multiplicação de {} com {} é  {}  ".format(numero1,numero2,numero1*numero2))
if operação == "/":
    print("A divisão de %i por %i é: %i " % (numero1,numero2,numero1/numero2))
