import pygame
import math

pygame.init()

WIDTH = 600
HEIGHT = 600

x_start = WIDTH / 2
y_start = HEIGHT / 2

two_pi = math.pi * 2

black = (0, 0, 0)
pink = (255, 102, 204)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Heart')
font = pygame.font.Font('FreeSansBold.ttf', 16)

character ="*"

def heart(char, x_value, y_value):

    text = font.render(str(char), True, pink)
    display_surface.blit(text, (x_value, y_value))


t = 0
r = 15

run = True
while run:
    screen.fill((black))
    while t < two_pi:
        x = x_start + (r * 16 * math.sin(t) ** 3)
        y = y_start - (r * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)))
        heart(character, x, y)
        pygame.time.wait(100)
        pygame.display.update()
        t += 0.12

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False