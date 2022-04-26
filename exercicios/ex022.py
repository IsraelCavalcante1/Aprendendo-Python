'''Crie um programa que leia o nome completo de uma pessoa e mostre:
> o nome com todas as letras maiúsculas
> o nome com todas minúsculas
> quantas letras ao todo (sem considerar espaços)
> quantas letras tem o primeiro nome'''

nome = str(input('Qual o seu nome? ')).strip()
separa = nome.split()

print(f'Analisando o seu nome...')
print(f'O seu nome em letras maiúsculas é: {nome.upper()}')
print(f'O seu nome em letras minúsculas é: {nome.lower()}')
print (f'O seu nome contém ao todo: ',len(nome.replace(' ','')))
print(f'O seu primeiro nome é: {separa[0]} e contém {len(separa[0])} letras')





