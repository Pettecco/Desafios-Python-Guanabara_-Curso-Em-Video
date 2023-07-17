dias = int(input('Quantos dias alugado? '))
km = float(input('Quanto Km o carro percorreu? '))
preço = (dias * 60) + (km * 0.15)
print(f'O total a ser pago é R${preço:.2f}')