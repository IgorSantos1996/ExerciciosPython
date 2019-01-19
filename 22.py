preco = 0.0
total = 0
while True:

    codigo = int(input("Informe o codigo do produto: "))
    if codigo == 0:
        break
    qtd_comprada = int(input("Informe a quantidade comprada: "))

    if codigo == 1:
        preco = qtd_comprada * 0.60
    elif codigo == 2:
        preco = qtd_comprada * 1
    elif codigo == 3:
        preco = qtd_comprada * 4.0
    elif codigo == 5:
        preco = qtd_comprada * 7.0
    elif codigo == 9:
        preco = qtd_comprada * 8.0
    else:
        print("Codigo inválido!!")
        preco = 0.0
    total = total + preco
print("O total é: %5.2f: " % total)
