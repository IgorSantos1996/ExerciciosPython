numero = x = 171
invertido = 0

while numero != 0:
    digito = numero % 10
    invertido = (invertido * 10) + digito
    numero /= 10
if x == invertido:
    print("Palindromo!")
else:
    print("não é palindromo")
