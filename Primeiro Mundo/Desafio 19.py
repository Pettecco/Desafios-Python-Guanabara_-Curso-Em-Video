from random import choice

aluno_1 = str(input('Digite o nome do primeiro aluno: '))
aluno_2 = str(input('Digite o nome do segundo aluno: '))
aluno_3 = str(input('Digite o nome do terceiro aluno: '))
aluno_4 = str(input('Digite o nome do quarto aluno: '))

lista_de_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
escolhido = choice(lista_de_alunos)
print(f'O aluno(a) escolhido foi: {escolhido}')