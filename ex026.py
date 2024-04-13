# Faca um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# em que posiçao ela aparece a primeira vez
# Em que posição ela aparece a ultima vez

frase = str(input("digite uma frase: ")).strip()
frase = frase.lower()
contar = frase.count("a")
primeira = frase.find("a")
ultima = frase.rfind("a")

print("Na frase temos um total de {} a".format(contar))
print("o primeiro a aparece na posição {}".format(primeira))
print("o último a aparece na posição {}".format(ultima))