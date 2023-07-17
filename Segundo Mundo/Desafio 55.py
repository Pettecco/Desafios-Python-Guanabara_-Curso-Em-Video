print('Digite o peso de 5 pessoas: ')

for i in range(0, 5):
    peso = float(input())
    if i == 0:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'A pessoa com o menor peso tem um total de {menor} kg e a com o maior peso tem {maior} kg')
