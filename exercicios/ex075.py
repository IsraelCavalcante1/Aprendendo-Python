'''Desenvolva um programa que leia quatro valores
pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''



n = (int(input('Digite um número: ')), \
    int(input('Digite um número: ')), \
    int(input('Digite um número: ')), \
    int(input('Digite um número: ')))
print(f'Você digitou os valores {n}')
print(f'O valor 9 apareceu {n.count(9)}') #contar quantas vezes apareceu o valor 9
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram', end=' ')
for s in n :
    if s % 2 == 0:
        print(s, end=' ')
