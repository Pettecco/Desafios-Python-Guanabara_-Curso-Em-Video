anoNascimento = int(input('Digite o ano de nascimento: '))
anoAtual = 2022 #ano em que estou escrevendo este código

idade = anoAtual - anoNascimento

print('A categoria do atleta é: ')

if idade <= 9 :
    print('Mirim')

elif idade <= 14:
    print('Infantil')

elif idade <= 19:
    print('Junior')

elif idade <= 20:
    print('Sênior')

elif idade > 20:
    print('Master')

else:
    print('Entrada inválida!!')