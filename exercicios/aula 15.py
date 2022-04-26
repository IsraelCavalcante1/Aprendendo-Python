# cont = 1
# while True:
#     print(cont, '-> ', end='')
#     cont += 1
# print('Acabou')
n = 0
cont = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n


print(f'A soma vale {s}')

