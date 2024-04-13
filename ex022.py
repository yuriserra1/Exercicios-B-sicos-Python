# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1) O nome com todas as letras maiusculas
# 2) O nome com todas minusculas
# 3) quantas letras ao todo (sem considerar espaços)
# 4) quantas letras tem o primeiro nome.

name = str(input("Qual é seu nome completo? ")).strip()  # .strip para eliminar os espaços desnecessarios.
print("Seu nome em maiusculo é {}".format(name.upper))   # .upper para deixar as letras maiusculas.
print("Seu nome em minusculo é {}".format(name.lower))   # .lower para deixar as letras minusculas.
print("Seu nome tem {} letras".format(len(name)-name.count(" ")))   # len() para ler toda a variavel, -.count( " ") para eliminar os espaços.
print("O seu primeiro nome tem {} letras".format(name.find(" ")))   # .find (" ") conta do indice 0 até o indice especificado nos () -1.