#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento


salario = int(input('Qual o salário atual?'))
aumento = salario + (salario * 15/ 100)


print(f'O salário é de: R${salario:.2f} e com aumento ficará R${aumento:.2f}')


