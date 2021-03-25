
import pygame
import random
import time
import sys


pygame.init()

#GLOBAL VARIABLES
BLUE = (0,0,255)
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
(WIDTH, HEIGHT) = (400,400)

#SCREEN AND CAPTION SETUP
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake game by Yookie")
pygame.display.update()

font_style = pygame.font.SysFont(None,50)

def msg(msg):
    mesg = font_style.render(msg, True, BLUE)
    screen.blit(mesg, [WIDTH/2, HEIGHT/2])

def apple_loc():
    x_a = random.randrange(10,WIDTH-10)
    y_a = random.randrange(10,HEIGHT-10)
    return [x_a,y_a]

def gameLoop():
    running = True
    eaten = 0
    appear = 0
    x_snake = WIDTH/2
    y_snake = HEIGHT/2
    x_change = 0
    y_change = 0

    clock = pygame.time.Clock()
    pygame.display.update()

    apple = apple_loc()
    x_apple = apple[0]
    y_apple = apple[1]
    snake_head = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = +10
                    y_change = 0
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -10
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = +10 

        if x_snake >= WIDTH or x_snake < 0 or y_snake >= HEIGHT or y_snake < 0:
            running == False

    #Snake movement update
        x_snake += x_change
        y_snake += y_change
        screen.fill(WHITE)
        pygame.draw.rect(screen,BLUE,[x_snake,y_snake,20,20])

    #Apple
        if eaten == 0:
            pygame.draw.rect(screen,RED,[x_apple,y_apple,10,10]) 
        else:
            apple = apple_loc()
            x_apple = apple[0]
            y_apple = apple[1]
            eaten = 0
  
        

        pygame.display.update() 
        clock.tick(10)
        snake = pygame.Rect(x_snake,y_snake,20,20)
        apple_a = pygame.Rect(x_apple,y_apple,10,10)
        
        if snake.colliderect(apple_a):
            print('Yummy')
            eaten = 1

    pygame.quit()

    

gameLoop()         

