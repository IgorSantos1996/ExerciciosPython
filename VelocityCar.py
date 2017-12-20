vel = float (input("informe a velocidade do carro: "))
multa = 5*(vel-80.0)
if vel > 80.0:
    print("Multado com certeza!")
    print("E sua multa é de %5.2f reais "% multa)
