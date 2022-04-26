'''Crie um programa que leia dois valores e mostre
um menu na tela:
'''

from time import sleep


n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
soma = n1 + n2
multiplicação = n1 * n2
opção = 0

while opção != 5:

    print('''Escolha uma das opções abaixo:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    print('-==-' * 10)
    # soma = n1 + n2
    # multiplicação = n1 * n2
    opção = int(input('>>>>>>> O que você quer fazer? '))
    if opção == 1:
        print('-==-' * 10)
        print(f'A soma dos números {n1} + {n2} é: {soma}')
        print('-==-' * 10)
    elif opção == 2:
        print('-==-' * 10)
        print(F'A multiplicação dos números {n1} x {n2} é: {multiplicação}')
        print('-==-' * 10)
    elif opção == 3:
        if n1 > n2:
            print('-==-' * 10)
            print(f'O {n1} foi o maior número e o {n2} o menor.')
            print('-==-' * 10)
        else:
            print('-==-' * 10)
            print(f'O {n2} foi o maior número e o {n1} o menor.')
            print('-==-' * 10)
    elif opção == 4:
        print('-=-' * 10)
        print('ESCOLHA NOVOS NÚMEROS')
        print('-=-' * 10)
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    else:
        print('Opção inválida, tente novamente...')
    sleep(2)

print(f'Finalizando...')
sleep(2)
print(f'Programa finalizado com sucesso!')


