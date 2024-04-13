# O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalhos dos alunos. faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

p1 = str(input("nome do aluno 1: "))
p2 = str(input("nome do aluno 2: "))
p3 = str(input("nome do aluno 3: "))
p4 = str(input("nome do aluno 4: "))

lista = [p1, p2, p3, p4]
# Embaralhar a lista
random.shuffle(lista)
print(" A ordem de apresentacao sera: {}:".format(lista))
