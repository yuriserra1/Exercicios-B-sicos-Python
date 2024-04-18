# Crie um programa que leia uma frase qualquer e diga se ela e um palindromo, desconsiderando os espacos.
# EX: APOS A SOPA

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ""

for x in range(len(junto) - 1, -1, -1):
    inverso += junto[x]

if inverso == junto:
    print(f"O inverso de {junto} e {inverso} logo, e um palindromo.")

else:
    print(f"O inverso de {junto} e {inverso} logo, nao e um palindromo.")
    