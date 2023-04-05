import pygame

class Animation:
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

    attack0 = pygame.transform.scale_by(pygame.image.load("graphics/player/attack/adventurer-attack2-00.png"), 4)
    attack1 = pygame.transform.scale_by(pygame.image.load("graphics/player/attack/adventurer-attack2-01.png"), 4)
    attack2 = pygame.transform.scale_by(pygame.image.load("graphics/player/attack/adventurer-attack2-02.png"), 4)
    attack3 = pygame.transform.scale_by(pygame.image.load("graphics/player/attack/adventurer-attack2-03.png"), 4)
    attack4 = pygame.transform.scale_by(pygame.image.load("graphics/player/attack/adventurer-attack2-04.png"), 4)
    attack5 = pygame.transform.scale_by(pygame.image.load("graphics/player/attack/adventurer-attack2-05.png"), 4)
    attack_list = [attack0, attack1, attack2, attack3, attack4, attack5]