import pygame

__all__ = [
    "tileset",
    "spritesheet",
    "get_image_from_lookup_table",
    "get_fitting_text"
]

def tileset(image: pygame.Surface, tilesize: tuple[int, int], gridsize: tuple[int, int], colorkey: pygame.Color | tuple[int, int, int] = (0, 0, 0), scale: int | float = 1) -> list[pygame.Surface]:
    tiles = []
    for y in range(gridsize[1]):
        for x in range(gridsize[0]):
            tile = pygame.Surface(tilesize)
            tile.fill(colorkey)
            tile.blit(image, (tilesize[0] * -x, tilesize[1] * -y))
            tile.set_colorkey(colorkey)
            tile = pygame.transform.scale(tile, (tilesize[0] * scale, tilesize[1] * scale))
            tiles.append(tile)
    return tiles

def spritesheet(image: pygame.Surface, cells: int, cellsize: tuple[int, int], horizontal: bool = True, colorkey: pygame.Color | tuple[int, int, int] = (0, 0, 0), scale: int | float = 1) -> list[pygame.Surface]:
    animation = []
    for z in range(cells):
        cell = pygame.Surface(cellsize)
        cell.fill(colorkey)
        if horizontal:
            cell.blit(image, (cellsize[0] * -z, 0))
        else:
            cell.blit(image, (0, cellsize[1] * -z))
        cell.set_colorkey(colorkey)
        cell = pygame.transform.scale(cell, (cellsize[0] * scale, cellsize[1] * scale))
        animation.append(cell)
    return animation

def get_image_from_lookup_table(lookup_table: pygame.Surface, rect: pygame.Rect, colorkey: tuple[int] = (0, 0, 0), scale: float = 1) -> pygame.Surface:
    image = pygame.Surface(rect.size)
    image.fill(colorkey)
    image.blit(lookup_table, (-rect.x, -rect.y))
    image.set_colorkey(colorkey)
    image = pygame.transform.scale(image, (rect.width * scale, rect.height * scale))
    return image

def _get_lines(font: pygame.font.Font, maximum_width: int, text: str) -> list[str]:
    lines = []
    words = text.split(" ")
    current_string = ""
    current_width = 0
    for word in words:
        word_width = font.size(word + " ")[0]
        if current_width + word_width < maximum_width:
            current_width += word_width
            current_string += word + " "
        else:
            lines.append(current_string)
            current_string = word + " "
            current_width = font.size(current_string)[0]
    lines.append(current_string)
    return lines

def _get_height(font: pygame.font.Font, lines: list[str], line_height: int) -> int:
    height = 0
    for line in lines:
        height += font.size(line)[1] + line_height
    return height

def get_fitting_text(font: pygame.font.Font, maximum_width: int, text: str, textcolor: tuple[int]=(0,0,0), background: tuple[int]=(255,255,255)) -> pygame.Surface:
    lines = _get_lines(font, maximum_width, text)
    line_height = font.get_linesize()
    height = _get_height(font, lines, line_height)
    image = pygame.Surface((maximum_width, height))
    image.fill(background)

    y = line_height / 2
    for line in lines:
        l = font.render(line[:-1], True, textcolor)
        image.blit(l, ((maximum_width / 2) - (l.get_width() / 2), y))
        y += line_height + l.get_height()
    return image
