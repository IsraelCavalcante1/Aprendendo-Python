# Faça um programa que calcule o valor de um aluguel de carro.
# Você deverá ler a quantidade de dias que o carro foi alugado e a quantidade de quilometros rodados.
# Para cada dia, será cobrado o valor de 60 reais
# Para cada km será cobrado 15 centavos.


dias = int(input('Quantos dias o carro foi alugado? '))
km   = float(input('Quantos kilometros foi rodado?'))
vd   = dias*60
kmr  = km*0.15
val  = vd+kmr


print(f'O valor total a ser pago é de: {val} ')







