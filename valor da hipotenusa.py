import math
n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjacente: '))
hip = n1**2 + n2**2
print(f'A hipotenusa é de {math.sqrt(hip):.2f}')
