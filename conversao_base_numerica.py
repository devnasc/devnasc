num = int(input('Digite um número: '))
print('''Escolha uma opção
[1] Para Binário
[2] Para Octal
[3] Para Hexadecimal''')
opcao = int(input('Escolha a opção: '))

if opcao == 1:
    print(f'O número escolhido convertido para BINÁRIO fica: {format(num, "b")}')
elif opcao == 2:
    print(f'O número escolhido convertido para OCTAL fica: {format(num, "o")} ')
elif opcao == 3:
    print(f'O número escolhido convertido para HEXADECIMAL fica: {format(num, "x")}')
#A função format retornará a saída formatada de acordo com a função, removendo o prefixo 0b quando utilizado bin(x) por exemplo
