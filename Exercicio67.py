# Faça um programa que leia uma expressão como parênteses.
# Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta.
pilha = []
x = 0

expressao = input("Digite a seequencia de parênteses a validar: ")
while x < len(expressao):
    if (expressao[x] == "("):
        pilha.append("(")
    if (expressao[x] == ")"):
        if (len(pilha) > 0):
            pilha.pop(-1) # ultimo elemento inserido
        else:
            pilha.append(")")
            break
    x = x + 1
if (len(pilha) == 0 ):
    print("Ok")
else:
    print("Erro")

