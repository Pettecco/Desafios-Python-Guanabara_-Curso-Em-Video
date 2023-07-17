#Cálculo do IMC
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))

imc = peso / (altura * altura)

print('IMC = {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso.')

elif imc < 25:
    print('Peso ideal')

elif imc < 30:
    print('Sobrepeso.')

elif imc < 40:
    print('Obesidade.')

elif imc > 40:
    print('Obesidade mórbida.')

else:
    print('Valor inválido!')