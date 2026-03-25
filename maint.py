import pygame
#from pygame import K_SPACE

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 450))
pygame.display.set_caption("... under construction.")

bg_sound = pygame.mixer.Sound('Srcs/Sounds/scotland_theme.mp3')
bg = pygame.image.load('srcs/bg_tal.png').convert_alpha()

walk_left =[
    pygame.image.load('srcs/PlayerLeft/pll1.png').convert_alpha(),
    pygame.image.load('srcs/PlayerLeft/pll2.png').convert_alpha(),
    pygame.image.load('srcs/PlayerLeft/pll3.png').convert_alpha(),
    pygame.image.load('srcs/PlayerLeft/pll4.png').convert_alpha()
]
walk_right =[
    pygame.image.load('srcs/PlayerRight/plr1.png').convert_alpha(),
    pygame.image.load('srcs/PlayerRight/plr2.png').convert_alpha(),
    pygame.image.load('srcs/PlayerRight/plr3.png').convert_alpha(),
    pygame.image.load('srcs/PlayerRight/plr4.png').convert_alpha()
]

enemy = pygame.image.load('Srcs/Dron64.png').convert_alpha()
enemy_list_in_game = []

bg_x = 0
player_anim_count = 0
player_speed = 5
player_x = 150
player_y = 250
is_jump = False
jump_count = 10

bg_sound.play()
enemy_timer = pygame.USEREVENT + 1  # always +1
pygame.time.set_timer(enemy_timer, 5000)    # every 5 sec

running = True
while running:
    KeyPressed = pygame.key.get_pressed()
    screen.blit(bg,(bg_x, 0))
    screen.blit(bg, (bg_x + 800, 0))

    player_rect = walk_left[0].get_rect(topleft = (player_x, player_y)) #kwargs player

    if enemy_list_in_game:
        for elm in enemy_list_in_game:
            screen.blit(enemy, elm)
            elm.x -= 10

            if player_rect.colliderect(elm):
                pygame.display.set_caption("You lost...")
                # end the game
                running = False
                pygame.quit()

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
        if jump_count >= -10:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    bg_x -= 2
    if bg_x == -800:
        bg_x = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == enemy_timer:
            enemy_list_in_game.append(enemy.get_rect(topleft = (810, 250)))

    clock.tick(15)







