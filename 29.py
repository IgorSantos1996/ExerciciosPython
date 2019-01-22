# Escreva um programa que calcule a raiz quadrada de um número.
# Utilize o método de Newton para obter um resultado aproximado. Sendo n o número a obter a raiz
# quadrada, considere a base b = 2. Calcule p usando a fórmula p = (b+(n/b))/2.
# Agora calcule o quadrado de p. A cada passo, faça b=p e calcule p usando a fórmula apresentada.
# Para quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001.

n = float(input("Digite um numero: "))
b = 2
while abs(n - (b*b)) > 0.00001:
    p = (b+(n/b))/2
    b = p
print("A raiz quadrada de %d é aproximadamente %8.4f" % (n, p))
