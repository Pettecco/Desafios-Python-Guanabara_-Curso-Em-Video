salario = float(input('Digite o salário: '))

if salario >= 1250:
    print(f'O aumento será de {(salario * 0.10)}')
else:
    print(f'O aumento será de {(salario * 0.15)}')
