# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário,
# digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
n = 0
n = int(input('Digite um valor: '))
cont = 0
soma = 0
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um valor: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')