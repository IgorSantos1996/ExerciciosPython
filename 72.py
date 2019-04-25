primeira = input("Informe a primeira string: ")
segunda = input("Informe a segunda string: ")

terceira = ""
for letra in primeira:
    if letra in segunda and letra not in terceira:
        terceira = terceira + letra
if terceira == "":
    print("Caracteres comuns não encontrados.")
print(terceira)