
dias = int(input("Informe a quantidade de dias: "))
horas = int(input("Informe as horas: "))
minutos = int(input("Informe os minutos: "))
segundos = int (input("Informe os segundos, por fim.. : "))

total = ((dias*86400) + (horas*3600) + (minutos*60) + segundos)

print(dias,"dias", horas, "horas", minutos, "minutos", segundos, "segundos", ", equivale a", total, "segundos")