from random import randint

v = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if escolha == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')