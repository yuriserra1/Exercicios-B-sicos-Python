#Faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quant. de tinta para pinta-la. Cada litro de tinta pinta uma area de 2m ao quadrado
base = float(input("digite a largura em metros da parede: "))
altura = float(input("digite a altura em metros da parede: "))
area = base*altura
tinta = area / 2

print("A area total da parede é igual a {}m² e o total de tinta necessario para pintar a parede é igual a {}L".format(area, tinta))