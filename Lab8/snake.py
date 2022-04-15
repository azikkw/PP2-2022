#SNAKE GAME

from itertools import count
import pygame
from random import randint, randrange

pygame.init()

BACK = pygame.image.load("Lab8/image/grass.png")
WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))     
clock = pygame.time.Clock() 
pygame.display.set_caption('Snake Game')

font_score = pygame.font.SysFont("Verdana", 30)
font_level = pygame.font.SysFont("Verdana", 30)


class Snake(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Lab8/image/snake.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 80)
        
    def update(self):
        
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.y > 100:
            if pressed_keys[pygame.K_UP]:
                self.rect.y -= 7
        if self.rect.y < HEIGHT - 90:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.y += 7
        if self.rect.x > 10:
            if pressed_keys[pygame.K_LEFT]:
                pygame.transform.rotate(self.image, -90)
                self.rect.x -= 7
        if self.rect.x < WIDTH - 40:        
              if pressed_keys[pygame.K_RIGHT]:
                self.rect.x += 7   
                
    def draw(self, surface):
        surface.blit(self.image, self.rect) 

class Apple(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Lab8/image/apple.png")
        self.rect = self.image.get_rect()
        
    def reset_pos(self):
        self.rect.x = randrange(WIDTH - 80)
        self.rect.y = randrange(80, HEIGHT)

snake = Snake()

apples = pygame.sprite.Group()

score, level = 0, 0

for i in range(10):
    apple = Apple()
    apple.rect.x = randrange(WIDTH - 80)
    apple.rect.y = randrange(80, HEIGHT)
    apples.add(apple)
    
    if i == 0:
        apple.reset_pos()
         

done = True
while done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            
    screen.blit(BACK, (0, 0))
    clock.tick(60)
    
    point_add = pygame.sprite.spritecollide(snake, apples, True)
    
    score_add = font_score.render(str(score), True, (0, 0, 0))
    level_add = font_score.render(f'Level {str(level)}', True, (0, 0, 0))
    screen.blit(score_add, (20, 20))
    screen.blit(level_add, (80, 20))
    
    for i in point_add:
        apple.reset_pos()
        score += 1
        if score == 4:
            level += 1
    
    apples.draw(screen)
    snake.update()
    snake.draw(screen)
    
    pygame.display.update()
    
            
pygame.quit()