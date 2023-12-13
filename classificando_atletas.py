from datetime import date
ano_atual = date.today().year
ano_nasc = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nasc
if idade <= 9:
    print(f'O atleta tem {idade} anos. MIRIM!')
elif idade <= 14:
    print(f'O atleta tem {idade} anos. INFANTIL!')
elif idade <= 19:
    print(f'O atleta tem {idade} anos. JÚNIOR!')
elif idade <= 25:
    print(f'O atleta tem {idade} anos. SÊNIOR!')
else:
    print(f'O atleta tem {idade} anos. MASTER!')
