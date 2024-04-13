#Faca um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input("digite um valor: "))
ant = num-1
suce = num+1
print("o antecessor do numero {} é o numero {} e seu sucessor é o {}".format(num, ant, suce))