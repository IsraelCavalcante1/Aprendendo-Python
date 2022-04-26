'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
 O programa vai ler o nome do jogador e quantas partidas ele jogou.
 Depois vai ler a quantidade de gols feitos em cada partida. No final,
 tudo isso será guardado em um dicionário,
 incluindo o total de gols feitos durante o campeonato.'''
jogador = dict()
partidas = list()
jogador['jogador'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["jogador"]} jogou?'))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}°? ')))
jogador['gols'] = partidas [:]
del partidas
jogador['total'] = sum(jogador['gols'])
print(f'-='*30)
print(jogador)
print(f'-='*30)
for k, v in jogador.items():
    print(f'{k} {v}')
print(f'-='*30)
print(f'O jogador {jogador["jogador"]} jogou {len(jogador["gols"])} partidas ')
for l, c in enumerate(jogador['gols']):
    print(f'   => Na partida {l+1}, fez {c} gols.')
print(f'Foi um total de {jogador["total"]}')
print(f'-='*15, f'FIM', '-='*13)


