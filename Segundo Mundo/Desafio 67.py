n = 0

while True:
    n = int(input('Qual valor gostaria de ver a tabuada? '))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
    print('--' * 10)

print('Programa encerrado')