num = float(input(f'Digite a distancia em metros: '))
print(f'A medida de {num} corresponde a: ')
print(f'''{num/1000}km
{num/100}hm
{num/10}dam
{num*10:.0f}dm
{num*100:.0f}cm
{num*1000:.0f}mm''') # o :.0f significa que não tera casa decival