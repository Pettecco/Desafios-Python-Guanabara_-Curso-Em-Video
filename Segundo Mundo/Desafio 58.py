from random import randint

computador = randint(0, 10)
palpites = 1

jogador = int(input('Tente acertar o número no qual estou pensando: '))

while jogador != computador:
    print('Palpite errado.')
    jogador = int(input('Tente novamente: '))
    palpites += 1

print(f'Você acertou em {palpites} palpites!! Eu estava pensando no número {jogador}')
