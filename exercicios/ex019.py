# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome delas e escrevendo o nome do escolhido
'''import random
a1 = input('Qual o nome do primeiro aluno? ') #
a2 = input('Qual o nome do segundo aluno?')
a3 = input('Qual o nome do terceiro aluno?')
a4 = input('Qual o nome do quarto aluno?')
sort = random.randint (1, 4)



if sort == 1:
    print(f'Quem apagará o quadro é o: {a1}!')

elif sort == 2:
    print(f'Quem apagará o quadro é o: {a2}!  ')

elif sort == 3:
    print(f'Quem apagará o quadro é o: {a3}!')

elif sort == 4:
    print(f'Quem apagará' o quadro é o: {a4}!')'


#A maneira acima é a que tentei fazer por conta própria, ela saiu de forma mais complexa do que o necessário'''

import random

a1 = input('Qual o nome do primeiro aluno? ') #
a2 = input('Qual o nome do segundo aluno?')
a3 = input('Qual o nome do terceiro aluno?')
a4 = input('Qual o nome do quarto aluno?')
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)

print(f'O escolhido foi {escolhido}')

'''Essa foi a forma proposta pelo professor, sendo a mais prática. Ela foi proposta pois ainda não apareceu else/if no curso'''