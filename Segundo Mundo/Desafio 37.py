num = int(input('Digite um número: '))

print('''
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL 
Escolha uma opção para converter o número: ''')

option = int(input())

if option == 1:
    num = format(num, "b")
    print('O número na forma binária é {}'.format(num))

elif option == 2:
    num = format(num, "o")
    print('O número na forma octal é {}'.format(num))

elif option == 3:
    num = format(num, "x")
    print('O número na forma hexadecimal é {}'.format(num))

else:
    print('Opção inválida!')
