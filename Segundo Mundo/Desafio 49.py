num = int(input('Digite um número: '))

print('A tabuada de {} é:'.format(num))
for i in range(1, 11):
    print(f'{num} x {i} = {num*i}')