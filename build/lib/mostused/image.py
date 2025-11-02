import pygame

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