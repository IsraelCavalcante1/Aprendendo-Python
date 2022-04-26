'''Faça um programa que tenha uma função chamada maior(), que receba vários
parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

# maior1 = None
#
# def maior(maior1):
#     while True:
#         num = int(input('Digite um número: '))
#         if maior1 is None or maior1 < num:
#             maior1 = num
#         resp = str(input('Você quer continuar? S/N')).upper().strip()[0]
#         if resp in 'nN':
#             break
#     print(maior1)
# maior(maior1)
from time import sleep

# Segunda solução

def maior( * num):
    maior = None
    cont = 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end= '')
        sleep(0.3)
        if maior is None or maior < valor:
            maior = valor
        cont += 1 
    cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

# Programa principal
maior(2, 9, 4, 5, 7, 1)

# Programa principal

