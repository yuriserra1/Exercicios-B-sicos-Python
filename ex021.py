import pygame
pygame.init()
# Carregando o audio mp3
pygame.mixer.music.load("ex021.mp3")
# Play na musica
pygame.mixer.music.play()
input()
# Esperar a musica acabar
pygame.event.wait()
