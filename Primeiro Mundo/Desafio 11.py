#a cada 2m^2 de parede equivale a 1L de tinta
altura = float(input('Altura da parede:'))
largura = float(input('Largura da parede:'))
area = altura * largura
tinta = area/2
print(f'A parede tem um total de {area} metros quadrados e será necessário {tinta:.2f} litros de tinta')
