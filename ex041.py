# A confederacao Nacional de Natacao precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - ate 9 ano: Mirim // - ate 14 anos: infantil // ate 19 anos: junior // ate 20 anos: senior // acima: < master

print("-=-"*20)
print("LER O ANO DE NASCIMENTO DE UM ATLETA E INFORME A CATEGORIA: ")
print("-=-"*20)

i = int(input("Digite a sua idade: "))

if i <= 9:
    print("Categoria Mirim")

elif i > 9 and i <= 14:
    print("Categoria Infantil")

elif i > 14 and i <= 19:
    print("Categortia Junior")

elif i > 19 and i <= 20:
    print("Categoria Senior")

else: 
    print("Categoria Master")

