nome = str(input('Qual seu nome completo: ')).strip()
nome = nome.split()
print(' Muito prazer em te conhecer!\n Seu primeiro nome é {}\n Seu último nome é {}'.format(nome[0], nome[-1]))