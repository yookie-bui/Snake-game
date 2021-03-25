
import pygame
import random
import time
import sys


pygame.init()


(width, height) = (400,400)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake game by Yookie")
pygame.display.update()

font_style = pygame.font.SysFont(None,50)

def msg(msg,colour):
    mesg = font_style.render(msg, True, colour)
    screen.blit(mesg, [width/2, height/2])

def apple_loc(width,height,colour):
    x_a = random.randrange(0,width)
    y_a = random.randrange(0,height)
    return [x_a,y_a]

def gameLoop():
    running = True
    eaten = 0
    appear = 0
    x_snake = width/2
    y_snake = height/2
    x_change = 0
    y_change = 0

    clock = pygame.time.Clock()
    blue = (0,0,255)
    white = (255,255,255)
    red = (255,0,0)
    black = (0,0,0)
    pygame.display.update()

    apple = apple_loc(width,height,red)
    x_apple = apple[0]
    y_apple = apple[1]
    i = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    i += 1
                    x_change = -10
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    i += 1
                    x_change = +10
                    y_change = 0
                elif event.key == pygame.K_UP:
                    i += 1
                    x_change = 0
                    y_change = -10
                elif event.key == pygame.K_DOWN:
                    i += 1
                    x_change = 0
                    y_change = +10
        if x_snake >= width or x_snake < 0 or y_snake >= height or y_snake < 0:
            running == False

    #Snake movement update
        x_snake += x_change
        y_snake += y_change
        screen.fill(white)
        pygame.draw.rect(screen,blue,[x_snake,y_snake,10,10])

    #Apple
        if eaten == 0:
            pygame.draw.rect(screen,red,[x_apple,y_apple,10,10]) 
        else:
            apple = apple_loc(width,height,red)
            x_apple = apple[0]
            y_apple = apple[1]
            eaten = 0

        pygame.display.update() 
        clock.tick(10)
        if x_snake == x_apple or y_snake == y_apple:
            print('Yummy')
            eaten = 1

        if i == 10:
            eaten = 1
            i = 0
    pygame.quit()

    

gameLoop()         

