nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))

media = (nota1 + nota2) / 2

print(f'A média foi de {media:.2f}')

if media > 7:
    print('Aluno APROVADO!')

elif media < 7 and media >= 5:
    print('Aluno está de recuperação!')

elif media < 5:
    print('Aluno REPROVADO!')