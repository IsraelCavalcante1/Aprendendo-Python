# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#
# – Média abaixo de 5.0: REPROVADO
#
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
#
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Qual a sua primeira nota? '))
nota2 = float(input('Qual a sua segunda nota? '))
média = (nota1+nota2) / 2

if média < 5.0 :
    print(f'Sua média é {média} e você foi REPROVADO! Estude um pouco mais da próxima.')

elif média => 5.0 and média < 6.9:
    print(f'Sua média é {média} e você estará de recuperação nos próximos dias.')

elif média >= 7:
    print(f'Sua média é {média} e você foi APROVADO.')