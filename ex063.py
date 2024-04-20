# Escreva um programa que leia um numero N inteiro qualquer e mostre na tela os N primeiros elementos
# de uma sequencia de fibonacci.

n  = int(input("Digite quantos termos deseja ver da sequencia Fibonacci: "))
cont= 3
a = 0
b = 1
c = a+b

if n == 1:
   print(a)
     
elif n == 2:
   print(a,b,)
    
elif n > 2:
   print(a, b,  end=" ")
   while cont <= n:
      print(c, end=" ")
      a = b
      b = c
      c = a+b
      cont+=1



  
  
    