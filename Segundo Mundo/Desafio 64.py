i = 0
soma = 0

num = int(input('Digite um número: '))
while num != 999:
    i += 1
    soma += num
    num = int(input('Digite outro número: '))

print(f'A soma dos {i} números inseridos é igual a {soma}')