#Programa que converte uma temperatura em digitada em °C para °F. A formula para conversão será apresentada no código
celsius = float(input("Informe a temperatura em °C: "))
f = ((9 * celsius)/5 + 32)
print("A temperatura que você informou foi : %3.2f °C, convertendo para °F fica: %4.2f °F" % (celsius,f))