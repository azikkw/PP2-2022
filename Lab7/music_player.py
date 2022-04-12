#MUSIC PLAYER

from secrets import choice
from textwrap import indent
import pygame 
import os 

pygame.init()


screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption('Music Player')

music_list = ['Lab7\music\Akeboshi - wind.mp3', 'Lab7\music\Feduk - Хлопья Летят Наверх.mp3']

BACK = (255, 255, 255)

"""def play(index):
    
    pygame.mixer.music.load(music_list[index])
    pygame.mixer.music.play(-1)
    
    return music_list

index = 0"""

done = True
while done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            
    screen.fill(BACK)
    
    #play(index)
    
    pygame.mixer.music.load('F:/Study/Labs/Lab7/music/Akeboshi - wind.mp3')
    pygame.mixer.music.play(-1)
            
    pygame.display.flip()
    
            
pygame.quit()