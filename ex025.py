# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
lista = ["SILVA"]
nome = str(input("digite seu nome completo: ")).strip()
nome = nome.upper()
verdade = "SILVA" in nome  #operador do python que confere se tem "SILVA" no nome. 
if verdade == True:
    print("Seu nome contém Silva")
else:
    print("Seu nome nao contém Silva")