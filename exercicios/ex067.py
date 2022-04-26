'''Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. O programa
será interrompido quando o número solicitado for negativo'''
cont = 0
soma = 0

while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')



print(f'O seu programa finalizou, obrigado!')

