#CLOCK

import pygame 
from datetime import datetime 
 
pygame.init() 

time = datetime.now() 
second = time.second 
minute = time.minute 
 
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption('Mickey Clock')

BACK = pygame.image.load('Lab7\image\mickeyclock.jpg').convert() 
RIGHT = pygame.image.load('Lab7\image\Right.png').convert() 
LEFT = pygame.image.load('Lab7\image\left.png').convert() 
 
surf_right = pygame.Surface((900, 900)) 
surf_right.set_colorkey((0, 0, 0)) 
surf_left = pygame.Surface((900, 900)) 
surf_left.set_colorkey((0, 0, 0)) 
 
cnt = second * 6 
angle_right = second * 6 * (-1) + 54 
angle_left = minute * 6 * (-1) + 306 
 
done = True 
while done: 
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = False
            
    pygame.time.delay(1000) 
    angle_right -= 6 
    cnt += 6 
 
    screen.blit(BACK, (0, 0))
    
    screen.blit(surf_right, (0, 0)) 
    surf_right.blit(pygame.transform.rotate(RIGHT, angle_right), pygame.transform.rotate(RIGHT, angle_right).get_rect(center=(900/2, 900/2))) 
    
    screen.blit(surf_left, (0, 0)) 
    surf_left.blit(pygame.transform.rotate(LEFT, angle_left), pygame.transform.rotate(LEFT, angle_left).get_rect(center=(900/2, 900/2))) 
 
    if cnt == 360: 
        cnt = 0 
        angle_left -= 6 
     
    pygame.display.flip()  
 
pygame.quit()