# Escreva um programa que leia duas Strings. Verifique se a segunda
# ocorre dentro da primeira e imprima a posição de início.

s1 = input("Informe a primeira string: ")
s2 = input("Informe a segunda string: ")

p = s1.find(s2) # verificando se a segunda está dento da primeira
                # retorna -1 indicando falha
if p == -1: 
    print("%s não encontrada em '%s'" % (s2, s1))
else:
    print("%s encontrada na posição %d de %s" % (s2, p, s1))
