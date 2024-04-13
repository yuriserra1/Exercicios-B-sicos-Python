# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir
# qual foi o numero escolhido pelo computador. O programa devera escrevver na tela se o usuario venceu ou perdeu.
from random import randint
from time import sleep
print("-=-" *  15)
print("Vou pensar em um numero de 0 a 5")
print("-=-" *15)

num = randint(0 , 5)
palpite = int(input("Que numero eu pensei? "))

print("Processando...")
sleep(2)

if num == palpite:
    print("Voce ganhou, eu pensei no numero {}".format(num))
    
else: 
    print("voce perdeu, eu pensei no numero {}".format(num))
        



