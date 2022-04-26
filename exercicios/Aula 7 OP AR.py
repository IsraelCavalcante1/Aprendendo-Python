#Aula 7 - Operadores Aritméticos/Operações

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1+n2
divisao = n1/n2
subtracao = n1-n2
multiplica = n1*n2
potencia = n1**n2


print(f'O valor da soma é: {soma}' , end='')
print(f' O valor da divisão é: {divisao:.3f}' , end='')
print(f' O valor da subtração é: {subtracao} '  , end='')
print(f' O valor da multiplicação é: {multiplica} ', end='')
print(f' O valor da potência é: {potencia}', end='')
# ORDEM DE PRECEDÊNCIA
# 1 = ()
# 2 = **
# 3 = * / //%
# 4 = +-
