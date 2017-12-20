#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
#total de dias.
qtdCigaretes = int(input("informe a quantidade de cigarros fumados por dia: "))
yearsFumantes = int(input("Quantos anos de fumante: "))
total = qtdCigaretes*(yearsFumantes*365)
diasLost = (total*10)/24
print("Perdeu - se %d dias" % total)


