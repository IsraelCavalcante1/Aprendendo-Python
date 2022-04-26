'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
'''

valor_casa = float(input('Qual o valor da casa a ser comprada: R$ '))
salário = float(input('Qual o seu salário: R$ '))
anos = int(input('Quantos anos de financiamento?'))
prestação = valor_casa / (anos * 12) # Aqui para saber de quanto será as prestações
mínimo = salário * 30 / 100 # Aqui temos um código para saber quanto é 30% do salário do comprador

print (f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos', end='')
print (f' a prestação será de R${prestação:.2f}')

if prestação <= mínimo: # Aqui estou falando que se a prestação for menor que 30% do salário, ela será aprovada
    print('Empréstimo APROVADO! ')

else: # Aqui é o contrário da linha "if", que diz que se a prestação for maior que 30% ela automaticamente será negada
    print('Infelizmente não podemos aprovar seu empréstimo, tente no futuro! ')







