'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''


salário = float(input('Qual o salário atual R$'))
if salário <= 1250.00:
    aumento = (salário * 15 / 100)
else:
    aumento = (salário * 10 / 100)


print(f'O aumento será de R${aumento:.2f}')