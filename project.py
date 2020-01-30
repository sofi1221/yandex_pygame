import pygame

pygame.init()
size = width, height = 1100, 700
screen = pygame.display.set_mode(size)


def draw():
    # screen.fill((204, 202, 202))  # светлая тема
    screen.fill((57, 57, 57))  # темная тема
    pygame.draw.rect(screen, pygame.Color(87, 87, 87), (150, 0, 500, 700), 0)
    # pygame.draw.rect(screen, pygame.Color(230, 230, 230), (150, 0, 500, 700), 0)
    pygame.draw.rect(screen, pygame.Color(147, 147, 147), (150, 340, 500, 20), 0)
    pygame.draw.circle(screen, (147, 147, 147), (400, 350), 64)
    pygame.draw.rect(screen, pygame.Color(255, 13, 0), (300, 680, 200, 20), 0)
    pygame.draw.rect(screen, pygame.Color(51, 61, 255), (300, 0, 200, 20), 0)


pygame.display.flip()
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw()
    pygame.display.flip()
    clock.tick(24)
