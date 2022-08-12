# faça um programa em python que abra e reproduza o áudio de um arquivo mp3

import pygame
pygame.mixer.init() # iniciando o mixer pygame
pygame.init() # iniciando o pygame em si
pygame.mixer.music.load('ex021.mp3') # escolhendo o arquivo - para utilizar assim o arquivo e o mp3 precisam estar na mesma pasta
pygame.mixer.music.play() # dar play no arquivo
pygame.event.wait() # esperar o arquivo tocar para finalizar
