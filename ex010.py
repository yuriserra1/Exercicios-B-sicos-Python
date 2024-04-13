#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. considere U$ 1,00 = R$ 5,00
dinheiro = float(input("Total de dinheiro em reais na carteira: "))
total_em_dolar = dinheiro / 5
print("Com R${} voce podera comprar U${}".format(dinheiro, total_em_dolar))