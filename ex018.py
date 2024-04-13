# Faca um programa que leia um angulo qualquer e mostre na tela o  valor do seno, cosseno e tangente desse angulo.
import math

angulo1 = float(input("digite um angulo seno: "))
seno = math.sin(math.radians(angulo1))
cosseno = math.cos(math.radians(angulo1))
tangente = math.tan(math.radians(angulo1))
print("O seno do angulo {} e igual a {}, o cosseno e igual a {} e a tangente e igual a {}".format(angulo1, seno, cosseno, tangente))
