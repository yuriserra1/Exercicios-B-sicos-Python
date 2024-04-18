# Faca um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.

tot=0
num = int(input("Digite um numero: "))

for x in range (1, num+1 ):
    if num % x == 0:
     print(f"\033[32m {x} \033[m", end="")
     tot +=1
    else:
     print(f"\033[31m {x} \033[m", end="")
        
print(f"""
O numero {num} foi dividido {tot} vezes""")

if tot == 2:
    print("Logo ele e um numero primo")

else:
    print("Logo ele nao e um numero primo")


        
        
        
    