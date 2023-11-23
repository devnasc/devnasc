#n1 = int(input('Digite o primeiro número: '))
#n2 = int(input('Digite o segundo número: '))
#if n1 == n2:
    #print('Os valores são iguais')
#else:
 #   print(f'O menor valor foi {min(n1, n2)}')
  #  print(f'O maior valor foi {max(n1, n2)}')

numero = []
for c in range(1,3):
    n = int(input(f'Digite o {c}º número: '))
    numero.append(n)
if numero[0] == numero[1]:
    print('Não existe maior, os dois são iguais!')
else:
    print(f'O maior é {max(numero)}')
    print(f'O menor é {min(numero)}')