# Escreva um programa que leia um numero inteiro qualquer e peca  para o usuario escolher qual sera a base de conversao:
# 1 para binario, 2 para octal e 3 para hexadecimal.

n = int(input("Digite um numero inteiro qualquer: "))
print("Escolha a conversao: [1] para binario, [2] para octal e [3] para hexadecimal")
e = int(input("Escolha a conversao: "))

if  e == 1:
    print(f"O numero {n} em binario e igual a {bin(n)[2:]}")\

elif e == 2:
    print(f"O numero {n} em octal e igual a {oct(n)[2:]}")

elif e == 3:
    print(f"O numero {n} em hexadecimal e igual a {hex(n)[2:]}.")

else:
    print("Voce nao digitou um numero de 1 a 3")
    
print("Fim")