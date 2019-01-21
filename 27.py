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
