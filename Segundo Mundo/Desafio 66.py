i = 0 # contador
soma = 0 # soma dos valores inseridos
n = 0

while True:

    n = float(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    i += 1

print(f'Foram digitados {i} valores. A soma entre eles é {soma}!')
