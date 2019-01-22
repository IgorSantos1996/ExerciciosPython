numero = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    numero[x] = int(input("Numero %d: " % (x+1)))
    x = x + 1
while True:
    escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    print("Você escolheu o numero: %d " % (numero[escolhido-1]))
    
numeros = [0, 0, 0, 0, 0]
k = 0
while k < 5:
    numeros[k] = int(input("Numero %d: " % (k+1)))
    k = k + 1
while True:
    escolhidos = int(input("Que posição deseja imprimir: (0 para sair)" ))