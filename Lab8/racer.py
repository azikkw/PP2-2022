#RACER GAME

import pygame 
from random import randint

pygame.init()


BACK = pygame.image.load("Lab8/image/road.png")
WIDTH = 500
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))     
clock = pygame.time.Clock() 
pygame.display.set_caption('Racer Game')

font_score = pygame.font.SysFont("Verdana", 40)
    
pygame.mixer.music.load('Lab8/music/music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)


class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Lab8/image/player_car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 80)
        
    def update(self):
        
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.x > 0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.x -= 7
        if self.rect.x < WIDTH - 115:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.x += 7
        

class Coin(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Lab8/image/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(40, WIDTH - 40), 0)
        
    def reset_pos(self):
        self.rect.y = 0
        self.rect.x = randint(40, WIDTH - 40)
        
    def update(self):
        self.rect.y += 7
        if self.rect.y > 800:
            self.reset_pos()
                    
P1 = Player()
C1 = Coin()

coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(C1)

score = 0


done = True
while done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            
    screen.blit(BACK, (0, 0))
    clock.tick(60)
    
    for i in all_sprites:
        screen.blit(i.image, i.rect)
        i.update()
    
    point_add = pygame.sprite.spritecollide(P1, coins, False)
    score_add = font_score.render(str(score), True, (255, 255, 255))
    screen.blit(score_add, (245, 20))
    
    for i in point_add:
        C1.reset_pos()
        score += 1
        pygame.mixer.Sound('Lab8/music/coin.mp3').play()
    
    pygame.display.update()
    
            
pygame.quit()