soma = 0

print('Digite 6 valores:')


for i in range(0, 7):
    num = int(input())
    if(num % 2 == 0):
        soma += num

print(f'A soma entre os valores pares digitados é igual a {soma}')