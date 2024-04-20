# Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario 
#digitar o valor "999", que e a condicao de parada. No final, mostre quantos numeros foram digitados e
# qual foi a soma entre eles (desonsiderando o flag).

n = soma = cont = 0
n = int(input("Digite um numero [999 para parar]: "))
while n != 999:
    soma+= n
    cont+=1
    n = int(input("Digite um numero [999 para parar]: "))
print(f"O total de numeros digitados foi {cont} e a soma de todos os numeros desconsiderando o flag foi {soma}")
