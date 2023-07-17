maior = 0
menor = 0

print('Digite a idade de 7 pessoas: ')

for i in range(0, 7):
    num = int(input())
    if num > 18:
        maior += 1
    else:
        menor += 1

print(f'{maior} pessoas já atingiram a maioridade e {menor} ainda não atingiram.')