vel = int(input('Qual a velocidade do carro? '))

if vel > 80:
    print('Você está MULTADO em R$ {},00.'.format((vel - 80) * 7))
else:
    print('Você estava dentro do limite permitido. Dirija com segurança!')