# Faca um programa que leia o sexo de uma pessoa, mas so aceite os valores "M" ou
# "F". Caso esteja errado, peça a digitaçao novamente ate ter um valor correto.

M = "Masculino"
F = "Feminino"
sexo = str(input("Digite o seu sexo M/F: ")).upper().strip()[0]
while sexo != "M" and sexo != "F" :
    sexo = str(input("Dados invalidos, digite novamente o seu sexo: ")).upper().strip()[0]
print("Seu cadastro foi realizado com sucesso.")
print("-=-"*5)
print("FIM")
print("-=-"*5)