'''Faça um programa que leia um número qualquer
e mostre o seu fatorial'''

# from math import factorial
#
# n = int(input('Digite um número para calcular seu FATORIAL: '))
# f = factorial(n)
# print(f'O fatorial de {n} é {f}')
#  'Solução com módulo'

# n = int(input('Digite um número para calcular seu FATORIAL: '))
# c = n
# f = 1
# print(f'Calculando {n}! = ', end='')
# while c > 0:
#     print(f'{c}', end='')
#     print(f' x ' if c > 1 else'= ', end='')
#     f = f * c
#     c -= 1
# print(f'{f}')


n = int(input('Digite um número para calcular seu FATORIAL: '))
c = n
f = 1
for s in range (1 , c ):
    print(f'{c}', end='')
    print(f' x ' if c > 1 else '= ', end='')
    f = f * c
    c -= 1
print(f'{f}')