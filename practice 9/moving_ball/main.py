import pygame
from ball import Ball

pygame.init()
W, H = 800, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
ball = Ball(W, H)

running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    ball.move(keys)
    ball.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit() 