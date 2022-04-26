'''Crie um programa que leia vários números inteiros
O programa só vai parar quando o usuário digitar 999
, que é a condição de parada. No final Mostre quantos foram digitados e a soma'''

cont = 0
soma = 0
while True:
    n = int(input('Digite um valor (999 para parar) : '))
    if n == 999:
        break
    soma = soma + n
    cont = cont + 1
print(f'Você digitou {cont} valores e a soma entre eles foi: {soma}')
