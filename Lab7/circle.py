#DRAW CIRCLE GAME

import pygame
import sys


#CIRCLE OPTIONS
class DrawCircle():
    
    def __init__(self, screen): #Settings for circle view and motion
        self.screen = screen
        
        self.x = 300
        self.y = 300
        self.r = 25
        
        self.color = (255, 0, 0)
        
        self.motion_x_r = False
        self.motion_x_l = False
        self.motion_y_t = False
        self.motion_y_b = False
        
        
    def output(self): #For circle output
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        
        
    def motion(self): #For circle motion
        if self.motion_x_r and self.x < 570:
            self.x += 5
        if self.motion_x_l and self.x > 30:
            self.x -= 5
        if self.motion_y_t and self.y > 30:
            self.y -= 5
        if self.motion_y_b and self.y < 570:
            self.y += 5


    def events(self): #For events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()    
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:         
                    self.motion_y_t = True
                if event.key == pygame.K_DOWN:
                    self.motion_y_b = True
                if event.key == pygame.K_RIGHT:
                    self.motion_x_r = True
                if event.key == pygame.K_LEFT:
                    self.motion_x_l = True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:         
                    self.motion_y_t = False
                if event.key == pygame.K_DOWN:
                    self.motion_y_b = False
                if event.key == pygame.K_RIGHT:
                    self.motion_x_r = False
                if event.key == pygame.K_LEFT:
                    self.motion_x_l = False
                

#GAME RUN FUNCTION
def run():
    
    pygame.init()
    
    #Display options
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Draw Circle')
    clock = pygame.time.Clock()
    
    #Circle
    circle = DrawCircle(screen)
    
    #COLORS
    background_color = (255, 255, 255)
    
    #Endless loop for the game
    while True:
        screen.fill(background_color)
        
        circle.events()
        circle.motion()
        circle.output()
        
        pygame.display.flip()
        
        clock.tick(60)

run()