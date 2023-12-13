import random
from time import sleep
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Qual a sua jogada? '))
print('JO!')
sleep(0.8)
print('KEN!')
sleep(0.8)
print('PO!')
sleep(0.8)
print('-='*15)
print(f'O computador escolheu {lista[computador]}')
print(f'O jogador escolhou {lista[jogador]}')
print('-='*15)
if jogador == computador:
    print('EMPATOU')
elif computador == 0:
    if jogador == 1:
        print('Jogador ganhou!')
    elif jogador == 2:
        print('Jogador perdeu!')
elif computador == 1:
    if jogador == 0:
        print('Jogador perdeu!')
    elif jogador == 2:
        print('Jogador ganhou!')
elif computador == 2:
    if jogador == 0:
        print('Jogador ganhou!')
    elif jogador == 1:
        print('Jogador perdeu!')

#codigo simplificado
'''import random
print ("VAMOS JOGAR PEDRA, PAPEL E TESOURA!")
a = int(input("Considere:\n1 = PEDRA\n2 = PAPEL\n3 = TESOURA\nAgora, digite sua escolha: "))
b = random.randint(1,3)
print (b)
if a == b:
    print ("EMPATE")
elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print ("VOCÊ PERDEU!")
else:
    print ("VOCÊ GANHOU")'''

