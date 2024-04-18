# Faca um programa que leia o ano de nascimento que um jovem e informe, de acordo com a sua idade:
# - se ele ainda vai se alistar ao servico militar, 
# - se e a hora de se alistar
# - se ja passou do tempo do alistamento.
# Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.

print("-=-"*20)
print("VOCE DEVE/DEVIA/DEVERA SE ALISTAR? RESPONDEREMOS A VOCE:")
print("-=-"*20)

i = int(input("Digite a sua idade: "))

if i < 18:
    print(f"Voce ainda nao chegou na idade de se alistar, faltam {18-i} anos.")

elif i > 18:
    print(f"Voce deveria ter se alistado a {i-18} ano(s) atras.")

else:
    print("Chegou a hora de se alistar voce ja tem 18 anos.")
