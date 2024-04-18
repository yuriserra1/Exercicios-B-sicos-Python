# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o 
#valor da casa, o salario do comprador, e em quantos anos ele vai pagar.
# Calcule o valor da prestacao mensal. Sabendo que ela  nao pode exceder 30% do salario ou entao o emprestimos
# sera negado.

c = float(input("Qual o valor da casa em reais: "))
s = float(input("Qual o seu salario em reais: "))
t = float(input("Quanto tempo em meses voce ira pagar? "))

p = c / t

if p <= (30/100)* s:
    print(f"Seu emprestimo foi autorizado pelo banco e ficara no valor de {p} numa parcela de {t} vezes")
else:
    print(f"Seu emprestimo nao foi autorizado pois a prestacao no valor de {p} excede 30% do seu salario")
