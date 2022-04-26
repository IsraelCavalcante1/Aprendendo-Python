'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça]
para o usuário tentar descobrir qual foi o número escolhido pelo computador'''

from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador sortear/pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print(f'PARABÉNS! Você conseguiu me vencer! ')
else:
    print(f'Você é um perdedor! Eu pensei no número {computador} e não no {jogador}! ')


