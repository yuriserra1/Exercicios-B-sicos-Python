# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faca um programa que ajude ele, lendo o nome deles a escrevendo o nome do escolhido
import random

p1 = str(input("nome do aluno 1: "))
p2 = str(input("nome do aluno 2: "))
p3 = str(input("nome do aluno 3: "))
p4 = str(input("nome do aluno 4: ")) 

lista = [p1, p2, p3, p4]
# Sortear um
sorteado = random.choice(lista)

print("o sorteado foi {}".format(sorteado))
