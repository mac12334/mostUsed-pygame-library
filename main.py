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

data = mostused.convert_to_dictionary.get_data("test.txt", ":", " ")
print(data)
mostused.convert_to_dictionary.write_data("test.txt", data, ":", " ")

index = 0

class Player(mostused.entity.Entity):
    def __init__(self, image: pygame.Surface, pos: tuple[int, int]) -> None:
        mostused.entity.Entity.__init__(self)
        self.image = image
        self.rect = image.get_rect(topleft=pos)
        self.speed = 5

        self.obstacle = pygame.Rect(250, 250, 50, 50)
    
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

lookup_table = pygame.image.load("test_assets/image-test.png").convert_alpha()

spritesheet = mostused.image.get_image_from_lookup_table(lookup_table, pygame.Rect(16, 0, 16, 32))
animation = mostused.image.spritesheet(spritesheet, 2, (16, 16), False, scale = 2)

coffin = mostused.image.get_image_from_lookup_table(lookup_table, pygame.Rect(0, 0, 16, 32), scale=2)
bowl = mostused.image.get_image_from_lookup_table(lookup_table, pygame.Rect(32, 0, 16, 16), scale=2)
ice_cube = mostused.image.get_image_from_lookup_table(lookup_table, pygame.Rect(32, 16, 16, 16), scale=2)

animation_index = 0

clock = pygame.time.Clock()
last_update = pygame.time.get_ticks()

text = mostused.image.get_fitting_text(pygame.font.SysFont(pygame.font.get_default_font(), 32), 200, "this is some really long text, and is only one string")

run = True
while run:
    p.update()

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= 500:
        last_update = current_time
        animation_index = animation_index + 1 if animation_index < len(animation) - 1 else 0

    win.fill((200, 200, 200))

    if button.draw(win):
        index = (index + 1) % 100

    if button_2.draw(win):
        index = (index - 1) % 100
    
    if button_3.draw(win):
        index = 0

    win.blit(tiles[index], (0, 0))

    win.blit(coffin, (500, 500))
    win.blit(bowl, (400, 450))
    win.blit(ice_cube, (500, 400))
    win.blit(animation[animation_index], (400, 400))
    win.blit(text, (400, 0))
    p.draw(win)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(60)
pygame.quit()