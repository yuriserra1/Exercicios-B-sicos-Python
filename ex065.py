# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execucao, mostre a media
# entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario
# se ele quer ou nao continuar a digitar valores.
num = soma = maior = menor = 0
cont = 0
c = "s"
n = "n"
num = int(input("Digite um valor: "))  
if num > maior and num > menor:
        maior = num
        menor = num
while c != n:
    soma+=num
    c = str(input("Deseja digitar outro numero? ")).lower().strip()[0]
    if c == "s":
        num = int(input("Digite um valor: "))  
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    cont+=1
media = (soma/cont)
if cont == 1 and maior == menor:
    print(f"Voce digitou {cont} numero a media ficou {media} e nesse caso nao temos um numero maior ou menor.")  
elif maior == menor:
   print(f"Voce digitou {cont} numeros a media ficou {media} e nesse caso nao temos um numero maior ou menor.") 
else: 
    print(f"Voce digitou {cont} numeros a media ficou {media}, sendo o maior digitado {maior} e o menor digitado {menor}.")



