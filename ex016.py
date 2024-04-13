# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porcao inteira.
import math

valor1 = float(input("digite um numero: "))
valor2 = math.floor(valor1)
print("o numero {} tem a parte inteira {}".format(valor1, valor2))