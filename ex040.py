# Crie um programa que leia duas notas de um aluno e calcule sua media, mostrrando uma mensagem no
# final  de acordo com a media atingida
# media abaixo de 5: reprovado
# media entre 5 e 6.9: recuperacao
# media 7 ou superior: aprovado
print("-=-"*10)
print("CALCULADO DE MEDIA")
print("-=-"*10)

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 1: "))

m = (n1 + n2) / 2

if m < 5.0:
    print(f"Voce ficou com media {m} e foi reprovado.")

elif m > 5.0 and m < 6.9:
    print(f"Voce ficou com a media {m} e ficou em recuperacao.")

elif  m >= 7.0:
    print(f"Voce ficou com a media {m} e esta aprovado.")

else: 
   print(f"Voce ficou com a media {m} e ficou em recuperacao.")