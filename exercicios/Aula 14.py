#ESTRUTURA DE REPETIÇÃO WHILE

# n = 1
# while n != 0: #condição de parada
#     n = int(input('Digite um valor: '))
# print('Fim')

# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar? [S/N] ')).upper()
# print('Fim.')
parar = 0
par = impar = 0
while parar != 'S':
    n = int(input('Digite um valor: '))
    parar = str(input(f'Você quer parar o programa? [S/N]')).upper()
    if n % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Você digitou {par} números pares e {impar} números ímpares.')

