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

bg_x = 0
player_anim_count = 0
player_speed = 5
player_x = 150
player_y = 250
is_jump = False
jump_count = 7

bg_sound.play()

running = True
while running:
    KeyPressed = pygame.key.get_pressed()
    screen.blit(bg,(bg_x, 0))
    screen.blit(bg, (bg_x + 800, 0))

    if KeyPressed[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))

    if KeyPressed[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    elif KeyPressed[pygame.K_RIGHT] and player_x < 750:
        player_x += player_speed

    if not is_jump:
        if KeyPressed[pygame.K_UP]:
            is_jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 7

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







