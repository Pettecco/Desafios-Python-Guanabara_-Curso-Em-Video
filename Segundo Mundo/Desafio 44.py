valor = float(input('Qual o valor do produto? R$ '))

print('''[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão
Qual será a opção de pagamento? ''')

option = int(input())

if option == 1:
    print('Desconto de 10%. O valor do produto passa a custar R${:.2f}'.format(valor - (valor * 0.10)))

elif option == 2:
     print('Desconto de 10%. O valor do produto passa a custar R${:.2f}'.format(valor - (valor * (5/100))))

elif option == 3:
    print('O preço do produto será R$ {}'.format(valor))

elif option == 4:
    print('Juros de 20%. O preço do produto será de R$ {}'.format(valor + (valor * 0.20)))

else:
    print('Opção inválida!')
