import pygame

pygame.init()
size = width, height = 1100, 700
screen = pygame.display.set_mode(size)
pos = (400, 350 + 175)
pos_vrag = (400, 175)
pos_shaiba = (400, 350)
x = 0
v_x = 0
v_y = 0

schet_igr = 0
schet_comp = 0


def draw():
    # screen.fill((204, 202, 202))  # светлая тема
    screen.fill((57, 57, 57))  # темная тема
    pygame.draw.rect(screen, pygame.Color(87, 87, 87), (150, 0, 500, 700), 0)
    # pygame.draw.rect(screen, pygame.Color(230, 230, 230), (150, 0, 500, 700), 0)
    pygame.draw.rect(screen, pygame.Color(147, 147, 147), (150, 340, 500, 20), 0)
    pygame.draw.circle(screen, (147, 147, 147), (400, 350), 64)
    pygame.draw.rect(screen, pygame.Color(255, 13, 0), (300, 680, 200, 20), 0)
    pygame.draw.rect(screen, pygame.Color(51, 61, 255), (300, 0, 200, 20), 0)


def beat(): #otbit
    global v_x, v_y
    if (pos[0] - pos_shaiba[0]) ** 2 + (pos[1] - pos_shaiba[1]) ** 2 <= 40 ** 2:
        v_x = (-pos[0] + pos_shaiba[0]) // 5
        v_y = (-pos[1] + pos_shaiba[1]) // 5
    if (pos_vrag[0] - pos_shaiba[0]) ** 2 + (pos_vrag[1] - pos_shaiba[1]) ** 2 <= 40 ** 2:
        v_x = (-pos_vrag[0] + pos_shaiba[0]) // 5
        v_y = (-pos_vrag[1] + pos_shaiba[1]) // 5


def border(): #kraya
    global v_y, v_x
    if pos_shaiba[0] - 20 <= 150 or pos_shaiba[0] + 20 >= 150 + 500:
        v_x *= -1
    if pos_shaiba[1] - 20 <= 0 or pos_shaiba[1] + 20 >= 700:
        v_y *= -1


def gate(): #vorota
    global schet_comp, schet_igr
    if pos_shaiba[1] - 20 in range(20) or pos_shaiba[1] + 20 in range(680, 700):
        if pos_shaiba[0] in range(150 + 100, 150 + 300):
            if pos_shaiba[1] - 20 in range(20):
                schet_igr += 1
            else:
                schet_comp += 1
            returning()


def returning(): #vozvrat
    global pos, pos_vrag, pos_shaiba, v_y, v_x
    pos = (400, int(350 * 1.5))
    pos_shaiba = (400, 350)
    pos_vrag = (400, 175)
    v_x = v_y = 0
    print(schet_igr, schet_comp)


draw()
pygame.display.flip()
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            returning()
    draw()
    pygame.display.flip()
    clock.tick(24)