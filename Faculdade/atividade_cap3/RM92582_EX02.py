print('*'*10,'Seja bem vindo á calculadora de média','*'*10)
transacoes = int(input('Quantas transações foram feitas hoje? '))
soma = 0
print('Informe qual o valor de cada transação: ')
for i in range(transacoes):
    valorTransacao = float(input(f'Qual foi o valor da {i + 1}° transação? R$'))
    soma += valorTransacao
media = soma / transacoes
print(f'Você fez {transacoes} transações durante o dia e a média de valor delas é de R${media:.2f}')

