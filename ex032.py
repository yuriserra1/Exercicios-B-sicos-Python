# Faça um programa que leia um ano e diga se ele é BISSEXTO.
ano = int(input("Digite um ano: "))

if (ano % 4) == 0:
    print(f"O {ano} é bissexto")
else:
    print(f"O {ano} nao é bissexto")