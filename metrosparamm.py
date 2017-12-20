#programa para ler um valor em metros e transformar em milimetros
metros = float(input("Informe o valor em metros: "))
milimetros = metros * 1000
print("O valor em metros que vc forneceu foi de %5.2f, que em milimetros corresponde a %4.1f" % (metros,milimetros))