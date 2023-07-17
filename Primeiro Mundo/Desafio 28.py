from random import randint

num_computador = randint(0, 5)

num_usuario = int(input('Estou pensando em um número entre 0 e 5, tente adivinhar qual: '))

if num_usuario == num_computador:
    print('Você acertou!')
else:
    print(f'Você errou! Eu estava pensando no número {num_computador}') 