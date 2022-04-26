'''Crie um programa que tenha uma tupla totalmente
preenchida com uma contagem por extenso, de zero até vinte'''
'''Seu programa deverá ler um número pelo teclado (entre zero e vinte
e mostra-lo por extenso.'''

cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
opção = ''
while opção in 'sS':
        n = int(input('Digite um número entre 0 e 20: '))
        while n <= 0 and n <= 20:
                n = int(input('Digite um número entre 0 e 20: '))
        print(f'Você digitou o número {cont[n]}')
        opção = str(input('Você quer continuar? S/N: ')).upper().strip()[0]

