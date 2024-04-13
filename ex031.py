# Desenvolva um programa que pergunte a distancia de uma viagem KM. Calcule o preço da passagem cobrando
# R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.
print("PREÇO DA PASSAGEM")
print("-=-"*10)
distancia = int(input("Digite uma distancia em KM/H: "))

if distancia <= 200:
    print(f"O preço da passagem é igual a R${distancia*0.50}")
else:
    print(f"O preço da passagem é igual a R${distancia*0.40}")
    