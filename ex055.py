# Faca um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
menor = 0
maior= 0
for p in range(1, 6):
    peso = float(input(f"digite o peso {p} em kilogramas: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
    
print(f"O maior peso foi {maior} kg e o menor peso foi {menor} kg")