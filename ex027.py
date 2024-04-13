# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# ex: Ana maria de Souza ==> primeiro: Ana / utimo = Souza

nome = str(input("digite o seu nome completo: ")).strip()
nome = nome.split() 

print("Seu primeiro nome é: {}".format(nome[0]))

# # Len conta o total de numeros a partir do numero 1 e o index começa a partir do 0, entao logo, (len-1) = ultimo index.
print("Seu ultimo nome é: {}".format(nome[len(nome)-1]))

#Tambem podemos utilizar o [-1] como ultimo objeto de uma lista e [-2] o penultimo e assim por diante.
#seguindo essa logica o codigo ficaria assim:
# nome = str(input("digite o seu nome completo: "))
# nome = nome.split()
# print(f"Seu primeiro nome é {nome[0]} e seu ultimo nome é {nome[-1]}")