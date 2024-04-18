# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de 
# pagamento: - a vista dinheiro/cheque: 10% de desconto, a vista no cartao: 5% de desconto, ate 2x no cartao: sem desconto
# 3x ou mais no cartao: 20% de juros


v = float(input("Valor do produto em reais: "))

d = v*0.90
c1 = v*0.95
c2 = v
c3 = v*1.20

print("-=-"*35)
print("Forma de Pagamento: [1] dinheiro, [2] cartao em uma vez, [3] cartao em 2x e [4] cartao em 3x ou mais")
print("-=-"*35)

f = int(input("Escolha a forma de pagamento: "))

if f == 1:
    print(f"O valor a pagar e igual a {d}")

elif f == 2:
    print(f"O valor a pagar e igual a {c1} ")

elif f == 3:
    print(f"O valor a pagar e igual a {c2}")

elif f == 4:
    print(f"O valor a pagar e igual a {c3}")

else:
    print("Voce nao escolheu nenhuma forma de pagamento correspondente")
