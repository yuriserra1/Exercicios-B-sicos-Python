# Faca um programa que calcule a soma entre todos os numeros impares que sao multiplos de 3 e que se
# encontram no intervalo de 1 ate 500.
cont = 0
soma = 0
for x in range(1,501, 2):
    i = x % 3
    if i == 0:
        soma = soma + x 
        cont = cont + 1
print(f"A soma de todos os {cont} valores solicitados e igual a {soma}")

    
