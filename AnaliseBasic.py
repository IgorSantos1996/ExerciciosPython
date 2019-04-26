#  Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome
nomec = str(input('Informe o nome completo: ')).strip()
print('O nome com todas as letras maiusculas são: ' , nomec.upper())
print('O nome com todas as letras minusculas são: ' , nomec.lower())
print('O nome tem ao todo: {} letras '.format(len(nomec) - nomec.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nomec.find(' ')))