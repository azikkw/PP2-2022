

import pygame 
from random import randrange
import time

pygame.init()


WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))     
clock = pygame.time.Clock() 
pygame.display.set_caption('Snake Game')

font_score = pygame.font.SysFont("Verdana", 25)
font_level = pygame.font.SysFont("Verdana", 25)
font_over = pygame.font.SysFont("Verdana", 40)

score = 0
level = 1
speed = 15

colors = [(255, 255, 0), 
          (0, 255, 0), 
          (0, 255, 255), 
          (255, 0, 255), 
          (200, 0, 100), 
          (70, 70, 70), 
          (0, 0, 255)
        ]

snake_position = [130, 100]
snake_body = [  [130, 100],
                [120, 100],
                [110, 100],
                [100, 100]
            ]

direction = 'RIGHT'
change_to = direction

fruit_position = [randrange(1, (WIDTH // 10)) * 10 - 10, randrange(1, (HEIGHT // 10)) * 10]
bonus_position = [randrange(1, (WIDTH // 10)) * 10 - 10, randrange(1, (HEIGHT // 10)) * 10]

fruit_spawn = True
bonus_spawn = True

done = True
while done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
        
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 1
        fruit_spawn = False
        if score == 5 or score == 10 or score == 15 or score == 20:
            level += 1
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [randrange(1, (WIDTH // 10)) * 10, randrange(1, (HEIGHT // 10)) * 10]
        
    fruit_spawn = True
    screen.fill((0, 0, 0))
    
    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    
    if level == 2:
        speed = 20
    elif level == 3:
        speed = 25
    elif level == 4:
        speed = 30
    elif level == 5:
        speed = 35
    
    if snake_position[0] < 0 or snake_position[0] > WIDTH - 10:
        screen.fill((0, 0, 0))
        game_over = font_over.render(f'GAME OVER, TRY AGAIN', True, (255, 0, 0))
        screen.blit(game_over, (50, 250))
        pygame.display.flip()
        time.sleep(2)
        done = False
    if snake_position[1] < 0 or snake_position[1] > HEIGHT - 10:
        screen.fill((0, 0, 0))
        game_over = font_over.render(f'GAME OVER, TRY AGAIN', True, (255, 0, 0))
        screen.blit(game_over, (50, 250))
        pygame.display.flip()
        time.sleep(2)
        done = False
        
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            screen.fill((0, 0, 0))
            game_over = font_over.render(f'GAME OVER, TRY AGAIN', True, (255, 0, 0))
            screen.blit(game_over, (50, 250))
            pygame.display.flip()
            time.sleep(2)
            done = False
    
    clock.tick(speed)
    
    score_add = font_score.render(f'Score {str(score)}', True, (255, 255, 255))
    level_add = font_level.render(f'Level {str(level)}', True, (255, 255, 255))
    screen.blit(score_add, (20, 20))
    screen.blit(level_add, (140, 20))
            
    pygame.display.update()