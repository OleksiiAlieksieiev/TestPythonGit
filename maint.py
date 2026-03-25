import pygame
from pygame import K_SPACE

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("... under construction.")

bg = pygame.image.load('srcs/bg.jpg')
bg_sound = pygame.mixer.Sound('Srcs/Sounds/scotland_theme.mp3')

walk_left =[
    pygame.image.load('srcs/PlayerLeft/left1.png'),
    pygame.image.load('srcs/PlayerLeft/left2.png'),
    pygame.image.load('srcs/PlayerLeft/left3.png'),
    pygame.image.load('srcs/PlayerLeft/left4.png')
]
walk_right =[
    pygame.image.load('srcs/PlayerRight/right1.png'),
    pygame.image.load('srcs/PlayerRight/right2.png'),
    pygame.image.load('srcs/PlayerRight/right3.png'),
    pygame.image.load('srcs/PlayerRight/right4.png')
]
player_anim_count = 0
bg_x = 0

bg_sound.play()

running = True
while running:

    screen.blit(bg,(bg_x, 0))
    screen.blit(bg, (bg_x + 800, 0))

    screen.blit(walk_right[player_anim_count], (350, 250))

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                screen.fill((0, 200, 0))

    bg_x -= 2
    if bg_x == -800:
        bg_x = 0

    clock.tick(15)







