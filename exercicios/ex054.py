##Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1, 8):
    nascimento = int(input(f'Em que ano a {pess} pessoa nasceu? '))
    idade = atual - nascimento
    print(f'Essa pessoa tem {idade} anos')
    if idade >= 21:
       totmaior += 1
    else:
        totmenor += 1
print(f'Existem {totmenor} pessoas que ainda não atingiram a maioridade')
print(f'Existem {totmaior} pessoas que já atingiram a maioridade')
