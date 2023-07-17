#fatorial com while
num = int(input('Digite um número: '))

fat = 1
c = 1

while c <= num:
    fat *= c
    c += 1

print(f'O fatoral de {num} é {fat}')