'''Crie um programa que vai ler vários números e colocar em uma lista.
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente
C) Se o valor 5 foi digitado e está ou não na lista.'''


lista = list()

while True:
    n = int(input(f'Digite um número:  '))
    lista.append(n)
    opção = str(input(f'Você quer continuar? [S/N] ')).upper().strip()[0]
    if opção != 'Nn' or opção != 'sS':
        opção = str(input(f'Opção inválida, você quer continuar? [S/N]')).upper().strip()[0]
        if opção in 'Nn':
            break
print('-=' * 30)
print(f'Foram digitados {len(lista)} números em sua lista!')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print(f'O valor 5 foi digitado')
else:
    print(f'O valor 5 não foi digitado.')
print('-=' * 30)
