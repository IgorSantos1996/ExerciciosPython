# Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
co = float(input('Informe o comprimento do cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))
hipo = (co**2 + ca**2) ** (1/2)  # ou math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hipo))
