distancia = float(input('Qual a distancia da viagem (em Km)? '))

if distancia <= 200:
    print('O preço da passagem será de R$ {:.2f}'.format(distancia * 0.50))
else:
    print('O preço da passagem será de R$ {:.2f}'.format(distancia * 0.45))