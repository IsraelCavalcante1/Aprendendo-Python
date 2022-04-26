'''Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função
vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint
from time import sleep

numeros = list()


def sorteia(*num):
    for c in range (0, 5):
        numeros.append(randint(0, 10))
    print(f'-'*10, 'Os números estão sendo sorteados', '-'* 10)
    print(f'Os numeros sorteados são:', end='')
    for num in numeros:
        print(num, end=' ')
        sleep(0.3)
    print('')

def SomaPar():
    soma = 0
    print(f'Os numeros pares são: ', end=' ')
    for par in numeros:

        if par % 2 == 0 and par > 0:
            print(f'{par}', end=' ')
            soma = soma + par
    print('')
    print(f'A soma total dos números pares é: {soma}')

# Programa Principal

sorteia()
SomaPar()












