expression = input("Digite a sequencia de parênteses a ser avaliada: ")
x = 0
pilha = []
while x < len(expression):
    if (expression[x] == "("):
        pilha.append("(")
    if expression[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1) # ultimo elemento
        else:
            pilha.append(")")
            break
    x = x + 1
if len(pilha) == 0:
    print("ok")
else:
    print("Error")
