'''Faça um programa que jogue par ou impar com o computador.
O joso só será interrompido quando o jogador PERDER, mostrando o total
de vitórias consecutivas que ele conquistou no final do jogo'''
from random import randint
vit = 0
soma = 0

while True:
    computador = randint(0, 10)
    jogador = int(input(f'Diga um valor: '))
    escolha = str(input(f'Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    soma = computador + jogador
    while escolha not in 'PI':
        escolha = str(input(f'Par ou Ímpar? [P/I]: ')).upper().strip()[0]

    if soma % 2 == 0 and escolha in 'pP':
        print(f'Deu PAR!')
        print(f'O computador escolheu o número {computador} e você {jogador}, somando é: {soma}')
        print(f'Você ganhou, continue jogando: ')
        vit += 1
    elif soma % 2 == 1 and escolha in 'iI':
        print(f'Deu ÍMPAR!')
        print(f'O computador escolheu o número {computador} e você {jogador}, somando é: {soma}')
        print(f'Você ganhou, continue jogando: ')
        vit += 1
    else:
        print(f'O computador escolheu o número {computador} e você {jogador}, somando é: {soma}')
        print(f'Você perdeu e teve {vit} vitórias consecutivas.')
        break


