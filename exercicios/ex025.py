'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome'''


nome = str(input('Qual o seu nome?')).strip()


print(f'Essa pessoa tem Silva no nome? {"SILVA" in nome.upper() }' )
