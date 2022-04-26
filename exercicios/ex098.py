'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

from time import sleep


def cont1():
    for c in range (1, 11, 1):
        print(c, end=' ')
        sleep(0.5)

def contador():
    for d in range (10, -2, -2):
        print(d)
        sleep(0.5)
def contadorperso():
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    for c in range (inicio, fim, passo):
        print(c)
        sleep(0.5)



cont1()
print('')
print ('-='*16)
contador()
print ('-='*16)
contadorperso()










