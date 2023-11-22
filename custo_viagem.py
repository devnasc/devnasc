dist = float(input('Qual a distância da viagem?  '))
if dist < 200:
    valor = dist*0.50
    print(f'A viagem custará R${valor:.2f}')
else:
    valor = dist*0.45
    print(f'A viagem custará R${valor:.2f}')

    