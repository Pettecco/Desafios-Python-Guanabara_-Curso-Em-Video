sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    print('Entrada inválida!')
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

if sexo =='M':
    sexo = 'masculino'
else:
    sexo = 'feminino'

print(f'Pessoa do sexo {sexo} cadastrada')


 