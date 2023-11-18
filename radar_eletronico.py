vel = int(input('Digite a sua velocidade: '))
if vel > 80:
    multa = (vel-80)*7
    print(f'Voce está acima do limite da velocidade')
    print(f'Sua multa é de R${multa}')
else:
    print('Tenha um bom dia!')