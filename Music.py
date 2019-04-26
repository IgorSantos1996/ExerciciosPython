# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
from pygame import * 
mixer.init()
mixer.music.load('teste.mp3')
mixer.music.play()
while mixer.music.get_busy():
    pause = int(input('Digite 1 para pausar e 2 para dar play: '))
    if pause == 1:
        mixer.music.pause()
    else:
        mixer.music.unpause()