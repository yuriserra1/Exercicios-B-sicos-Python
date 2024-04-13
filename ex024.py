# Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "santo".
# primeiro passo: criar um input com o nome cidade
# segundo passo: a gente pode .lower para deixar tudo em minusculo
# terceiro passo: criar uma lista com 1 indice chamado "santo"
# #quarto passo: cidade= cidade[0:5] ou seja vai mostrar o index: [0, 1, 2, 3, 4]
# quinto passo: usar if e o else 
# printar se começar ou nao com santo.
lista = ["santo"]
cidade = str(input("Qual o nome da sua cidade: ")).strip()
cidade = cidade.lower()
cidade = cidade[0:5]

if lista[0] == cidade[0:5]:
    print("A sua cidade começa com a palavra Santo")
else:
    print(" A sua cidade nao começa com a palavra Santo")