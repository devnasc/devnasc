salario = float(input('Digite o salário do funcionário: R$'))

if salario > 1250:
    salario = (salario*0.10) + salario
    print(f'O novo salário será de R${salario:.2f}')
else:
    salario = (salario*0.15) + salario
    print(f'O novo salário será de R${salario:.2f}')