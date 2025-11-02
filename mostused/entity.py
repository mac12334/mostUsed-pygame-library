import pygame

class Entity:
    def __init__(self) -> None:
        self.image: pygame.Surface = pygame.Surface((50, 50))
        self.rect: pygame.Rect | pygame.rect.Rect = pygame.Rect(0, 0, 50, 50)

        self.speed: int | float = 0
        self.id: str = "0000"
    
    def colliding(self, rect: pygame.Rect, delta: tuple[int | float, int | float]) -> tuple[int | float, int | float]:
        dx, dy = delta
        if rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
            if rect.right < self.rect.right:
                dx = rect.right - self.rect.left
            if rect.left > self.rect.left:
                dx = rect.left - self.rect.right
        if rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
            if rect.top > self.rect.top:
                dy = rect.top - self.rect.bottom
            if rect.bottom < self.rect.bottom:
                dy = rect.bottom - self.rect.top
        return dx, dy