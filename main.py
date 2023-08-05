import pygame
from pygame.locals import *

pygame.init() #initialised the pygame

screen_width = 780
screen_height = 820

screen = pygame.display.set_mode((screen_width,screen_height))  #game window
pygame.display.set_caption("flappy bird")


# define varible
ground_scroll = 0
scroll_speed = 4
clock = pygame.time.Clock()
fps = 60

#load images
bg = pygame.image.load('D:/tanishq/CODING/Flappy Bird/fbg.png')
ground = pygame.image.load('D:/tanishq/CODING/Flappy Bird/ground.png')
run = True

#RUNNING

while run:

    clock.tick(fps)

    #this is bg setting

    screen.blit(bg, (0,0))

    #groung img
    screen.blit(ground, (ground_scroll,768))
    ground_scroll -= scroll_speed
    for event in pygame.event.get(): # will get all the events that are happening
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update() 

pygame.quit

