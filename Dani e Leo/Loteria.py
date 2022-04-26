# três amigos jogaram na loteria. Caso eles ganhem, o premio deve ser repartido
# proporcionalmente ao valor que cada deu para a realizacao da aposta. Faca um programa
# que leia quanto cada apostador investiu, o valor do premio, e imprima quanto cada um
# ganharia do premio com base no valor investido.


aposta1 = float(input('Qual foi o valor que o Joãozinho deu?'))
aposta2 = float(input('Qual foi o valor que o Zezinho deu?'))
aposta3 = float(input('Qual foi o valor que a Dani deu?'))
premio  = float(input('Qual será o prêmio total?'))
aposta_total = aposta1+aposta2+aposta3
porcentagem1 = aposta1/aposta_total
porcentagem2 = aposta2/aposta_total
porcentagem3 = aposta3/aposta_total
pagamento1 = premio*porcentagem1
pagamento2 = premio*porcentagem2
pagamento3 = premio*porcentagem3

print(f"\nO primeiro investidor irá receber: {pagamento1:.2f}")
print(f'O Segundo investidor irá receber: {pagamento2:.2f}')
print(f'O terceiro investidor irá receber: {pagamento3:.2f}')























