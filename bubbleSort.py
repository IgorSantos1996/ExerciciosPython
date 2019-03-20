l = [7, 4, 3, 12, 8]
fim = 5
while fim > 1:  # precisamos de no mínimo dois elementos
    trocou = False
    x = 0
    while x < (fim - 1):  # x seja anterior ao ultimo elemento
        if l[x] < l[x + 1]:
            trocou = True
            temp = l[x]
            l[x] = l[x + 1]
            l[x + 1] = temp
        x = x + 1
    if not trocou:  # se não trocamos nada de lugar, a lista está ordenada e
        # não precisamos executar a repetição outra vez, por iso o break
        break
    fim = (
        fim - 1
    )  # Nesse método de ordenação não precisamos verificar o ultimo elemento
    # após uma passagem completa. Como a ultima posição já está com o elemento correto diminuiremos
    # o valor de fim para que não precisemos mais verificá-lo
for e in l:
    print(e)

