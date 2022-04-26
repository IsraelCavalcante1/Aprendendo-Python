# for c in range(0, 7 , 3):
#     print(c)
# print('fim')

####### chegando até o número capturado pela variável
# n = int(input('Digite um número: '))
# for c in range(0, n+1):
#     print(c)
# print('fim')


# i = int(input('Início: ')) #INÍCIO QUE COMEÇARA A CONTAGEM
# f = int(input('Fim: ')) # QUANTOS NÚMEROS SERÁ CONTADO
# p = int(input('Passo: ')) # QUANTOS NÚMEROS IRÁ PULAR
# for c in range (i, f+1, p): #apenas coloque as variáveis acima na posição correta
#     print(c) #estou chamando a variável da repetição
# print('FIM')
s = 0
for c in range(0, 3): #capturar a variável mais de uma vez, pois está dentro da estrutura de repetição
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi: {s}')