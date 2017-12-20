#Escreva um programa que calcule o tempo de uma viagem de carro.
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem
dist = float(input("Informe a distancia a percorrer: "))
speed = float(input("Informe a velocidade média esperada: "))
print("O tempo de viagem será de %3.2f: " % (dist/speed))