primeira = input("Informe a primeira string: ")
segunda = input("Informe a segunda string: ")

terceira = ""
for letra in primeira:
    if letra not in segunda:
        terceira += letra
if terceira == "":
    print("Todos os caracteres foram removidos.")
else:
    print("OS caracteres %s foram removidos de %s, gerando: %s" %
          (segunda, primeira, terceira))
