'''Nessa aula, vamos aprender o que são funções ou rotinas e como utilizar funções em Python.
Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
Veja como funciona o comando def em Python e como utilizá-lo
com parâmetros simples e múltiplos.'''

# def soma(a, b):
#     s = a + b
#     print(s)
#
# # Programa Principal
# soma(4, 5)
# soma(8, 9)
# soma(2, 1)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)