# Variável para fazer a média de idade das pessoas cadastradas
media = 0
# Variável que irá guardar o número de mulheres com a idade menor que vinte
mulheresVinte = 0
# Variável auxiliar para saber qual o primeiro homem a ser cadastrado para salvar sua idade e usar como comparação 
auxMasc = 0

for i in range(0, 4):
    nome = str(input('Digite um nome: '))
    idade = int(input('Digite uma idade: '))
    media += idade
    sexo = str(input('Digite o sexo [M/F]: '))
    if sexo == 'F' and idade < 20:
        mulheresVinte += 1
    if sexo == 'M' and auxMasc == 0:
        nomeMaior = nome
        maior = idade
        auxMasc = 1
    if sexo == 'M' and idade > maior:
        maior = idade
        nomeMaior = nome
    
media = media/4

print('A média de idade do grupo é de {:.2f}\n'.format(media))
print(f'O homem com a maior idade é {nomeMaior} com {maior} anos. E o grupo conta com {mulheresVinte} mulheres com menos de vinte anos')    