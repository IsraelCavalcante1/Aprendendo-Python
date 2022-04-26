'''Melhore o jogo do DESAFIO 028 onde o computador vai
"Pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acerter, mostrando no final quantos palpites foram
necessários para vencer.'''

from random import randint
from time import sleep

computador = randint(0, 10)
contador = 1
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')


while jogador != computador:
    if jogador != computador:
        contador += 1
        print(f'Você errou, o número que pensei não foi esse... Tente novamente!')
        if jogador < computador:
            print('É pra cima...')
        if jogador > computador:
            print('É pra baixo...')
    jogador = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')




print(f'Você acertou, o número que a máquina pensou é {computador} e você deu {contador} palpites')
