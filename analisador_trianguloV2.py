r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3 == r1:
        print('Podem formar um triangulo EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('Podem formar um triangulo ESCALENO!')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('Podem formar um triangulo ISOSCELES!')
else:
    print('Nao podem formar um trianglo')