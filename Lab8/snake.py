
import pygame 
from random import randrange
import time

pygame.init()


WIDTH = 700
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))     
clock = pygame.time.Clock() 
pygame.display.set_caption('Snake Game')

font_score = pygame.font.SysFont("Verdana", 25)
font_level = pygame.font.SysFont("Verdana", 25)
font_over = pygame.font.SysFont("Verdana", 40)

score = 0
level = 1
speed = 15
bonus_time = 1

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

fruit_position = [randrange(1, (WIDTH // 10)) * 10, randrange(1, (HEIGHT // 10)) * 10]
bonus_position = [randrange(1, (WIDTH // 10)) * 10, randrange(1, (HEIGHT // 10)) * 10]

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
        if score == 2 or score == 14 or score == 21 or score == 28:
            level += 1
        fruit_spawn = False
    elif snake_position[0] == bonus_position[0] and snake_position[1] == bonus_position[1]:
        score += 1
        bonus_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [randrange(1, (WIDTH // 10)) * 10, randrange(1, (HEIGHT // 10)) * 10]
    if not bonus_spawn:
        bonus_position = [randrange(1, (WIDTH // 10)) * 10, randrange(1, (HEIGHT // 10)) * 10]
        
    fruit_spawn = True
    bonus_spawn = True
    screen.fill((0, 0, 0))
    
    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    
    while score != 5:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(bonus_position[0], bonus_position[1], 10, 10))
    
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
        game_over = font_over.render(f'Game over. Your score {str(score)}', True, (255, 0, 0))
        screen.blit(game_over, (110, 300))
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
    if snake_position[1] < 0 or snake_position[1] > HEIGHT - 10:
        screen.fill((0, 0, 0))
        game_over = font_over.render(f'Game over. Your score {str(score)}', True, (255, 0, 0))
        screen.blit(game_over, (110, 300))
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over = font_over.render(f'Game over\n Your score {str(score)}', True, (255, 0, 0))
            screen.blit(game_over, (WIDTH / 2, HEIGHT / 2))
    
    clock.tick(speed)
    
    score_add = font_score.render(f'Score {str(score)}', True, (255, 255, 255))
    level_add = font_level.render(f'Level {str(level)}', True, (255, 255, 255))
    screen.blit(score_add, (20, 20))
    screen.blit(level_add, (140, 20))
            
    pygame.display.update()


pygame.quit()