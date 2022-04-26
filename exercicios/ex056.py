# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

from datetime import date
atual = date.today().year

mulher = 0 # Variável para identificar quantas mulheres há
somaidade = 0 # Soma da idade recebida no laço for
médiaidade = 0 # Aqui fazemos a divisão pelas 4 pessoas, para tirarmos a média de idade
maioridadehomem = 0 # Aqui pegamos a maior idade identificada no laço for (contanto que seja homem)
nomevelho = '' # Aqui atribuimos o valor identificado no homem mais velho e colocamos a variável "nome" dentro dela
menoridade = 0 # Menor idade das mulheres para identificar quais tem menos de 20 anos
for p in range (1, 5):
    nome = str(input(f'Qual o nome da {p} pessoa: ')).strip()
    idade = int(input(f'Qual a idade da {p} pessoa: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm': #Identificar qual o homem mais velho, assim atribuindo a idade e o nome
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff':   # Quantas mulheres tem e quantas são menores de 20 anos
        mulher += 1
    if sexo in 'Ff' and idade < 20: # Identificar quantas mulheres tem menos de 20 anos
        menoridade += 1



médiaidade = somaidade / 4 # média de idade

print(f'A média de idade do grupo é de {médiaidade}')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Existem {menoridade} mulheres menores de 20 anos')
