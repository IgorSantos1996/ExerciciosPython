primeira = input("Informe a primeira string: ")
segunda = input("Informe a segunda string: ")
terceira = input("Informe a terceira string: ")
if len(segunda) == len(terceira):
    resultado = ""
    for letra in primeira:
        posicao = segunda.find(letra)
        if posicao != -1:
            resultado = resultado + terceira[posicao]
        else:
            resultado = resultado + letra
    if resultado == "":
        print("todos os caracteres foram removidos.")
    else:
        print("Os caracteres %s foram substituidos por %s em %s, gerando: %s" %
              (segunda, terceira, primeira, resultado))
else:
    print("ERRO: A segunda e a terceira string devem ter o mesmo tamanho.")
