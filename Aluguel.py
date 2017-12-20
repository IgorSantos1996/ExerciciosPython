#Você foi contratado para desenvolver um sistema de uma locadora de carros, seu trabalho é desenvolver um sistema
#que calcule o dia em que o usuário terá que devolver o carro à locadora. O formato de entrada será o seguinte:
#Nome:
#Data atual:
#Quantidade de dias de aluguel:
#Já a tela de saída terá que conter os seguintes dados:
#Nome:
#Data de entrega do veículo:
from datetime import date
nome = input("Nome: ")
data = int(input("Data atual: "))
qtd = input("Quantidade de dias de aluguel: ")

print (int(data / 1000000))
print("""
Nome: {}
Data de entrega do veículo: {}""".format(nome,data))
