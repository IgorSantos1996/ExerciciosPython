# Pergunte o salario, e reajuste a depender do valor!
salario = float(input("Informe o salario: "))
if salario > 1250.0:
    salario = salario + (salario * 10) / 100
    print("Salario reajustado: %5.2f" % salario)
if salario <= 1250.0:
    salario = salario + (salario * 15) / 100
    print("Salario reajustado: %5.2f" % salario)
