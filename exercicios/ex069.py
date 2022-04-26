'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar, no final mostre:

A) Quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos
'''

mulhermenor = 0
maiores = 0
homens = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]')).upper().strip()[0]
    while sexo not in 'fFMm':
        sexo = str(input('Repita seu sexo: [M/F]')).upper().strip()[0]
    escolha = str(input('Quer continuar cadastrando mais pessoas? [S/N]')).upper().strip()[0]
    while escolha not in 'SsNn':
        escolha = str(input('Quer continuar cadastrando mais pessoas? [S/N]')).upper().strip()[0]
    if idade > 18:
        maiores +=1
    if sexo in 'mM':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulhermenor += 1
    if escolha in 'nN':
        break
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulhermenor} mulheres com menos de 20 anos')
