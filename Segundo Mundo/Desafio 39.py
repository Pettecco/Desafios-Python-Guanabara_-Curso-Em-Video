idade = int(input('Qual a sua idade? '))
ano = 2022 #ano no qual estou escrevendo o código

print('Quem nasceu no ano de {}:'.format(ano - idade))

if idade == 18:
    print('Se alistar este ano!')

elif idade < 18:
    print('Deve se alistar daqui {} anos.'.format(18 - idade))

elif idade > 18:
    print('Já se alistou / deveria ter se alistado.')
