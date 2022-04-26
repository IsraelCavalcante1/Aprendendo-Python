'''Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores 'M' ou 'F'. Caso esteja errado
peça a digitação novamente até ter um valor correto'''

sexo = str(input('Você é homem ou mulher? [M/F]: ')).upper().strip()[0]


while sexo != 'M' and sexo != 'F':
    sexo = str(input('Você digitou algo errado, informe novamente [M/F]')).upper().strip() [0]
    if sexo != 'M' and sexo != 'F':
        print('Você digitou algo incorreto, tente novamente: ')
if sexo == 'F':
    print('Seu sexo foi registrado com sucesso e você é mulher.')
if sexo == 'M':
    print('Seu sexo foi registrado com sucesso e você é homem.')

#Acima foi minha solução



# sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
# while sexo not in ('MmFf'):
#     sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
# print(f'Sexo {sexo} registrado com sucesso! ')
#
# #Essa foi a do professor