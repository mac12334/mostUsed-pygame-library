import mostused, pygame

import random

pygame.init()

win = pygame.display.set_mode((600, 600))

b_rect = pygame.Rect(50, 50, 100, 50)
button = mostused.button.button_from_rect(b_rect, (255, 0, 0), True, (0, 255, 0))

button_2 = mostused.button.button_from_text_def("hello world", (50, 100), 20, (255, 255, 255), (0, 0, 0))

font = pygame.font.SysFont("roboto", 20)
button_3 = mostused.button.button_from_text("roboto", (50, button_2.rect.bottom), font, (255, 255, 255), (0, 0, 255))

surf = pygame.Surface((600, 600))

for y in range(10):
    for x in range(10):
        val = random.randint(0, 255)
        pygame.draw.rect(surf, (val, val, val), pygame.Rect(x * 60, y * 60, 60, 60))

tiles = mostused.image.tileset(surf, (60, 60), (10, 10), (255, 0, 0))

index = 0

class Player(mostused.entity.Entity):
    def __init__(self, image: pygame.Surface, pos: tuple[int, int]) -> None:
        mostused.entity.Entity.__init__(self)
        self.image = image
        self.rect = image.get_rect(topleft=pos)
        self.speed = 5

        self.obstacle = pygame.Rect(50, 50, 50, 50)
    
    def update(self) -> None:
        dx, dy = 0, 0
        k = pygame.key.get_pressed()
        if k[pygame.K_w]:
            dy -= self.speed
        if k[pygame.K_a]:
            dx -= self.speed
        if k[pygame.K_s]:
            dy += self.speed
        if k[pygame.K_d]:
            dx += self.speed
        
        dx, dy = self.colliding(self.obstacle, (dx, dy))
        self.rect.x += int(dx)
        self.rect.y += int(dy)
    
    def draw(self, screen: pygame.Surface | pygame.surface.Surface) -> None:
        screen.blit(self.image, self.rect)

        pygame.draw.rect(screen, (0, 0, 0), self.obstacle)

player_image = pygame.Surface((50, 50))
player_image.fill((255, 0, 0))

p = Player(player_image, (300, 300))

clock = pygame.time.Clock()

run = True
while run:
    p.update()

    win.fill((255, 255, 255))

    if button.draw(win):
        index = (index + 1) % 100

    if button_2.draw(win):
        index = (index - 1) % 100
    
    if button_3.draw(win):
        index = 0

    win.blit(tiles[index], (0, 0))
    p.draw(win)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(60)
pygame.quit()