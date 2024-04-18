# Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com
# a tabela abaixo:
# Abaixo de 18.5 --> abaixo do peso
# entre 18.5 - 25 --> peso ideal
# entre 25 - 30 ---> sobrepeso
# entre 30 - 40 --> obesidade
# acimda de 40 --> obesidade morbida

a = float(input("Informe sua altura em cm: "))
p = float(input("Informe seu peso em kg: "))


imc = p/((a /100)**2)
imc2 = round(imc, 2)

if imc2 < 18.5:
    print(f"Voce esta abaixo do peso, seu IMC e de {imc2}.")

elif imc2 >= 18.5 and imc2 < 25:
    print(f"Voce esta no peso ideal, seu IMC e de {imc2}")

elif imc2 >= 25 and imc2 < 30:
    print(f"Voce esta sobrepeso, seu IMC e de {imc2}")

elif imc2 >= 30 and imc2 < 40:
    print(f"Voce esta obeso, seu IMC e de {imc2}")

else:
    print(f"Voce esta com obesidade morbida, seu IMC e de {imc2}")

