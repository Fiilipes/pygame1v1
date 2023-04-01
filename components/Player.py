import pygame

class Player:
    def __init__(self, text, image, screen_size, ground_height, spawn_pos):
        self.gravitation = 0
        self.inair = False
        self.running = False
        self.falling = False
        self.left = False
        self.index = 0
        self.surface = self.Surface(image, screen_size, ground_height, spawn_pos)
        self.text = self.Text(text, screen_size)




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


