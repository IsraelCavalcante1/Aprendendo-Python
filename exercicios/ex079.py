''' Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos
os valores únicos digitados, em ordem crescente'''

números = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print(f'Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não será adicionado.')
    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if r in 'Nn':
        break

print('-=' * 30)
print(f'Você digitou os valores {números.sort()}')
