
import pygame
import random
import time
import sys
import numpy as np

pygame.init()

#GLOBAL VARIABLES
BLUE = (0,0,255)
WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
(WIDTH, HEIGHT) = (800,600)

#SCREEN AND CAPTION SETUP
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake game by Yookie")
pygame.display.update()

font_style = pygame.font.SysFont('bahnschrift',25)
score_font = pygame.font.SysFont('comicsansms',35)

def msg(msg,colour):
    mesg = font_style.render(msg, True, colour)
    screen.blit(mesg, [WIDTH/5, HEIGHT/2])

def apple_loc():
    x_a = random.randrange(10,WIDTH-10)
    y_a = random.randrange(10,HEIGHT-10)
    return [x_a,y_a]

def draw_snake(snake_head):
    for head in snake_head:
        x = head[0]
        y = head[1]
        pygame.draw.rect(screen, BLUE, [x,y,20,20])

def draw_score(score):
    score = score_font.render("Score: " + str(score),True, BLUE)
    screen.blit(score, [0,10])

def gameLoop():
    running = True
    closing = False

    started = 0   
    eaten = 0
    score = 0

    x_snake = WIDTH/2
    y_snake = HEIGHT/2
    x_change = 0
    y_change = 0
    snake_head = []
    snake_length = 1

    apple = apple_loc()
    x_apple = apple[0]
    y_apple = apple[1]

    clock = pygame.time.Clock()

    while running:
        #End screen
        while closing == True:
            screen.fill(BLACK)
            msg('Press Q to quit or R to reset the game', RED)
            draw_score(score)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        closing = False
                    if event.key == pygame.K_r:
                        gameLoop()
        #Welcome text
        if started == 0:
            screen.fill(BLACK)
            msg('WELCOME TO SNAKE. PRESS S KEY TO START',WHITE)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        started = 1
            pygame.time.wait(1000)
        else:
        #Snake control
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

            if x_snake >= WIDTH or x_snake < 0 or y_snake >= HEIGHT or y_snake < 0: #game ends when snake run out of screen
                closing = True
                print(closing)

        #Snake movement and snake length update
            x_snake += x_change
            y_snake += y_change
            screen.fill(BLACK)
            draw_snake(snake_head)

            head_pos = []
            head_pos.append(x_snake)
            head_pos.append(y_snake)
            snake_head.append([x_snake,y_snake])
            if len(snake_head) > snake_length:
                del snake_head[0]

            for part in snake_head[:-1]: #snake eats itself
                if part == head_pos:
                    closing = True

        #Generating apple
            if eaten == 0:
                pygame.draw.rect(screen,RED,[x_apple,y_apple,10,10]) 
            else:
                snake_length += 1
                apple = apple_loc()
                x_apple = apple[0]
                y_apple = apple[1]
                eaten = 0

            draw_score(score)
            pygame.display.update() 
            clock.tick(30)

        #Snake and apple collision
            snake = pygame.Rect(x_snake,y_snake,20,20)
            apple_a = pygame.Rect(x_apple,y_apple,10,10)
            
            if snake.colliderect(apple_a):
                score += 1
                eaten = 1
                apple = apple_loc()
                x_apple = apple[0]
                y_apple = apple[1]

    pygame.quit()
    quit()
    
if __name__ == "__main__":
    gameLoop()         



