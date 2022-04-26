'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''
import sys
import emoji




# print('=' * 4,'Lojas Adocicadas', "=" * 4)
print(f'{" Lojas Adocicadas ":=^40}')

produto = float(input('Qual o valor do produto R$ '))

print(f'''Você quer pagar como?
[ 1 ] Á vista 10% de desconto
[ 2 ] Á vista no Cartão de Crédito
[ 3 ] Em 2x no Cartão de Crédito, sem juros
[ 4 ] Em 3x no Cartão de Crédito, com 20% de de juros''')

opção = int(input('Escolha uma opção acima: '))
# desconto10 = produto - (produto * 10 / 100)
# desconto5 = produto - (produto * 5 / 100)
# juros20 = (produto * 20 / 100) + produto


if opção == 1:
    total = produto - (produto * 10 / 100)
    print(f'Com esse método de pagamento você terá 10% de desconto e o total ficará R${total:.2f}')

elif opção == 2:
    total = produto - (produto * 5 / 100)
    print(f'Com esse método de pagamento você terá 5% de desconto e o total ficará R${total:.2f}')


elif opção == 3:
    parcela = produto / 2
    print(f'Sua compra será parcelada em 2x sem juros')
    print(f'As parcelas são de R${parcela:.2f} e o total ficará R${produto:.2f}')
elif opção == 4:
    total = produto + (produto * 20 / 100)
    totalp = float(input('Você deseja fazer em quantas parcelas?'))
    parcela = (total / totalp)
    print(f'Você parcelará em {totalp:.0f}x e as parcelas será de R${parcela:.2f}')
else:
    (print(f'Essa opção é inválida seu imbecil! '))
# elif opção == 3:
#     print(f'Com esse método de pagamento você pagará o valor integral do produto e ficará R${produto:.2f}')
# elif opção == 4:
#     print(f'Com esse método de pagamento você deverá pagar o produto com 20% de juros e ficará R${juros20:.2f}')
#
# else:
#     print(f'Essa opção é inválida seu imbecil! ')
#
print(f'''Deseja continuar?
[ 1 ] Sim
[ 2 ] Não
[ 3 ] Voltar ''')
opção2 = int(input('Escolha uma das opções acima: '))

if opção2 == 1:
    print (emoji.emojize('Obrigado pela compra, volte sempre!! :red_heart:'))
elif opção2 == 2:
    print(f'Voltando para o menu inicial...')





