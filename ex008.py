#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
metro = float(input("digite um valor em metros: "))
cent = metro*100
mili = metro*1000

print("o valor em centimetros é {} e em milimetros é {}".format(cent, mili))
