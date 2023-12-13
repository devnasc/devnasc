peso = float(input('Qual seu peso? (KG) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura**2)
if imc < 18.5:
    print(f'O IMC é de {imc:.1f}, ABAIXO DO PESO!')
elif imc < 25:
    print(f'O IMC é de {imc:.1f}, PESO IDEAL!')
elif imc < 30:
    print(f'O IMC é de {imc:.1f}, SOBREPESO!')
elif imc < 40:
    print(f'O IMC é de {imc:.1f}, OBESIDADE!')
else:
    print(f'O IMC é de {imc:.1f}, OBESIDADE MORBIDA!')

