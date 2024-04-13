#crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
num = int(input("digite um numero:"))
dobro = num*2
triplo = num*3
raiz = num**(1/2)

print("o dobro do numero {} é {}, o triplo é {} e a raiz quadrada  é {}".format(num, dobro, triplo, raiz))