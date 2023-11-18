dias = int(input('Quantos dias alugados: '))
km = float(input('Quantos Km rodados: '))
custodia = dias*60
kmrodado = km*0.15
total = custodia + kmrodado

print(f'O total a pagar é de R${total:.2f}')