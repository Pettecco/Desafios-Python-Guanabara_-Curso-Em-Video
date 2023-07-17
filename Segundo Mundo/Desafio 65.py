#declaração das variáveis
media = 0
contador = 0

#entrada dos números e processamento dos dados
num = float(input('Digite um número: '))
maior = num
menor = num
contador += 1
media += num
flag = str(input('Deseja continuar [S/N]: ')).strip().upper()
while flag not in 'N':
    num = float(input('Digite outro número: '))   
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    contador += 1
    media += num
    flag = str(input('Deseja continuar [S/N]: ')).strip().upper()

#saída de dados
media = media / contador
print(f'A média dos números digitados é igual a {media}, o maior número inserido foi {maior} e o menor {menor}')
    
