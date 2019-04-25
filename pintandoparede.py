largura = float(input('Informe a largura: '))
altura = float(input('Informe a altura: '))
area = altura * largura
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(
    largura, altura, area))
tinta = area * .5 # cada 2m² eu preciso de 2 litros de tinta
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
