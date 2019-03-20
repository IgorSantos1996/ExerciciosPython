tabela = {"Alface": 0.45, "Batata": 1.20, "Tomate": 2.30, "Feijão": 1.50}
# dictionary
while True:
    produto = input("Digite o nome do produto, fim para terminar:")
    #nome do produto que sera pesquisado no dicionário
    if produto == "fim":
        break
    if produto in tabela:
        print("Preço %5.2f" % tabela[produto])
    else:
        print("Produto não encontrado")