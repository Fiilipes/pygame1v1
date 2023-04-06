import pygame

class Player:
    def __init__(self, text, image, screen_size, ground_height, spawn_pos, screen):
        self.gravitation = 0
        self.inair = False
        self.running = False
        self.falling = False
        self.attack = False
        self.left = spawn_pos["facing_l"]
        self.index = 0
        self.surface = self.Surface(image, screen_size, ground_height, spawn_pos)
        self.text = self.Text(text, screen_size)
        self.hearts = self.Hearts(3, screen, screen_size, self.left)
        self.spawn_pos = spawn_pos


    class Hearts:
        def __init__(self, amount, screen, screen_size, left):
            self.screen = screen
            self.screen_size = screen_size
            self.left = left
            self.filled = {"full": (pygame.transform.scale_by(pygame.image.load("graphics/heart_full.png"), 0.3)),
                         "empty": (pygame.transform.scale_by(pygame.image.load("graphics/heart_empty.png"), 0.3))
                         }
            self.surf = self.filled["full"]
            self.hearts_list = []
            self.heart_pos = [50, 50]
            for i in range(amount):
                self.hearts_list.append(self.surf) # Surface to the position 0
        def displaying_hearts(self):
            if not self.left:
                for i in range(len(self.hearts_list)):
                    self.screen.blit(self.hearts_list[i], (220 + i * 90, 50))
            else:
                for i in range(len(self.hearts_list)):
                    self.screen.blit(self.hearts_list[i], (self.screen_size[0] - 220 - i * 90, 50))

        def restarting_hearts(self):
            for i in range(len(self.hearts_list)):
                self.hearts_list[i] = self.filled["full"]



    class Surface:
        def __init__(self, image, screen_size, ground_height, spawn_pos):
            self.surf = pygame.transform.scale_by(pygame.image.load(image), 4)
            self.rect = self.surf.get_rect(midbottom=spawn_pos["pos"])

    class Text:
        def __init__(self, text, screen_size):
            self.font = pygame.font.SysFont(text["font_name"], text["font_size"], True)
            self.text = text["text"]
            self.color = text["color"]
            self.font_size = text["font_size"]
            self.text = self.font.render(self.text, True, self.color)

        def get_rect(self, position, x, y):
            match position:
                case "center":
                    return self.text.get_rect(center=(x, y))
                case "midbottom":
                    return self.text.get_rect(midbottom=(x, y))
                case "topleft":
                    return self.text.get_rect(topleft=(x, y))
                case "topright":
                    return self.text.get_rect(topright=(x, y))
                case "bottomleft":
                    return self.text.get_rect(bottomleft=(x, y))
                case "bottomright":
                    return self.text.get_rect(bottomright=(x, y))
                case "midleft":
                    return self.text.get_rect(midleft=(x, y))
                case "midright":
                    return self.text.get_rect(midright=(x, y))
                case "centerleft":
                    return self.text.get_rect(centerleft=(x, y))
                case "centerright":
                    return self.text.get_rect(centerright=(x, y))
                case "topcenter":
                    return self.text.get_rect(topcenter=(x, y))
                case "bottomcenter":
                    return self.text.get_rect(bottomcenter=(x, y))
                case _:
                    return self.text.get_rect(center=(x, y))


