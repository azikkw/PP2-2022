import pygame, sys
from random import randrange
import time
from add_user import add_user
from show_score import show_score

    
print("Please state your name:")
user_name = input()

file = open('users.txt', 'r')
users_list = [line.strip() for line in file]
cnt = 0
for user in users_list:
    if user_name == user:
        cnt += 1

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Snake Game')

font_score = pygame.font.SysFont("Verdana", 25)
pause_txt = pygame.font.SysFont("Verdana", 28)
font_level = pygame.font.SysFont("Verdana", 25)
font_over = pygame.font.SysFont("Verdana", 40)
for_exit = pygame.font.SysFont("Verdana", 20)
            
score = 0
level = 1
speed = 15

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
done = True


def pause():
    
    paused = True
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                if event.key == pygame.K_RETURN:
                    add_user(user_name, str(level), str(score))
                    pygame.quit()
                    quit()
                    
        screen.fill((255, 255, 255))
        general = pause_txt.render(f'Paused. Press ESC to continue!', True, (0, 0, 0))
        level_now = font_level.render(f'Level {str(level)}', True, (0, 0, 0))
        score_now = font_score.render(f'Score {str(score)}', True, (0, 0, 0))
        to_exit1 = for_exit.render(f'If you want to QUIT from game and', True, (255, 0, 0))
        to_exit2 = for_exit.render(f'save your results press ENTER!', True, (255, 0, 0))
        screen.blit(general, (82, 210))
        screen.blit(level_now, (190, 260))
        screen.blit(score_now, (310, 260))
        screen.blit(to_exit1, (117, 360))
        screen.blit(to_exit2, (139, 385))
        
        pygame.display.flip()
        

if cnt != 1:
    with open('users.txt', 'a') as f:
        f.write(f'{user_name}\n')
    
    while done:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                add_user(user_name, str(level), str(score))
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
                if event.key == pygame.K_ESCAPE:
                    pause()
            

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
            if score == 5 or score == 10 or score == 15 or score == 20 or score == 30:
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
        elif level == 6:
            add_user(user_name, 'max', 'max')
            screen.fill((0, 0, 0))
            game_over = font_over.render(f'YOU WIN', True, (255, 0, 0))
            screen.blit(game_over, (220, 250))
            pygame.display.flip()
            time.sleep(2)
            done = False
        
        if snake_position[0] < 0 or snake_position[0] > WIDTH - 10:
            add_user(user_name, str(level), str(score))
            screen.fill((0, 0, 0))
            game_over = font_over.render(f'GAME OVER, TRY AGAIN', True, (255, 0, 0))
            screen.blit(game_over, (50, 250))
            pygame.display.flip()
            time.sleep(2)
            done = False
        if snake_position[1] < 0 or snake_position[1] > HEIGHT - 10:
            add_user(user_name, str(level), str(score))
            screen.fill((0, 0, 0))
            game_over = font_over.render(f'GAME OVER, TRY AGAIN', True, (255, 0, 0))
            screen.blit(game_over, (50, 250))
            pygame.display.flip()
            time.sleep(2)
            done = False
            
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                add_user(user_name, str(level), str(score))
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
                
        pygame.display.flip()

else:
    print(f'\nTHIS NAME HAS ALREADY BEEN SELECTED:')
    show_score(user_name)
    
    
pygame.quit()