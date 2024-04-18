# Escreva um programa que leia 2 numeros inteiros e compare-os, mostrando na tela uma mensagem:
# - o primeiro valor e maior
# - o segundo valor e maior
# - nao existe valor maior, os sao iguais
print("-=-"*13)
print(" COMPARE 2 NUMERO E VEJA QUAL O MAIOR")
print("-=-"*13)

n1 = int(input("digite um numero: "))
n2 = int(input("digite outo numero: "))

if n1 > n2:
    print(f"{n1} e o maior")

elif  n2 > n1:
    print(f"{n2} e o maior")

else:
    print(f"Os numeros informados sao iguais")

print("Fim") 