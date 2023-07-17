# Criando um programa que joga JOKENPÔ
from random import randint
from time import sleep

#definindo os itens
itens = ('pedra', 'papel', 'tesoura')

#jogada do computador
computador = randint(0, 2)

#apresentando as opções para o jogador
print('''Suas opções : 
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')

#agora o jogador faz a jogada
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(2)
print('-=' * 11)

#mostrando o que cada um jogou
print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
print('-=' * 11)

#montando as estruturas condicionais para apresentar os resultados
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')

    elif jogador == 1:
        print('VOCÊ GANHOU!')

    elif jogador == 2:
        print('VOCÊ PERDEU!')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1: #computador jogou PAPEL
    if (jogador == 0):
        print('VOCÊ PERDEU!')

    elif jogador == 1:
        print('EMPATE!')

    elif jogador == 2:
        print('VOCÊ GANHOU!')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: #computador jogou TESOURA  ]
    if jogador == 0:
        print('VOCÊ GANHOU!')

    elif jogador == 1:
        print('VOCÊ PERDEU!')

    elif jogador == 2:
        print('EMPATE!')

    else:
        print('JOGADA INVÁLIDA!')

       