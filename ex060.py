# Faça um programa que leia um numero qualquer e mostre seu fatorial.

print("Fatorial de um numero")

num = int(input("Digite um numero: "))
c = num
f = 1
print(f"Calculando {num}!= ", end="")
while c > 0:
    print(c, end="")
    print( " x " if c>1 else " = ", end="")
    f*= c
    c-= 1
    
print(f, end="")     