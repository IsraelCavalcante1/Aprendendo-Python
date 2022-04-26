nome = str(input('Qual é seu nome? '))
if nome == 'Leonardo':
    print('Que nome lindo!')

elif nome == 'Pedro' or nome == 'Luana' or nome == 'Paulo':

    print(f'Seu nome é bem popular no Brasil! ')


elif nome in 'Ana Cláudia Jéssica Juliana':

    print(f'Belo nome feminino! ')

else:
    print(f'Você tem um nome bem normal {nome} ! ')
