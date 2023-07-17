print('=-' * 11)
print('VAMOS AS COMPRAS')
print('=-' * 11)

# inicialização das variáveis
soma = 0
mil = 0
menor = ''
# loop de cadastro dos produtos
while True:
    nome = str(input('Nome do produto: '))
    menor = nome
    preço = float(input('Preço: R$'))
    barato = preço
    if preço > 1000:
        mil += 1
    if preço < barato:
        barato = preço
        menor = nome
    soma += preço
    flag = ' '
    while flag not in 'SN':
        flag = str(input('Deseja comprar mais [S/N]? ')).strip().upper()[0]
    if flag == 'N':
        break

# saída de dados
print(f'O total da compra foi {soma:.2f}')
print(f'Temos {mil} produtos custando mais de R$1000.00.\nO produto mais barato foi {menor} que custa R${barato:.2f}')