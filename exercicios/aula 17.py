'''Aula 17 de Python: Listas'''


'''#Remover um valor da Lista:'''
# lanche = ['hamburguer', 'suco', 'pizza', 'sorvete', 'cookie']
# del lanche [3]
# lanche.pop(3)
# lanche.remove('pizza')


'''#Adicionar um valor á LISTA'''
# lanche.insert(0, 'pizza')
# lanche.append('cookie')

'''Método de verificar se o objeto está na lista para não 
apresentar erros no compilador'''

# if 'pizza' in lanche:
#     lanche.remove('pizza')
# else:
#     print(f'Pizza não está na LISTA!')

'''Criar lista através de RANGE'''

# valores = list(range(4, 11))
# valores = [8, 2, 5, 4 , 9, 3 ,0]
# valores.sort() '''# Deixar em ordem'''
# valores.sort(reverse=True) '''Ver a lista do fim ao inicio'''
# # len(valores) '''Contar quantos elementos'''

'''Teste prático'''
# num = [2, 5, 9 , 1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 2)
# if 5 in num:
#     print(f'O número 5 foi removido')
#     num.remove(5)
# else:
#     print(f'Não háo número 5 nessa lista')
# print(num)
# print(f'Essa lista tem {len(num)} elementos')
'''Como adicinar valores á lista com for e input'''
# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor inteiro: ')))
# for c, v in enumerate(valores):
#     print(f'Na posição {c+1} encontrei o valor {v}!')
# print('Cheguei ao final :D')

a = [2, 3, 4, 7]
b = a[:] # criar cópia da lista
b[2] = 8
# Python liga automaticamente as listas
print(f'Lista A: {a}')
print(f'Lista B: {b}')