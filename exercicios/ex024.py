'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO'''

cidade = str(input('Qual o nome da sua cidade? ')).strip()
dividido = cidade.split()
dividido2 = (dividido[0])


print(cidade[0:5].upper() == 'SANTO')
