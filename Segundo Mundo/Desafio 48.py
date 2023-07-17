soma = 0
contador = 0

for i in range(0, 501, +3):
    if(i % 2 != 0):
        soma += i
        contador += 1

print('A soma de todos os {} valores é {}'.format(contador ,soma))