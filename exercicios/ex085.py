'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''
# lista = list()
# par = list()
# impar = list()
# for c in range (0, 7):
#     valor = int(input('Digite um valor: '))
#     lista.append(valor)
# for p in lista:
#     if p % 2 == 0:
#         par.append(p)
#     elif p % 2 == 1:
#         impar.append(p)
# impar.sort()
# par.sort()
# print(f'-='* 30)
# print(f'Os valores pares em ordem crescentes são: {par}')
# print(f'Os valores ímpares em ordem crescente são: {impar}')
# print(f'-='* 30)


'''Solução alternativa com menos linha e também usando lista única com outros indices'''
num = [[], []]
valor = None
contpar = 0
contimpar = 0
for c in range (1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
        contpar += 1
    elif valor % 2 == 1:
        num[1].append(valor)
        contimpar += 1
num[0].sort()
num[1].sort()
print(num[0])
print(num[1])
print(f'Você tem no total {contpar} números pares')
print(f'Você tem no total {contimpar} números ímpares')

