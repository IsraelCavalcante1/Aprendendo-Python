 '''Faça um programa que leia nome e peso de várias pessoas
guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
pessoas = list()
temp = list()
maior = None
menor = None

while True:
    temp.append(str(input('Digite seu nome: ')))
    temp.append(float(input('Digite seu peso: ')))
    if maior is None or temp[1] > maior:
        maior = temp[1]
    if menor is None or temp[1] < menor:
        menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    opção = str(input(f'Você quer continuar? [S/N]')).upper().strip()[0]
    if opção in 'nN':
        break
print(f'-=' * 30)
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas')
print(f'Os maiores pesos são {maior}KG e são das respectivas pessoas: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end= ' ')
print(f'\nOs menores pesos são {menor}KG e são das respectivas pessoas: ', end='')
for c in pessoas:
    if c [1] == menor:
        print(f'{c[0]}')
print(f'-=' * 30)
 