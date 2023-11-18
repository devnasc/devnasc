#desconto de 5%
valor = float(input('Digite o valor do produto: R$'))
desc = valor - (valor*0.05)
#5% = 0.05
print(f'O valor do produto de R${valor} com 5% de desconto fica R${desc:.2f}')