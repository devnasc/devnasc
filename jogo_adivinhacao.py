import random
print('-*-'*16)
print('Pensei em um número entre 0 e 5, tente adivinhar!')
print('-*-'*16)
pc = random.randrange(5)
jogador = int(input('Digite um número de 0 a 5: '))

if jogador == pc:
    print('Você acertou!')
else:
    print(f'Você errou, eu pensei no número {pc} ')
