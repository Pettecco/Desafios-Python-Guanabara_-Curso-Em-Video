num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

print('''
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
''')

op = int(input('Escolha uma operação: '))

while op != 5:
    if op == 1:
        print('A soma de {} + {} é {}'.format(num1, num2, num1 + num2))
    elif op == 2:
        print('O produto de {} x {} é {}'.format(num1, num2, num1 * num2))
    elif op == 3:
        if num1 > num2:
            print(f'{num1} é o maior número')
        else:
            print(f'{num2} é o maior número')
    elif op == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    op = int(input('Escolha uma operação: '))