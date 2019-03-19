lugares_vagos = [10, 2, 1, 3, 0] # lugares vagos nas salas 1,2,3,4,5 respectivamente
while True:
    sala = int(input("Sala (0 sai): ")) #Lê o numero da sala
    if sala == 0: #encerrar se escolhermos 0
        print("Fim")
        break
    if sala > len(lugares_vagos) or sala < 1: # se a sala que escolhemos for maior que
                                                # o tamanho da lista ou se for < 1
        print("Sala inválida")
    elif lugares_vagos[sala-1] == 0:   # se na minha lista, na posição correspondente
                                        # à sala que escolhemos for 0 
        print("Desculpe, sala lotada!")
    else:
        lugares = int( #se ainda tem lugar vazio
            input("Quantos lugares você deseja (%d vagos): " % lugares_vagos[sala-1]))
        if lugares > lugares_vagos[sala-1]:
            print("Esse número de lugares não está disponível.")
        elif lugares < 0:
            print("Numero inválido")
        else:
            lugares_vagos[sala-1] = lugares_vagos[sala-1] - lugares
            print("%d lugares vendidos" % lugares)
print("Utilização das salas")
for x, l in enumerate(lugares_vagos):
    print("Sala %d - %d lugar(es) vazio(s)" % (x+1, l))
