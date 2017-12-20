# Faça um prgrama que leia a categoria de um produto e determine o preço da tabela
cate = int(input("Informe a categoria do produto: "))

if cate == 1:
    preco = 10.0
else:
    if cate == 2:
        preco = 18.0
    else:
        if cate == 3:
            preco = 23.0
        else:
            if cate == 4:
                preco = 26.0
            else:
                if cate == 5:
                    preco = 31.0
                else:
                    print("Categoria inválida, digite um valor entre 1 e 5!")
                    preco = 0
print("O preco do produto é: R$%6.2f " % preco)
