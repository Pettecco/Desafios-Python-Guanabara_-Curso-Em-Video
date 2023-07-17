valorCasa = float(input('Qual o valor da casa? R$ '))
sal = float(input('Qual o salário do comprador? R$ '))
qntAnos = int(input('Em quantos anos será realizado o pagamento completo? '))

parcela = valorCasa / (qntAnos * 12)

print(f'O valor da parcela séra de R${parcela:.2f} mensalmente durante {qntAnos} anos.')

if parcela > (sal * 0.30):
    print('Empréstimo negado!')

else:
    print('Empréstimo aceito!')
