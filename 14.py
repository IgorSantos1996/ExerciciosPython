dividendo = int(input("Informe o primeiro numero: ")) #10
divisor = int(input("Informe o segundo numero: ")) #3
# imprimir a divisão inteira e o resto
quociente = 0
x = dividendo # x = 10
while x >= divisor:      # 0 > 3 , fim, sai do laço e o resto é 0, acabou a divisão :)
    x = x - divisor      # 3 = 3 - 3, = 0
    quociente = quociente + 1 # 4
resto = x
print("%d / %d = %d (quociente) %d (resto)" % (dividendo, divisor, quociente, resto))
