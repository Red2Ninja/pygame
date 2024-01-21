import pygame
import random

pygame.init()

screen_width = 1000
screen_height = 500

background_image = pygame.image.load("assets/background.png").convert()
background_image = pygame.tranform.scale(background_image,(screen_width,screen_height))


screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Realm Quest")

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background_image,(0,0))
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()
