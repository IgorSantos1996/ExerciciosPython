# Escreva um programa que leia números inteiros do teclado.
# O programa deve ler os números até que o usuário digite 0 (zero).
# No final da execução exiba a quantidade de números digitados,
# assim como a soma e média aritmética
soma = 0
x = 0
while True:
    n = int(input("Informe um número: "))
    soma = soma + n
    x = x + 1
    if n == 0:
        break
media = soma / x
print(
    "A quantidade de números digitados é: %d, a soma é %d e a média é %5.2f"
    % (x, soma, media)
)

