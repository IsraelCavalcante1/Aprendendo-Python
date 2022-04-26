from time import sleep
somaCalorias = 0
print(f'*' * 13, 'Calculadora de Calorias', '*' * 13)
alimentos = int(input('Informe quantos alimentos foram ingeridos: '))
for i in range(alimentos):
    calorias = int(input(f'Quantas calorias tinha o {i + 1}° alimento? '))
    somaCalorias += calorias
print(f'Você ingeriu {alimentos} alimentos e somando seu valor energético, foram {somaCalorias} calorias. ')
sleep(0.5)
print('*' * 13, 'Finalizando...', '*' * 13)
