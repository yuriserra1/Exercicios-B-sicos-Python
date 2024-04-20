# Refaca o Desafio 051, lendo o primeiro termo e a razao de uma pa, mostrando os 10 primeiros termos da
# progressao usando a estrutura WHILE.

cont = 1
pt = float(input("Digite o primeiro termo da PA: "))
r = float(input("Digite a razao da PA: "))
print(f"OS 10 primeiros termos da  P.A com a1 igual a {pt} e razao igual a {r} é:")
while cont < 11:
    pa = pt+(cont-1)*r
    print(f"A{cont} = {pa}")
    cont+=1



