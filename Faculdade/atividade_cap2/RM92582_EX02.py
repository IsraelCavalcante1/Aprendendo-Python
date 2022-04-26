from time import sleep

faturamento = float(input('Qual o faturamento anual? R$ '))
plano = None

plano = int(input('Qual a sua assinatura?'
                  '\n[1] Basic'
                  '\n[2] Silver'
                  '\n[3] Gold'
                  '\n[4] Platinum\nDigite o número referente a sua assinatura: '))


print('~' * 40)
if plano == 1:
    total = (faturamento * 30 / 100)
    print(F'Você escolheu a assinatura Basic e terá que pagar 30% do total ganho.')
    print(f'Total a ser pago: R${total} e você tem o plano')
elif plano == 2:
    total = (faturamento * 20 / 100)
    print(f'Você escolheu a assinatura Silver e terá que pagar 20% do total ganho.')
    print(f'Total a ser pago: R${total}')
elif plano == 3:
    total = (faturamento * 10 / 100)
    print(f'Você escolheu a assinatura Gold e terá que pagar 10% do total ganho.')
    print(f'Total a ser pago: R${total}')
elif plano == 4:
    total = (faturamento * 5 / 100)
    print(f'Você escolheu a assinatura Platinum e terá que pagar 5% do total ganho.')
    print(f'Total a ser pago: R${total}')
else:
    print('Opção inválida')
sleep(0.5)
print('*' * 13, 'Finalizando...', '*' * 13)
