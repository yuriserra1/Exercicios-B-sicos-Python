# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar, [2] multiplicar, [3] maior, [4] novos numeros, [5] sair do programa
# seu programa devera realizar a operaçao solcitada em cada caso

valor1 = int(input("Digite um numero: "))
valor2 = int(input("Digite outro numero: "))
    
escolha = 0
while escolha != 5:
    print("""Escolha uma opção:
          [1] Somar
          [2] multiplicar
          [3] maior
          [4] novos numeros
          [5] sair do programa""")
    escolha = int(input("Escolha: "))
    if escolha == 1:
        soma = valor1+valor2
        print(f"A soma entre {valor1} e o {valor2} é igual a {soma}.")
    elif escolha == 2:
        mult = valor1*valor2
        print(f"O resultado da multiplicacao entre o {valor1} e o {valor2} é igual a {mult}.")
    elif escolha == 3:
        if valor1 > valor2:
            print(f"O numero {valor1} é maior que o {valor2}.")
        elif valor2 > valor1:
            print(f"O numero {valor2} é maior que o {valor1}.")
        else:
            print(f"O numero {valor1} é igual ao {valor2}.")
    elif escolha == 4:
        valor1 = int(input("Digite um novo valor: "))
        valor2 = int(input("Digite outro novo valor: "))
    elif escolha == 5:
        print("Voce finalizou o programa até a proxima!")
        break
    else:
       print("Voce nao digitou nenhuma alternativa valida.")
    