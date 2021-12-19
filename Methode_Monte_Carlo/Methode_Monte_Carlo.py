import pygame

pygame.init()

TAILLE = (500, 500)
screen = pygame.display.set_mode((TAILLE))
COLOR = {
        "RED": (255, 0, 0),
        "BLUE": (0, 0, 255),
        "BLACK": (0, 0, 0),
        "PURPLE": (255, 0, 255),
    }


lauched = True




while lauched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lauched = False
    pygame.draw.circle(screen,"RED",(0,500), 500)
    

    pygame.display.update()
