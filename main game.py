import pygame  # pygame module
import ctypes  # module for getting users data

def on_platform(player_rect):
    return ground_right > player_rect.centerx > ground_left

def animation():
    global player1_surf,player_index, left
    if keys[pygame.K_a]:
        left = True
    elif keys[pygame.K_d]:
        left = False

    if player1_inair: # Jump
        player_index += 0.03
        if player_index >= len(jump_list): player_index = 0
        player1_surf = jump_list[int(player_index)]

    elif player1_running: # Run
        player_index += 0.16
        if player_index >= len(run_list): player_index = 0
        player1_surf = run_list[int(player_index)]

    elif player1_rect.bottom == ground_height: # Idle
        player_index += 0.07
        if player_index >= len(idle_list): player_index = 0
        player1_surf = idle_list[int(player_index)]


    if left:
        player1_surf = pygame.transform.flip(player1_surf, True, False)
    else:
        player1_surf = pygame.transform.flip(player1_surf, False, False)
user32 = ctypes.windll.user32  # get width and height of the window

pygame.init()
# Succesful start ->

screen_size = [
    user32.GetSystemMetrics(0),  # width
    user32.GetSystemMetrics(1)   # height
]
screen = pygame.display.set_mode(
    screen_size,          # size of the window
    pygame.FULLSCREEN     # fullscreen setup
)

pygame.display.set_caption(
    "1v1 GAME"  # title
)

clock = pygame.time.Clock()
game_active = False
step_size = 7
player1_falling = False
player1_inair = False
player1_running = False
left = False
play_button_size = 0.8

player_font = pygame.font.SysFont("comicsans", 50, True)
button_font = pygame.font.SysFont("comicsans", 100, True)

player1_text = player_font.render("P1", True, "blue")

""" Ground """
ground_height = screen_size[1] - 88
ground_surf = pygame.transform.scale_by(
    pygame.image.load("graphics/ground.png"),  # image url
    1                                        # scale
)
ground_rect = ground_surf.get_rect(midtop=(
    screen_size[0]//2,
    ground_height - 32)
)
ground_left = screen_size[0] // 2 - ground_rect.width // 2
ground_right = screen_size[0] // 2 + ground_rect.width // 2


run0 = pygame.transform.scale_by(pygame.image.load("graphics/player/run/adventurer-run-00.png"), 4)
run1 = pygame.transform.scale_by(pygame.image.load("graphics/player/run/adventurer-run-01.png"), 4)
run2 = pygame.transform.scale_by(pygame.image.load("graphics/player/run/adventurer-run-02.png"), 4)
run3 = pygame.transform.scale_by(pygame.image.load("graphics/player/run/adventurer-run-03.png"), 4)
run4 = pygame.transform.scale_by(pygame.image.load("graphics/player/run/adventurer-run-04.png"), 4)
run5 = pygame.transform.scale_by(pygame.image.load("graphics/player/run/adventurer-run-05.png"), 4)
run_list = [run0, run1, run2, run3, run4, run5]

idle0 = pygame.transform.scale_by(pygame.image.load("graphics/player/idle/adventurer-idle-00.png"), 4)
idle1 = pygame.transform.scale_by(pygame.image.load("graphics/player/idle/adventurer-idle-01.png"), 4)
idle2 = pygame.transform.scale_by(pygame.image.load("graphics/player/idle/adventurer-idle-02.png"), 4)
idle3 = pygame.transform.scale_by(pygame.image.load("graphics/player/idle/adventurer-idle-03.png"), 4)
idle_list = [idle0, idle1, idle2, idle3]

jump0 = pygame.transform.scale_by(pygame.image.load("graphics/player/jump/adventurer-jump-00.png"), 4)
jump1 = pygame.transform.scale_by(pygame.image.load("graphics/player/jump/adventurer-jump-01.png"), 4)
jump2 = pygame.transform.scale_by(pygame.image.load("graphics/player/jump/adventurer-jump-02.png"), 4)
jump3 = pygame.transform.scale_by(pygame.image.load("graphics/player/jump/adventurer-jump-03.png"), 4)
jump_list = [jump2, jump3]

player_index = 0
player1_gravitation = 0
player1_surf = pygame.transform.scale_by(pygame.image.load("graphics/player/run/adventurer-run-00.png"), 4)
player1_rect = player1_surf.get_rect(midbottom=(screen_size[0]//4, ground_height))

exit_button_surf = pygame.transform.scale_by(pygame.image.load("graphics/exit_button.png"), 0.04)
exit_button_rect = exit_button_surf.get_rect(topright=(screen_size[0] - 40, 40))

play_button_surf = pygame.transform.scale_by(pygame.image.load("graphics/play.png"), play_button_size)
play_button_rect = play_button_surf.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_active:
                if event.key == pygame.K_w and player1_rect.bottom == ground_height and on_platform(player1_rect):
                    player1_gravitation = -21

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_active:
                if play_button_rect.collidepoint(mouse_pos):
                    game_active = True
            if exit_button_rect.collidepoint(mouse_pos):
                running = False


    screen.fill("white")
    keys = pygame.key.get_pressed()

    if game_active:
        if keys[pygame.K_a]:
            player1_rect.x -= step_size
            player1_running = True
        elif keys[pygame.K_d]:
            player1_rect.x += step_size
            player1_running = True
        else:
            player1_running = False

        player1_gravitation += 10 * 0.08
        player1_rect.y += player1_gravitation

        if ground_height < player1_rect.bottom and on_platform(player1_rect) and not player1_falling:
            player1_rect.bottom = ground_height
            player1_gravitation = 0

        if not on_platform(player1_rect) or player1_rect.bottom < ground_height:
            player1_inair = True
        else:
            player1_inair = False

        if ground_height < player1_rect.bottom:
            player1_falling = True
        else:
            player1_falling = False

        if player1_rect.top > screen_size[1]: # Death
            player1_rect.midbottom = (screen_size[0] // 2, ground_height - player1_gravitation)
            player1_falling = False
            game_active = False

        player1_text_rect = player1_text.get_rect(midbottom=(player1_rect.centerx, player1_rect.top + 10))

        screen.blit(ground_surf, ground_rect)
        animation()
        screen.blit(player1_surf, player1_rect)
        screen.blit(player1_text, player1_text_rect)

    else:
        play_button_surf = pygame.transform.scale_by(pygame.image.load("graphics/play.png"), play_button_size)
        play_button_rect = play_button_surf.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))

        screen.blit(play_button_surf, play_button_rect)

    if exit_button_rect.collidepoint(mouse_pos): # Exit hover
        pygame.draw.circle(screen, (230, 230, 230), exit_button_rect.center, exit_button_rect.width // 2 + 18, 0)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif not game_active and play_button_rect.collidepoint(mouse_pos):  # Play hover
        play_button_size = 0.9
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        play_button_size = 0.8

    screen.blit(exit_button_surf, exit_button_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
# -> Succesful end