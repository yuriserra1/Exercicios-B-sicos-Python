# Melhore o DESAFIO 061, perguntando para o usuario se ele quer mostrar mais alguns termos. o programa
# encerrar quandl ele disse que quer mostrar 0 termos

cont = 1
pt = float(input("Digite o primeiro termo da PA: "))
r = float(input("Digite a razao da PA: "))
print(f"OS 10 primeiros termos da  P.A com a1 igual a {pt} e razao igual a {r} é:")
while cont < 11:
    pa = pt+(cont-1)*r
    print(f"A{cont} = {pa}")
    cont+=1

continuar = 1
cont= 10
while  continuar > 0 :
    continuar = int(input("Voce quer ver mais quantos termos? "))
    cont2 = 0
    if continuar > 0:
        while cont2 < continuar:
            cont2+=1
            cont+=1
            print(f"A{cont} = {pt+(cont-1)*r}") 
    else:
     print("=-="*5)
     print("     FIM     ")
     print("=-="*5)
        