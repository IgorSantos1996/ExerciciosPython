metros = float(input("Informe o valor em metros: "))
km = metros / 100
cm = metros * 100
mm = metros * 1000
print("A medida de {} m corresponde a {:.2f}, {:.2f} cm e {:.2f} mm ".format(
    metros, km, cm, mm))
