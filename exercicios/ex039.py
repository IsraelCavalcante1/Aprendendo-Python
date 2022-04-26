'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''


from datetime import date
atual = date.today().year # Linha para pegar a data atual
nasc = int(input('Qual o seu ano de nascimento? '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')

if idade == 18:
    print(f'Você deve se ALISTAR esse ANO!')

elif idade < 18:
    saldo = 18 - idade # pegar quantos anos falta para 18
    ano = atual + saldo # fala o ano que a pessoa terá que se alistar
    print(f'Você ainda não tem 18 anos. Ainda falta {saldo} anos para o alistamento')
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    saldo = idade - 18 # quantos anos se passaram desde os 18 anos da pessoa
    ano = atual - saldo # Fala em que ano foi o alistamento da pessoa ou que deveria ter sido
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    print(f'Seu alistamento foi em {ano}')


