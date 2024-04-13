# Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Mostre unidade, dezena, centena e milhar

number = int(input("Digite um numero: "))
u = number // 1 % 10
d =  number // 10 % 10
c =  number // 100 % 10
m = number // 1000 % 10
print("unidade:{}".format(u))
print("dezena:{}".format(d))
print("centena:{}".format(c))
print("milhar:{}".format(m))