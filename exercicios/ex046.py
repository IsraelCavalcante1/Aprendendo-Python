#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# om uma pausa de 1 segundo entre eles.
import time

print('-=' * 4,'a contagem regressiva vai começar','-=' * 4)
for c in range (10, -1, -1):
    print(c)
    time.sleep(1)
print('-=' * 10)
print(f'BUM!  BUM! POOOW!')
print('-=' * 10)