nome = str(input('Digite o seu nome: '))

print(f'seu nome em maiusculo é {nome.upper()}')
print(f'seu nome em minusculo é {nome.lower()}')
print(f'seu nome tem {len(nome) - nome.count(' ')} letras')
print(f'Seu primeiro nome tem {nome.find(' ')} letras')