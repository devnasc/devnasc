from datetime import date
ano = int(input('Digite o ano que quer saber ou digite 0 para saber o ano atual: '))
if ano == 0:
    ano = date.today().year #pegar o ano atual da maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #para ser bissexto tem que atender essas condicoes
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')
