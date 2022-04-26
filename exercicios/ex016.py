# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# ex: Digite um número 6.127, o número tem a parte inteira de 6
'''import math
num = float(input('Digite um número: '))
s = math.trunc(num)

print(f'O valor inteiro de {num:.2f} é {s}')'''

num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é: {int(num)}')



#Duas formas de fazer a mesma coisa, uma importando módulo e outra não.