'''Crie um programa onde o usuário possa
digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()). No final,mostre a lista ordenada na tela.'''

lista = list()
for c in range (0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
        print(f'Adicionado no final da lista')
    elif n > lista[len(lista)-1]:
        lista.append(n)
        print(f'Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos +=1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')