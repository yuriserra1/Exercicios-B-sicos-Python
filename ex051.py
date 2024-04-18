# Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10
# primeiros termos dessa progressao.

pt = float(input("Digite o primeiro termo da PA: "))
r = float(input("Digite a razao da PA: "))

for x in range(1,11):
    pa =  pt +(x-1)*r
    print(round(pa, 2))