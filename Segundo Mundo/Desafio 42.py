r1 = float(input('Digite o primeiro valor: '))
r2 = float(input('Digite o segundo valor: '))
r3 = float(input('Digite o terceiro valor: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:

    if r1 == r2 and r1 == r3:
        print('As retas formam um triângulo equilátero!')

    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('As retas formam um triângulo isóceles!')

    else:
        print('As retas formam um triângulo escaleno!')

else:
    print('As retas NÃO formam um triângulo!')
