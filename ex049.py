# Refaca o desafio 009, mostrando a tabuada de um numero que o usuario escolher, so que agora 
# utilizando um laco for.

num = int(input("digite um numero: "))
for x in range (1, 11):
    tabuada = num * x
    print(F"{num} X {x} = {tabuada}")

   
