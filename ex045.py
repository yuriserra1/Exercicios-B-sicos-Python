# Crie um programa que jogue jokenpo com voce

import sys
import random

print("-=-"*15)
print("JOGO PEDRA, PAPEL OU TESOURA")
print("-=-"*15)

print("""Escolha uma opcao: 
    [1] PEDRA
    [2] PAPEL
    [3] TESOURA """)

player = int(input("Sua opcao: "))
if player == 1:
    player = "PEDRA"

elif player == 2:
    player = "PAPEL"

elif player == 3:
    player = "TESOURA"

else:
    print("Voce nao digitou uma alternativa valida")
    print("------------------=FIM=---------------------")
    sys.exit()



lista = ["PEDRA", "PAPEL" ,"TESOURA"]
bot = random.choice(lista)

if player == bot:
    print(f""""
            O jogador escolheu {player}
          -=--=--=--=--=--=--=--=--=--=--=-
            O computador escolheu {bot} 
          -=--=--=--=--=--=--=--=--=--=--=-
            O JOGO EMPATOU!     """)
    
elif player == "PEDRA" and bot == "PAPEL":
    print(f""""
            O jogador escolheu {player}
          -=--=--=--=--=--=--=--=--=--=--=-
            O computador escolheu {bot} 
          -=--=--=--=--=--=--=--=--=--=--=-
            O Computador ganhou!     
            """)

elif player == "PEDRA" and bot == "TESOURA":
    print(f""""
            O jogador escolheu {player}
          -=--=--=--=--=--=--=--=--=--=--=-
            O computador escolheu {bot} 
          -=--=--=--=--=--=--=--=--=--=--=-
            VOCE GANHOUU!    
            """)
    
elif player == "PAPEL" and bot == "PEDRA":
    print(f""""
            O jogador escolheu {player}
          -=--=--=--=--=--=--=--=--=--=--=-
            O computador escolheu {bot} 
          -=--=--=--=--=--=--=--=--=--=--=-
            VOCE GANHOOU!     
            """)
    
elif player == "PAPEL" and bot == "TESOURA":
     print(f""""
            O jogador escolheu {player}
          -=--=--=--=--=--=--=--=--=--=--=-
            O computador escolheu {bot} 
          -=--=--=--=--=--=--=--=--=--=--=-
            O Computador ganhou!     
              """)

elif player == "TESOURA" and bot == "PEDRA":
    print(f""""
            O jogador escolheu {player}
          -=--=--=--=--=--=--=--=--=--=--=-
            O computador escolheu {bot} 
          -=--=--=--=--=--=--=--=--=--=--=-
            O Computador ganhou!     
              """)
    

elif player == "TESOURA" and bot == "PAPEL":
    print(f""""
            O jogador escolheu {player}
          -=--=--=--=--=--=--=--=--=--=--=-
            O computador escolheu {bot} 
          -=--=--=--=--=--=--=--=--=--=--=-
            VOCE GANHOOU!   
              """)

else: 
    print("ERROR")
   








