# Faca um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
# indo de 10 ate 0, com uma pausa de 1 segundo entre eles.

import time

for t in range(10, -1, -1):
    time.sleep(1)
    print(t)
    if t == 0:
        break

