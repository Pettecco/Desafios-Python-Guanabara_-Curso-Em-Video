number = int(input('Digite um número de 1 a 9999: '))
unidade = number // 1 % 10 
dezena = number // 10 % 10 
centena = number // 100 % 10 
milhar = number // 1000 % 10 
print(f'Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')