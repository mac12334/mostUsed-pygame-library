import pygame

class Button:
    def __init__(self, surf: pygame.Surface, pos: tuple[int, int], delta: tuple[int, int] = (0, 0)) -> None:
        self.surf = surf
        self.rect = surf.get_rect(topleft=pos)
        self.delta = delta

        self.pressed = False
        self.allow_hold = False
    
    def draw(self, screen: pygame.Surface | pygame.surface.Surface) -> bool:
        screen.blit(self.surf, self.rect)

        if pygame.mouse.get_pressed()[0] and (not self.pressed or self.allow_hold):
            x, y = pygame.mouse.get_pos()
            x -= self.delta[0]
            y -= self.delta[1]
            self.pressed = True
            return self.rect.x <= x <= self.rect.right and self.rect.y <= y <= self.rect.bottom
        elif not pygame.mouse.get_pressed()[0]:
            self.pressed = False
        return False

def button_from_rect(rect: pygame.Rect, color: pygame.Color | tuple[int, int, int], border: bool=False, border_color:pygame.Color | tuple[int, int, int] = pygame.Color(0, 0, 0)) -> Button:
    surf = pygame.Surface(rect.size)
    surf.fill(color)

    if border:
        pygame.draw.rect(surf, border_color, pygame.Rect(0, 0, rect.width, rect.height), 2)

    but = Button(surf, rect.topleft)
    return but

def button_from_text_def(text: str, pos: tuple[int, int], size: int, t_color: pygame.Color | tuple[int, int, int], b_color: pygame.Color | tuple[int, int, int]) -> Button:
    font = pygame.font.SysFont(pygame.font.get_default_font(), size)
    return button_from_text(text, pos, font, t_color, b_color)

def button_from_text(text: str, pos: tuple[int, int], font: pygame.font.Font, t_color: pygame.Color | tuple[int, int, int], b_color: pygame.Color | tuple[int, int, int]) -> Button:
    t = font.render(text, False, t_color)
    surf = pygame.Surface((t.get_width() + 20, t.get_height() + 20))
    surf.fill(b_color)
    surf.blit(t, (10, 10))
    return Button(surf, pos)