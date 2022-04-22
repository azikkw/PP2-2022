#MUSIC PLAYER

import pygame

pygame.init()


screen = pygame.display.set_mode((320, 450))
pygame.display.set_caption('Music Player')
screen.fill((255, 255, 255))

music_list = [
    r"Lab7\music\Akeboshi - wind.mp3",
    r"Lab7\music\Feduk - Хлопья Летят Наверх.mp3",
    r"Lab7\music\MONATIK - Сильно.mp3",
    r"Lab7\music\piano - senbonzakura (maximp3.ru).mp3"
    ]

image_list = [
    r"Lab7\image\wind.jpg",
    r"Lab7\image\feduk.jpg",
    r"Lab7\image\monatik.jpg",
    r"Lab7\image\senbonzakura.jpg"
    ]
    
index = 0
volume = 0.5

image = pygame.image.load(image_list[index])
screen.blit(image, (10, 10))

pygame.mixer.music.load(music_list[index])
pygame.mixer.music.play()


done = True
while done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            
        if event.type == pygame.KEYUP and event.key == pygame.K_LCTRL:
            pygame.mixer.music.pause()
            
        if event.type == pygame.KEYUP and event.key == pygame.K_LALT:
            pygame.mixer.music.unpause()
            
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            if index <= 3:
                index += 1
            else:
                index = 0
                
            image = pygame.image.load(image_list[index])
            screen.blit(image, (10, 10))
            
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_list[index])
            pygame.mixer.music.play()
            
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            if index >= 0:
                index -= 1
            else:
                index = 4
                
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_list[index])
            pygame.mixer.music.play()
            
            image = pygame.image.load(image_list[index])
            screen.blit(image, (10, 10))
            
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            volume += 0.1
            pygame.mixer.music.set_volume(volume)
            
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            volume -= 0.1
            pygame.mixer.music.set_volume(volume)
            
    #screen.blit(image, (10, 10))
    
    pygame.draw.ellipse(screen, (0, 0, 0), (130, 350, 60, 60))
    pygame.draw.polygon(screen, (255, 255, 255), [(153, 368), (153, 392), (170, 380)], 0)
    
    pygame.draw.polygon(screen, (0, 0, 0), [(213, 368), (213, 392), (230, 380)], 0)
    pygame.draw.lines(screen, (0, 0, 0), False, [[230, 371], [230, 390]], 3)
    
    pygame.draw.polygon(screen, (0, 0, 0), [(103, 368), (86, 380), (103, 392)], 0)
    pygame.draw.lines(screen, (0, 0, 0), False, [[86, 371], [86, 390]], 3)
    
    
    pygame.display.flip()