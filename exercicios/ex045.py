# # Crie um programa que faça o computador jogar Jokenpô com você.
import time
from random import randint
#
#

#          ############ MINHA SOLUÇÃO PARA O EXERCÍCIO ############
print(f'''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual a sua jogada?',))

print('-='* 18)
print(f'JO')
time.sleep(1)
print(f'KEN')
time.sleep(1)
print(f'PÔ!!!')
print('-='* 18)
computador = randint(0 , 2)


# CONFIGURAÇÕES COMPUTADOR
if computador == 0:
    print(f'Computador jogou PEDRA ')
elif computador == 1:
    print(f'Computador jogou PAPEL ')
elif computador == 2:
    print(f'Computador jogou TESOURA ')
time.sleep(2)
#CONFIGURAÇÕES JOGADOR

if jogador == 0:
    print(f'Jogador jogou PEDRA')
elif jogador == 1:
    print(f'Jogador jogou PAPEL')
elif jogador == 2:
    print(f'Jogador jogou TESOURA')

time.sleep(2)

#CONFIGURAÇÕES DO VENCEDOR
if computador == jogador:
    print(f'Houve um EMPATE!!')
elif computador == 0 and jogador == 1:
    print(f'JOGADOR GANHOU!!')
elif computador == 1 and jogador == 0:
    print(f'COMPUTADOR GANHOU!!')
elif computador == 2 and jogador == 0:
    print(f'JOGADOR GANHOU!!')
elif computador == 0 and jogador == 2:
    print(f'COMPUTADOR GANHOU!!')
elif computador == 2 and jogador == 1:
    print(f'COMPUTADOR GANHOU!!')
elif computador == 1 and jogador == 2:
    print(f'JOGADOR GANHOU!!')
print('-='* 18)

time.sleep(2)

#################################### SOLUÇÃO DO PROFESSOR PARA RESOLVER O EXERCÍCIO, BEM MAIS SIMPLIFICADA ########################
# from random import randint
# itens = ('PEDRA', 'PAPEL', 'TESOURA')
# computador = randint (0, 2)
# print(f'''Suas opções:
# [ 0 ] PEDRA
# [ 1 ] PAPEL
# [ 2 ] TESOURA''')
# jogador = int(input('Escolha uma das opções: '))
# print('-=' * 11)
# print(f'COMPUTADOR jogou {itens[computador]}')
# print(f'JOGADOR jogou {itens[jogador]}')
# print('-=' * 11)
#
# if computador == 0: #COMPUTADOR JOGOU PEDRA
#     if jogador == 0:
#         print(f'EMPATE')
#
#     elif jogador == 1:
#         print(f'JOGADOR VENCE')
#
#     elif jogador == 2:
#         print(f'COMPUTADOR VENCE')
#
#     else:
#         print('JOGADA INVÁLIDA')
#
# elif computador == 1: # COMPUTADOR JOGOU PAPEL
#
#     if jogador == 0:
#         print(f'COMPUTADOR VENCE')
#
#     elif jogador == 1:
#         print(f'EMPATE')
#
#     elif jogador == 2:
#         print(f'JOGADOR VENCE')
#
#     else:
#         print('JOGADA INVÁLIDA')
#
#
# elif computador == 2: # COMPUTADOR JOGOU TESOURA
#
#     if jogador == 0:
#         print(f'JOGADOR VENCE')
#
#     elif jogador == 1:
#         print(f'COMPUTADOR VENCE')
#
#     elif jogador == 2:
#         print(f'EMPATE')
#     else:
#         print('JOGADA INVÁLIDA')




# print(f'O computador escolheu {itens[computador]}') #colocando itens na posição computador



