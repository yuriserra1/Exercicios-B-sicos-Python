# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daquelas que forem pares.
# Se o valor digitado for impar, desconsidere-o.

soma= 0
for x in range(1, 7):
    n1 = int(input(f"Digite o valor {x}: "))
    if n1% 2 == 0:
        soma = soma + n1
print(f"A soma dos numeros pares informados e igual a {soma}")
