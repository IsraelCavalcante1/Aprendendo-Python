# # A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
# # de acordo com a idade:
#
# – Até 9 anos: MIRIM
#
# – Até 14 anos: INFANTIL
#
# – Até 19 anos: JÚNIOR
#
# – Até 25 anos: SÊNIOR
#
# – Acima de 25 anos: MASTER

from datetime import date
ano_nascimento = int(input('Qual a sua data de nascimento? '))
atual = date.today().year
idade = atual - ano_nascimento

if idade <= 9:
    print(f'Parabéns, você tem {idade} anos e está na categoria MIRIM')
elif idade >= 10 and idade <= 14:
    print(f'Parabéns, você tem {idade} anos e está na categoria INFANTIL')
elif idade >= 15 and idade <=19:
    print(f'Parabéns, você tem {idade} anos e está na categoria JÚNIOR')
elif idade >= 20 and idade <=25:
    print(f'Parabéns, você tem {idade} anos e está na categoria SÊNIOR ')
elif idade >= 26:
    print(f'Parabéns, você tem {idade} anos e está na categoria MASTER')


'''Maneira exemplificada'''
# if idade <= 9:
#     print(f'Parabéns, você tem {idade} anos e está na categoria MIRIM')
# elif idade <=14:
#     print(f'Parabéns, você tem {idade} anos e está na categoria INFANTIL')
# elif idade <=19:
#     print(f'Parabéns, você tem {idade} anos e está na categoria JÚNIOR')
# elif idade <=25:
#     print(f'Parabéns, você tem {idade} anos e está na categoria SÊNIOR ')
# elif idade >= 25:
#     print(f'Parabéns, você tem {idade} anos e está na categoria MASTER')