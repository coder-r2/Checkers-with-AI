import pygame

WIDTH = HEIGHT = 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# RGB Codes
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (34, 18))