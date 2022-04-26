# from time import sleep
# print('*'*13, 'Votação', '*'*13)
# segunda = int(input('Quantos votos Segunda-Feira recebeu?'))
# terca = int(input('Quantos votos Terça-Feira recebeu?'))
# quarta = int(input('Quantos votos Quarta-Feira recebeu?'))
# quinta = int(input('Quantos votos Quinta-Feira recebeu?'))
# sexta = int(input('Quantos votos Sexta-Feira recebeu?'))
# vencedor = None
# dia = ''
# print('')
# print('='*48)
# print(f'*'*13, 'Calculando Votos...', '*' * 13)
# print('='*48)
# print('')
# sleep(0.5)
# if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
#     vencedor = segunda
#     dia = 'Segunda-Feira'
#     print(f'O dia da semana com mais votos foi {dia}, com {vencedor} votos.')
# elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
#     vencedor = terca
#     dia = 'Terça-Feira'
#     print(f'O dia da semana com mais votos foi {dia}, com {vencedor} votos.')
# elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
#     vencedor = quarta
#     dia = 'Quarta-Feira'
#     print(f'O dia da semana com mais votos foi {dia}, com {vencedor} votos.')
# elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
#     vencedor = quinta
#     dia = 'Quinta-Feira'
#     print(f'O dia da semana com mais votos foi {dia}, com {vencedor} votos.')
# elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
#     vencedor = sexta
#     dia = 'Sexta-Feira'
#     print(f'O dia da semana com mais votos foi {dia}, com {vencedor} votos.')
# else:
#     print(f'Houve um empate e não foi decidido qual dia seria o vencedor.')
#
# sleep(0.5)
# print('')
# print(f'*'*13, 'Finalizando...', '*'*13)
# sleep(0.5)
#
#

print('Informe o total de votos para os respectivos dias:')

seg = int(input('SEGUNDA:'))
ter = int(input('TERÇA:'))
quar = int(input('QUARTA:'))
quin = int(input('QUINTA:'))
sex = int(input('SEXTA:'))

if seg > ter and seg > quar and seg > quin and seg > sex:
    print(f"Segunda feira teve o maior número de votos! {seg}")

elif ter > seg and ter > quar and ter > quin and ter > sex:
    print(f"Terça feira teve o maior número de votos! {ter}")

elif quar > seg and quar > ter and quar > quin and quar > sex:
    print(f"Quarta feira teve o maior número de votos! {quar}")

elif quin > seg and quin > quar and quin > sex and quin > ter:
    print(f"Quinta feira teve o maior número de votos! {quin}")

elif sex > seg and sex > quar and sex > quin and sex > ter:
    print(f'Sexta feira teve o maior número de votos! {sex}')