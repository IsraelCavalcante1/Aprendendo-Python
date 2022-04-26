''': Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
 (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário
 receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade,
 com quantos anos a pessoa vai se aposentar.
'''
from datetime import datetime
pessoa = dict()
pessoa['seu nome'] = str(input('Digite seu nome: '))
pessoa['nascimento'] = int(input('Qual a sua data de nascimento? '))
pessoa['ctps'] = int(input('Digite sua carteira de trabalho: [Digite 0 se você não tem]'))
pessoa['sua idade'] = datetime.now().year - pessoa['nascimento']
del pessoa['nascimento']
print('=-'*10,'Informações trabalho: ' ,'=-'*10)
if pessoa['ctps'] == 0:
    print('Você não tem carteira de trabalho')
    del pessoa['ctps']
else:
    pessoa['contratação'] = int(input('Digite seu ano de contratação: '))
    pessoa['salário'] = float(input('Salário R$'))
    pessoa['aposentadoria'] = pessoa['sua idade'] + pessoa['contratação'] + 35 - datetime.now().year
print(f'=-'*10, 'Informações Pessoais', f'=-'*10)
for k, v in pessoa.items():
    print(f'{k} é {v}')
print(f'=-'*10, 'Fim', f'=-'*10)





