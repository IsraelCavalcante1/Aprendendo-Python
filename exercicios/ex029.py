'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''


velocidade = float(input('Qual a velocidade atual do carro? '))
multa = (velocidade-80)* 7
if velocidade > 80:
    print('MULTADO! Você excedeu o limite de velocidade que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}')

else:
    print('Tenha um bom dia e dirija com cuidado!')