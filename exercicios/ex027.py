'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
o primeiro e o último nome separadamente'''


nome = str(input('Qual o seu nome?')).strip()
separação = nome.split()
# primeiro_nome = (separação[0])
# ultimo_nome = separação[]

print('Muito prazer em te conhecer...')
print(f'O seu primeiro nome é: {separação[0]}')
print(f'O seu último nome é: {separação[len(separação)-1]}') #Aqui é para adquirir a última partição da string
