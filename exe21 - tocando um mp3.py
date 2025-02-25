#Faça um programa em Python que abra e reproduza o áudio
#de um arquivo mp3. (módulos)
import pygame
pygame.mixer.init() #isso é para iniciar o pygame
pygame.mixer.music.load (filename = ("C:\\Users\\David Alexandre\\Music\\iTunes\\iTunes Media\\Music\\Evanescence\\The Open Door\\04 Lithium.mp3"))
pygame.mixer_music.play()
input()
pygame.event.wait()

#esse código só vai rodar em arquivos mp3!!!
#na linha 5, pode ser:
#pygame.mixer.music.load ('') (apenas o nome do arquivo que está na pasta (sem caracteres especiais))
#o código acima, está rodando, mas ele podia acabar na linha 7, trocando ela pela 8.