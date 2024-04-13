#Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis.
algo = input("digite algo: ")
if algo.isnumeric():
    print("{} e do tipo primitivo numerico".format(algo))
elif algo.isalpha():
    print("{} e do tipo primitivo alfabetico".format(algo))
else:
    print("{} e do tipo primitivo alfanumerico".format(algo))