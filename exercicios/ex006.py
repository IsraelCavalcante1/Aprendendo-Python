#Leia um valor e calcule seu dobro, o triplo e a raiz. Depois exiba os valores na tela
import math

n1 = int(input('Digite um número: ' ))
dobro = n1*2
triplo = n1*3
raiz = n1**(1/2)

#print(f'O dobro do número digitado é: {dobro}')
#print(f'O triplo do número digitado é: {triplo}')
#print(f'A raiz do número digitado é: {raiz}')

print(
f'''O dobro do número digitado é: {dobro}
O triplo do número digitado é: {triplo}
A raiz do número digitado é: {raiz:.2f}''')



#print('isso é um \nteste') quebrar linha