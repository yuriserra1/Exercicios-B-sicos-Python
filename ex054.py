# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
# nao atingiram a maioridade e quantas ja sao maiores de idade.

maior= 0
menor= 0
for x in range(1, 8):
    ano = int(input(f"digite o ano de nascimento {x}: "))
    if ano <= 2006:
        maior += 1
    else:
        menor += 1
    
print(f"Ha {maior} maiores de idade e {menor} menores de idade")

