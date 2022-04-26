'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''


lista = list()
listapar = list()
listaimpar = list()

while True:
    lista.append(int(input(f'Digite um número: ')))
    resp = str(input(f'Você quer continuar? [S/N] ')).upper().strip()[0]
    if resp not in 'sSnN':
        resp = str(input(f'Opção inválida, digite novamente: [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break
for par in lista:
    if par % 2 == 0:
        listapar.append(par)
    elif par % 2 == 1:
        listaimpar.append(par)

print(f'-='*30)
print(f'A sua lista completa é: {lista}')
print(f'A sua lista de números pares é {listapar}')
print(f'A sua lista de números ímpares é {listaimpar}')
print(f'-='*30)


