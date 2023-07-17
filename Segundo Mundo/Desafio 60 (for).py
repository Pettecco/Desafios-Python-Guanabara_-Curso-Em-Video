#fatorial de um número com for
n = int(input('Digite um número: '))
fat = 1

for c in range(1, n + 1):
    fat *= c

print(f'O fatoral de {n} é {fat}')