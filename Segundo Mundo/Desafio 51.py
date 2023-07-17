primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão de PA: '))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo, +razao ):
    print(i, end =' -- ')

print('FIM')
