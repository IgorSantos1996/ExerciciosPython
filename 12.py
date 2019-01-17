tab = int(input("Tabuada do qual número: "))
inicio = int(input("Qual o inicio da tabuada: "))
fim = int(input("Qual o fim"))
x = inicio

while x <= fim:
    print(" %d x %d = %d " % (tab, x, tab * x))
    x = x + 1
    
