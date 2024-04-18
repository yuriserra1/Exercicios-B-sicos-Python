# Refazer o desafio 35 so que dizendo o tipo do triangulo.


r1 = float(input("Digite um valor para reta: "))
r2 = float(input("Digite um valor para reta: "))
r3 = float(input("Digite um valor para reta: "))

if  (r1+r2) > r3 and (r1+r3) > r2 and  (r2+r3) > r1 and r1 == r2 == r3:
    print("Esses valores de reta podem formar um triangulo, e forma um do tipo equilatero")
elif (r1+r2) > r3 and (r1+r3) > r2 and  (r2+r3) > r1 and (r1 == r2 != r3 or r3 == r1 != r2 or r2 == r3 != r1):
    print("Esses valores de reta podem formar um triangulo, e forma um do tipo isosceles")

elif (r1+r2) > r3 and (r1+r3) > r2 and  (r2+r3) > r1 and r1 != r2 != r3:
    print("Esses valores de reta podem formar um triangulo, e forma um do tipo escaleno")

else:
    print("Esses valores de reta nao podem formar um triangulo")