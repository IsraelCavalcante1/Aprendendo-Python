'''Faça um programa que leia 5 valors numéricos e guarde os em uma lista
No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista'''
maior = None
menor = None
listanum = []
for c in range (0, 5):
    listanum.append(int(input(f'Digite um número inteiro para a posição {c+1}: ')))
    if maior is None or listanum[c] > maior:
        maior = listanum[c]
    if menor is None or listanum[c] < menor:
        menor = listanum[c]



print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end= '')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i+1}...', end= '')
print(f'\nO menor valor digitado foi {menor} nas posições ', end= '')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i+1}...', end= '')


