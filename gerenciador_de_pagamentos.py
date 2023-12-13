preco_compra = float(input('Preço das compras: R$ '))
print('''Forma de pagamento
[1] à vista dinheiro/pix
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    preco = preco_compra - (preco_compra*0.1)
    print(f'Sua compra de R${preco_compra:.2f} vai custar R${preco:.2f} no final.')
elif opcao == 2:
    preco = preco_compra - (preco_compra*0.05)
    print(f'Sua compra de R${preco_compra:.2f} vai custar R${preco:.2f} no final.')
elif opcao == 3:
    preco = preco_compra/2
    print(f'Sua compra de R${preco_compra:.2f} vai custar 2x de R${preco:.2f} no final.')
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    preco = preco_compra + (preco_compra*0.2)
    print(f'Sua compra parcelada ficará em {parcela}x de R${preco/parcela:.2f} com juros.')
    print(f'Sua compra de R${preco_compra:.2f} custará R${preco:.2f} no final')
