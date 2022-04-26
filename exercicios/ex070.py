'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final mostre:

A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato.
'''

soma = 0
caros = 0
cont = 0
maior = 0
menor = None
nomemenor = 0

while True:
    nome = str(input(f'Qual o nome do produto que deseja comprar? '))
    preço = float(input(f'Qual o preço do produto que deseja comprar? R$'))
    escolha = str(input(f'Você deseja continuar? [S/N]')).upper().strip()[0]
    soma += preço
    cont += 1
    while escolha not in 'nNsS':
        escolha = str(input(f'Você deseja continuar? [S/N]')).upper().strip()[0]
    if preço > 1000:
        caros += 1
    if menor is None or preço < menor:
         menor = preço
         nomemenor = nome
    if escolha in 'nN':
        break
print(f'O valor total gasto nessa compra é: R${soma:.2f}')
print(f'Há {caros} produtos acima de R$1000 e são considerados produtos CAROS!')
print(f'O produto que custou menos foi o {nomemenor} e ele custou {menor}')
