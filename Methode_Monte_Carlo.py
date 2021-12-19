import pygame
import random

pygame.init()


s = 700
TAILLE = (s, s)
screen = pygame.display.set_mode((TAILLE))
COLOR = {
        "RED": (255, 0, 0),
        "BLUE": (0, 0, 255),
        "BLACK": (0, 0, 0),
        "PURPLE": (255, 0, 255),
    }
i = 0
HIT = 0
Total = 0
lauched = True




while lauched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lauched = False
        if i == 0:
            pygame.draw.circle(screen,"RED",(0,s), s) 
            i = i + 1
    l = random.sample(range(1,s), 2)
    if (l[0] - s) * (l[0] - s) + (l[1] - s) * (l[1] - s) <= s * s:
        HIT = HIT + 1 
        Total = Total + 1
    else:
        Total = Total + 1     
    

    print (f"nombre de points = {Total}")
    print (f"nombre de point dans le cercle = {HIT}")
    print (f"pi = {HIT/Total*4}")
    pygame.draw.circle(screen,"BLUE", l, 1)


    pygame.display.update()
