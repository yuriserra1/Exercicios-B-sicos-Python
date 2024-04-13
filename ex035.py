# Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou nao formar um triangulo.
# Para um triangulo existir a+b > c // a+c > b // b+c > a

r1 = float(input("Digite um valor para reta: "))
r2 = float(input("Digite um valor para reta: "))
r3 = float(input("Digite um valor para reta: "))

if  (r1+r2) > r3 and (r1+r3) > r2 and  (r2+r3) > r1:
    print("Esses valores de reta podem formar um triangulo")
else:
    print("Esses valores nao podem formar um triangulo")
    