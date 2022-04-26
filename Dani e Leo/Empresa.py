# Uma empresa contratou um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados e
# imprima a quantia liquida que deverá ser paga, sabendo-se que são descontados 8% para o imposto de renda


dias = int(input('Quantos dias o encanador trabalhou?'))
pagamento = dias*30
imposto_renda = pagamento*0.08
valor_total = pagamento-imposto_renda



print(f'Pagamento: {pagamento}')
print(f'Imposto de renda: {imposto_renda}')
print(f'O valor a ser recebido é de: {valor_total}')


