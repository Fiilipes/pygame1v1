import pygame  # pygame module
import ctypes  # module for getting users data
# import class Player from components\Player.py
from components.Player import Player
from components.animation import Animation


def death(player1, player2):
    if player1.attack and int(player1.index) == 3 or player2.surface.rect.top > screen_size[1]:
        for i in range(len(player1.hearts.hearts_list)):
            if player2.hearts.hearts_list[len(player1.hearts.hearts_list) - i - 1] == player2.hearts.filled["full"]:
                player2.hearts.hearts_list[len(player1.hearts.hearts_list) - i - 1] = player2.hearts.filled["empty"]
                break
    elif player2.attack and int(player2.index) == 3 or player1.surface.rect.top > screen_size[1]:
        for i in range(len(player2.hearts.hearts_list)):
            if player1.hearts.hearts_list[len(player2.hearts.hearts_list) - i - 1] == player1.hearts.filled["full"]:
                player1.hearts.hearts_list[len(player2.hearts.hearts_list) - i - 1] = player1.hearts.filled["empty"]
                break

    player1.surface.rect.midbottom = player1.spawn_pos["pos"]
    player2.surface.rect.midbottom = player2.spawn_pos["pos"]
    player1.left = player1.spawn_pos["facing_l"]
    player2.left = player2.spawn_pos["facing_l"]
    player1.attack, player2.attack = False, False
    player1.falling, player2.falling = False, False

def on_platform(player_rect):
    return ground_right > player_rect.centerx > ground_left

def physics_platform(player):
    global game_active
    player.gravitation += 10 * 0.08
    player.surface.rect.y += player.gravitation

    if ground_height < player.surface.rect.bottom and on_platform(player.surface.rect) and not player.falling:
        player.surface.rect.bottom = ground_height
        player.gravitation = 0

    if not on_platform(player.surface.rect) or player.surface.rect.bottom < ground_height:
        player.inair = True
    else:
        player.inair = False

    if ground_height < player.surface.rect.bottom:
        player.falling = True
    else:
        player.falling = False

    if player.surface.rect.top > screen_size[1]:  # Death
        death(player1, player2)

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
play_button_size = 0.8

player_font = pygame.font.SysFont("comicsans", 50, True)
button_font = pygame.font.SysFont("comicsans", 100, True)


""" Ground """
ground_height = screen_size[1] - 88
ground_surf = pygame.transform.scale_by(
    pygame.image.load("graphics/ground.png"),  # image url
    1                                          # scale
)
ground_rect = ground_surf.get_rect(midtop=(
    screen_size[0]//2,
    ground_height - 32)
)
ground_left = screen_size[0] // 2 - ground_rect.width // 2
ground_right = screen_size[0] // 2 + ground_rect.width // 2


player1 = Player(
    {
        "text": "P1",
        "color": "blue",
        "font_name": "comicsans",
        "font_size": 50
    },
    "graphics/player/idle/adventurer-idle-00.png",
    screen_size,
    ground_height,
    {
    "facing_l": False,
    "pos": (screen_size[0]//4, ground_height)
    },
    screen
)

player2 = Player(
    {
        "text": "P2",
        "color": "red",
        "font_name": "comicsans",
        "font_size": 50
    },
    "graphics/player/idle/adventurer-idle-00.png",
    screen_size,
    ground_height,
    {
    "facing_l": True,
    "pos": (screen_size[0] - screen_size[0]//4, ground_height)
    },
    screen
)

animate = Animation()

def animation(player):

    if player.attack:
        player.index += 0.15
        if player.index >= len(animate.attack_list):
            player.attack = False
            player.index = 0
        player.surface.surf = animate.attack_list[int(player.index)]

    elif player.inair: # Jump
        player.index += 0.03
        if player.index >= len(animate.jump_list): player.index = 0
        player.surface.surf = animate.jump_list[int(player.index)]

    elif player.running: # Run
        player.index += 0.16
        if player.index >= len(animate.run_list): player.index = 0
        player.surface.surf = animate.run_list[int(player.index)]

    elif player.surface.rect.bottom == ground_height: # Idle
        player.index += 0.07
        if player.index >= len(animate.idle_list): player.index = 0
        player.surface.surf = animate.idle_list[int(player.index)]


    if player.left:
        player.surface.surf = pygame.transform.flip(player.surface.surf, True, False)
    else:
        player.surface.surf = pygame.transform.flip(player.surface.surf, False, False)

exit_button_surf = pygame.transform.scale_by(pygame.image.load("graphics/exit_button.png"), 0.04)
exit_button_rect = exit_button_surf.get_rect(topright=(screen_size[0] - 40, 40))

play_button_surf = pygame.transform.scale_by(pygame.image.load("graphics/play.png"), play_button_size)
play_button_rect = play_button_surf.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))

running = True
print("SUCCESFUL START")
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_active:
                if event.key == pygame.K_w and player1.surface.rect.bottom == ground_height and on_platform(player1.surface.rect) and not player1.attack:
                    player1.gravitation = -21
                if event.key == pygame.K_UP and player2.surface.rect.bottom == ground_height and on_platform(player2.surface.rect) and not player2.attack:
                    player2.gravitation = -21

                if event.key == pygame.K_SPACE and not player1.attack:
                    player1.attack = True
                    player1.index = 0
                if event.key == pygame.K_KP_ENTER and not player2.attack:
                    player2.attack = True
                    player2.index = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_active:
                if play_button_rect.collidepoint(mouse_pos):
                    game_active = True
            if exit_button_rect.collidepoint(mouse_pos):
                running = False


    screen.fill("white")
    keys = pygame.key.get_pressed()

    if game_active:
        if keys[pygame.K_a] and not player1.attack:
            player1.surface.rect.x -= step_size
            player1.running = True
            player1.left = True
        elif keys[pygame.K_d] and not player1.attack:
            player1.surface.rect.x += step_size
            player1.running = True
            player1.left = False
        else:
            player1.running = False

        if keys[pygame.K_LEFT] and not player2.attack:
            player2.surface.rect.x -= step_size
            player2.running = True
            player2.left = True
        elif keys[pygame.K_RIGHT] and not player1.attack:
            player2.surface.rect.x += step_size
            player2.running = True
            player2.left = False
        else:
            player2.running = False

        if player1.surface.rect.colliderect(player2.surface.rect) and ((player1.attack and int(player1.index) == 3) or (player2.attack and int(player2.index) == 3)):
            death(player1, player2)


        if player1.hearts.hearts_list[0] == player1.hearts.filled["empty"] or player2.hearts.hearts_list[0] == player2.hearts.filled["empty"]:
            game_active = False
            player1.hearts.restarting_hearts()
            player2.hearts.restarting_hearts()

        player1.hearts.displaying_hearts()
        player2.hearts.displaying_hearts()

        physics_platform(player1)
        physics_platform(player2)

        screen.blit(ground_surf, ground_rect)

        animation(player1)
        screen.blit(player1.surface.surf, player1.surface.rect)
        screen.blit(player1.text.text, player1.text.get_rect("midbottom",player1.surface.rect.centerx, player1.surface.rect.top))
        animation(player2)
        screen.blit(player2.surface.surf, player2.surface.rect)
        screen.blit(player2.text.text, player1.text.get_rect("midbottom", player2.surface.rect.centerx, player2.surface.rect.top))

    else:
        player1.surface.rect.midbottom = (screen_size[0] // 4, ground_height)
        player1.left = False

        player2.surface.rect.midbottom = (screen_size[0] - screen_size[0] // 4, ground_height)
        player2.left = True

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
print("SUCCESFUL END")
# -> Succesful end
