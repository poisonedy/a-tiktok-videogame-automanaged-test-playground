import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 #frames per second setting
fpsClock = pygame.time.Clock()

#set up the window
screen = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('animation')

#set up the colors
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 180)
RED   = (255,   0,   0)

image  = pygame.image.load('img/showImage.png')
imagex = 360
imagey = 260
direction = 'left'

# text setting
font_obj = pygame.font.Font('freesansbold.ttf', 32)
text_surface_obj = font_obj.render('Hello World!', True, GREEN, BLUE)
text_rect_obj = text_surface_obj.get_rect()
text_rect_obj.center = (200, 150)

while True: # the main game loop
    screen.fill(WHITE)

    # draw a GREEN polygon onto the surface
    pygame.draw.polygon(screen, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

    # draw some BLUE lines onto the surface
    pygame.draw.line(screen, BLUE, (60, 60), (120, 60), 4)
    pygame.draw.line(screen, BLUE, (120, 60), (60, 120))
    pygame.draw.line(screen, BLUE, (60, 120), (120, 120), 4)

    # draw a BLUE circle onto the surface
    pygame.draw.circle(screen, BLUE, (300, 50), 20, 0)

    # draw a RED ellipse onto the surface
    pygame.draw.ellipse(screen, RED, (100, 150, 40,80), 1)

    # draw a RED rectangle onto the surface
    pygame.draw.rect(screen,RED, (200, 150, 100, 50))

    # draw the text onto the surface
    screen.blit(text_surface_obj, text_rect_obj)


    #the animation of the image
    if direction == 'right':
        imagex += 5
        if imagex == 360:
            direction = 'down'
    elif direction == 'down':
        imagey += 5
        if imagey == 260:
            direction = 'left'
    elif direction == 'left':
        imagex -= 5
        if imagex == 20:
            direction = 'up'
    elif direction == 'up':
        imagey -= 5
        if imagey == 20:
            direction = 'right'
    screen.blit(image, (imagex, imagey))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)