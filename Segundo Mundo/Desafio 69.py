maior = 0
homens = 0
mulheres = 0

while True:
    sexo = flag = ' '
    idade = int(input('Digite uma idade: '))
    if idade > 18:
        maior += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'F' and idade < 20:
        mulheres += 1
    if sexo == 'M':
        homens += 1
    while flag not in 'SN':
        flag = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if flag == 'N':
        break

print(f'Foram cadastradas {maior} pessoas com mais de 18 anos. Entre elas {homens} homens, e {mulheres} mulheres com menos de 20 anos.')