'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o
maior valor que estão na tupla.'''
from random import randint

numeros = randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5)
cont = 0
maior = None
menor = None
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
    if menor is None or n < menor:
        menor = n
    if maior is None or n > maior:
        maior = n


print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')