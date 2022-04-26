from time import sleep

maior = None  # Aqui armazenará os votos do maior número
dia = ''  # Aqui armazenará o dia que ganhou com mais votos
valor = None  # Aqui amarzenará o input com os votos
diasSemana = ['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira',
              'Sexta-Feira']  # Lista com os dias da semana

for cont in range(0, 5):  # Laço de repetição para comparar qual o maior e qual dia da semana é
    valor = int(input(f'Quantos votos tiveram a {diasSemana[cont]}: '))  # Input com os votos
    if maior is None or valor > maior:  # Código para saber qual dia da semana recebeu mais votos, ou seja, qual o maior
        maior = valor  # Maior recebe o valor com mais votos
        dia = diasSemana[cont]  # Identifica qual foi o dia com maior
sleep(0.5)
print('*' * 30)
print(f'Calculando os votos...')
print('*' * 30)
sleep(0.5)
print(f'O dia com mais votos foi a {dia}, com {maior} votos. ')
sleep(0.5)
print(f'*' * 13, 'Finalizando...', '*' * 13)
