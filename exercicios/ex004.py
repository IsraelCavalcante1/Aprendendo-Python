#Dissecando uma variável

algo = input ('Digite algo a ser dissecado: ')
print('O tipo primitivo desse valor é ', type(algo))
print('Só tem espaços? ', algo.isspace())
print('É maiúsculo? ', algo.isupper())
print('É um número? ', algo.isnumeric())
print('Contém letras ou números? ', algo.isalnum())
print('É alfabético? ', algo.isalpha())
print('Está em minúsculas? ', algo.islower())
print('Está capitalizada? ', algo.istitle())
