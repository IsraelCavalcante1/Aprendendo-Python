'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter
resultado = dict()
resultado['Primeiro jogador'] = randint(1, 6)
resultado['Segundo jogador'] = randint(1, 6)
resultado['Terceiro jogador'] = randint (1, 6)
resultado['Quarto jogador'] = randint(1, 6)
ranking = list()
print('Valores sorteados: ')
for k, v in resultado.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(resultado.items(), key=itemgetter(1), reverse= True )
print(f'-='*10, 'RANKING', '-='*10)
for i, v in enumerate (ranking):
    print(f' {i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
