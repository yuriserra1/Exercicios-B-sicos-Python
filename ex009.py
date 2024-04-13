#faca um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada.
cont = 1
num = int(input("digite um numero: "))
while cont < 11:
    tabuada = num *cont
    print("{} x {} é = {}".format(num, cont, tabuada))
    cont = cont + 1
