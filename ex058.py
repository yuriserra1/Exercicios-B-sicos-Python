#Melhore o jogo 028 onde o computador vai "pensar" em um numero de 0 e 10. so que agora o jogador vai tentar adivinhar ate certar.
# mostrando no final quantos palpites foram necessarios para  vencer.
from random import randint
from time import sleep
print("-=-" *  15)
print("Vou pensar em um numero de 0 a 10")
print("-=-" *15)

num = randint(0 , 10)
palpite = int(input("Que numero eu pensei? "))

print("Processando...")
sleep(1.5)
cont = 1
while num != palpite:
    palpite = int(input("Voce errou, digite outro numero de 0 a 10: "))
    cont+= 1
    print("Processando...")
    sleep(1.5)

print(f"Voce acertou! o numero era {num} porém voce precisou de {cont} tentativas para acertar")


