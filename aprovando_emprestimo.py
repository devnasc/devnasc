casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa/(anos*12)
minimo = salario*0.30

if prestacao <= minimo:
    print('Emprestimo aprovado')
else:
    print('Emprestimo negado')