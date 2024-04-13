#Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80 km/h. mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.
print
print("Velocidade do Carro")
velocidade = int(input("Digite uma velocidade em KM/H: "))
limite = (velocidade - 80)*7
if velocidade > 80:
    print("Voce foi multado")
    print(f"A sua multa ficou no valor de R${limite}")
else:
    print("Voce nao foi multado")