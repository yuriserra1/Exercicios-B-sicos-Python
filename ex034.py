# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# para salarios superiores a R$ 1250,00, calcule um aumento de 10%
# para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Qual o salario do funcionario em R$? "))
if salario > 1250:
    print(f"O salario é igual a {salario*1.10}")
else:
    print(f"O salario é igual a {salario*1.15}")
    