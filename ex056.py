# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A media de idade do grupo / qual e o nome do homem mais velho. / quantas mulheres tem menos de 20 anos
nome_maior_idade = ""
maiormasc = 0
cont1 = 0
cont2 = 0
soma = 0
somamasc = 0
for x in range(1, 5):
     nome = str(input(f"Digite o nome {x}: "))
     idade = int(input(f"Digite a idade {x}: "))
     sexo = str(input(f"Digite o sexo {x}: ")).lower()
     if idade > maiormasc and sexo == "masculino":
         maiormasc = idade
         nome_maior_idade = nome
     if sexo == "masculino":
         somamasc += idade
         cont1+= 1
     soma+= idade
     if idade < 20 and sexo == "feminino":
         cont2+= 1
mediamasculina = (somamasc / cont1)
mediatot = (soma / 4)
if mediamasculina == maiormasc:
 print(f"""A media de idade do grupo e de {mediatot} anos, nao tem o nome do homem mais velho pois a maior
 idade masculina condiz a mais de uma pessoa e ha {cont2} mulheres com menos de 20 anos.""")
else:
 print(f"""A media de idade do grupo e de {mediatot} anos, O nome masculino mais velho e {nome_maior_idade} e 
 ha {cont2} mulheres com menos de 20 anos.""")



