'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

n1 = int(input('Me diga um número qualquer: '))
resultado = n1 % 2

if resultado > 0:
    print('O seu número é impar!')
else:
    print('O seu número é par!')