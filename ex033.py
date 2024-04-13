# Faça um programa que leia 3 numeros e diga qual é o maior e qual é o menor
n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))

if n1 < n2 and n1 < n3:
    print(f"{n1} é o menor")
elif n2<n1 and n2<n3:
    print(f"{n2} é o menor")
elif n3<n1 and n3<n2:
    print(f"{n3} é o menor")
elif n1 == n2 and n1 < n3:
    print (f"{n1} é o menor") 
elif n2 == n3 and n2 < n1:
    print (f"{n2} é o menor") 
elif n1 == n3 and n1 < n2:
    print(f"{n1} é o menor")
else:
    print("Os numeros sao iguais")
    
if n1>n2 and n1>n3:
    print(f"{n1} é o maior")
elif n2>n1 and n2>n3:
    print(f"{n2} é o maior")
elif n3>n1 and n3>n2:
    print(f"{n3} é o maior")
elif n1 == n2 and n1 > n3:
    print (f"{n1} é o maior") 
elif n2 == n3 and n2 > n1:
    print (f"{n2} é o maior") 
elif n1 == n3 and n1 > n2:
    print(f"{n1} é o maior")

print("FIM")
    