numeros = []
for c in range(1,4):
    num = int(input(f'Digite o {c}º número: '))
    numeros.append(num)
if numeros[0] == numeros[1] == numeros[2]:
    print('Não existe maior, os números são iguais!')
else:
    print(f'O maior número digitado foi {max(numeros)}')
    print(f'O menor número digitado foi {min(numeros)}')
