from math import hypot
cateto_adjacente = float(input('Cateto Adjacente: '))
cateto_oposto = float(input('Cateto Oposto: '))
hipotenusa = hypot(cateto_adjacente, cateto_oposto)
print(f'A hipotenusa desse triangulo vale {hipotenusa:.2f}')