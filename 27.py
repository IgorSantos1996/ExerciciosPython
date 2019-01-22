<<<<<<< HEAD
# Escreva um programa que leia um número e verifique se é ou não primo.
# Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos
# os número impares até o número lido. Se o resto de uma dessas divisões for igual a zero, o numero não é primo.
# Observe que 0 e 1 não são  primos e que 2 é o único número primo que é par.
n = int(input("Informe o numero: "))
if n == 2:
    print("2 é primo...")
elif n % 2 == 0:
    print("%d não é primo, pois 2 é o unico número par primo. " % n)
else:
    i = 3  # primeiro número impar que é primo, por isso começamos com 3
    while i < n:  # enquanto o contador for menor que o input
        if n % i == 0:  # testa se o numero que digitamos mod i tem resto == 0
            break
        i = i + 2
    if i == n:
        print("%d número é primo" % n)
    else:
        print("%d O número não é primo, pois é divisível por %d" % (n, i))
=======
while True:
    n = int(input("Informe o numero: "))
    if n == 2:
        print("%d é par!")
    if n == 0 or n == 1:
        print("0 e 1 são casos especiais!")
    else:
        i = 3
        while i > n:
            if n % i == 0:
                break
            i = i + 2
        if i == n:
            print("%d é primo" % n)
        else:
            print("%d não é primo, pois é divisível por %d" % (n, i))
>>>>>>> 6b56d86626e99067a61eade909707592b1a7181d
