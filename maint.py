import pygame
from pygame import K_SPACE

pygame.init()

icon = pygame.image.load('srcs/building_test.png')
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((800, 300))
pygame.display.set_caption("... under construction.")

square = pygame.Surface((150, 150))
square.fill ("magenta")

running = True
while running:

    pygame.draw.circle(screen, 'yellow', (100, 75), 50)
    screen.blit(square,(100, 100))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                screen.fill((0, 200, 0))
            elif event.key == pygame.K_r:
                screen.fill((200, 0, 0))
            elif event.key == pygame.K_b:
                screen.fill((0, 0, 200))
            elif event.key == K_SPACE:
                screen.fill((200, 200, 200))







