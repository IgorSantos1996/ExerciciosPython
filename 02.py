kw = float(input("Informe a quantidade de kw consumida: "))
print("Tipos de instalação: ")
print("=========R de Residencial========")
print("========C de Comercial==========")
print("========I de Industrial=========")
preco = 0.0
tipo = input("Informe o tipo de instalação: ")
if tipo == "R":
    if kw <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == "C":
    if kw <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == "I":
    if kw <= 5000:
        preco = 0.55
    else:
        preco = 0.60
else:
    preco = 0
    print("Operação invalida")
custo = kw * preco
print("O tipo de instalação é %s e o valor a pagar é de %5.2f: " % (tipo, custo))
