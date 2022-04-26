'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''


n = int(input('Diga um número inteiro qualquer: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif opção == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif opção == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print(f'Sua opção não está disponível, tente novamente com uma opção válida.')

