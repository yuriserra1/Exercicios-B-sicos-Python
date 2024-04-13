# Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e o mostre o comprimento da hipotenusa. (PITAGORAS)
import math
cateto1 = float(input("Digite um valor para o cateto oposto: "))
cateto2 = float(input("Digite um valor para o cateto adjacente: "))
hipotenusa = math.hypot(cateto1, cateto2)
print("a hipotenusa do triangulo retangulo e igual a {}".format(hipotenusa))
