import pygame
import random
import os



pygame.init()
size = width, height = 1100, 700
screen = pygame.display.set_mode(size)
pos = (400, 350 + 175)
pos_vrag = (400, 175)
pos_shaiba = (400, 350)
x = 0
v_x = 0
v_y = 0
n = 0

schet_igr = 0
schet_comp = 0
obsh_igr = 0
obsh_comp = 0

theme = 0
level = 0
with open('statistic.txt', 'rt') as f:
    r = f.read()
    arr = [float(x) for x in r.split()]
    time = arr[0]
    comp = arr[1]
    igr = arr[2]
    best_comp = arr[3]
    best_igr = arr[4]
    lenqth = arr[5]

def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    return image
x_x = 0
screen.fill((87, 87, 87))

time = 0
comp = 0
igr = 0
best_comp = 0
best_igr = 0
lenqth = 0



class Hokkey:
    def draw(self):
        global screen, height, width, time, stroka
        # screen.fill((204, 202, 202))  # светлая тема
        # screen.fill((57, 57, 57))  # темная тема
        pygame.draw.rect(screen, color_back, (0, 0, 150, 700), 0)
        pygame.draw.rect(screen, color_back, (650, 0, 40, 700), 0)
        pygame.draw.rect(screen, color_back, (650, 0, 1100, 80 + 40), 0)
        pygame.draw.rect(screen, color_back, (500, 480, 1000, 1000), 0)
        pygame.draw.rect(screen, (87, 87, 87), (150, 0, 500, 700), 0)

        pygame.draw.rect(screen, color_pole, (150, 0, 500, 700), 0)
        pygame.draw.rect(screen, (197, 197, 197), (150, 340, 500, 20), 0)
        pygame.draw.circle(screen, (197, 197, 197), (400, 350), 64)
        pygame.draw.rect(screen, (255, 13, 0), (300, 680, 200, 20), 0)
        pygame.draw.rect(screen, (51, 61, 255), (300, 0, 200, 20), 0)

        font = pygame.font.Font(None, 296)
        color = color_green

        text = font.render("4k3s", 1, color)
        text_x = 150 + 250 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2
        image = pygame.Surface((text.get_width(), text.get_height()))
        image.set_alpha(50)
        pygame.draw.rect(image, color_pole, (0, 0, *text.get_size()), 0)
        image.blit(text, (0, 0))
        screen.blit(image, (text_x, text_y))
        pygame.draw.rect(screen, (20, 200, 255), (150, 0, 500, 700), 3)

        font = pygame.font.Font(None, 200)
        text = font.render(str(schet_comp), 1, (51, 61, 255))
        text_y = 20
        text_x = 20
        screen.blit(text, (text_x, text_y))

        text = font.render(str(schet_igr), 1, (255, 13, 0))
        text_y = 550
        text_x = 20
        screen.blit(text, (text_x, text_y))

        font = pygame.font.Font(None, 50)
        text = font.render("User's name: " + str(obsh_igr), 1, color_green)
        text_y = 20
        text_x = 150 + 500 + 20
        screen.blit(text, (text_x, text_y))

        text = font.render("CompudaXter: " + str(obsh_comp), 1, color_green)
        text_y = 20 + 40
        text_x = 150 + 500 + 20
        screen.blit(text, (text_x, text_y))

        font = pygame.font.Font(None, 35)
        text = font.render("Правила", 1, color_back)
        # print(text.get_size())
        text_x = 1100 - 10 - text.get_width()
        text_y = 650
        image = pygame.Surface((text.get_width() + 10, text.get_height() + 10))
        image.set_alpha(255)
        pygame.draw.rect(image, color_green, (0, 0, text.get_width() + 10, text.get_height() + 10), 0)
        image.blit(text, (5, 5))
        screen.blit(image, (text_x, text_y))

        text = font.render("Home", 1, color_back)
        # print(text.get_size())
        text_x = 1100 - 20 - 120 - text.get_width()
        text_y = 650
        image = pygame.Surface((text.get_width() + 10, text.get_height() + 10))
        image.set_alpha(255)
        pygame.draw.rect(image, color_green, (0, 0, text.get_width() + 10, text.get_height() + 10), 0)
        image.blit(text, (5, 5))
        screen.blit(image, (text_x, text_y))

        text = font.render("Инструкция", 1, color_back)
        # print(text.get_size())
        text_x = 900 - 30 - text.get_width()
        text_y = 650
        image = pygame.Surface((text.get_width() + 10, text.get_height() + 10))
        image.set_alpha(255)
        pygame.draw.rect(image, color_green, (0, 0, text.get_width() + 10, text.get_height() + 10), 0)
        image.blit(text, (5, 5))
        screen.blit(image, (text_x, text_y))

        font = pygame.font.Font(None, 25)
        color = color_green
        time_1 = time
        hh = time_1 // 3600
        time_1 %= 3600
        mm = time_1 // 60
        time_1 %= 60
        ss = time_1 // 1


        text = font.render(
            "В игре вы провели: " + str(int(hh)) + ':' + str(int(mm)).rjust(2, '0') + ':' +
            str(int(ss)).rjust(2, '0'), 1, color)
        text_x = 150 + 500 + 20
        text_y = 500
        screen.blit(text, (text_x, text_y))

        text = font.render(
            "Всего очков у ИИ: " + str(int(comp)), 1, color)
        text_x = 150 + 500 + 20
        text_y = 500 + 20
        screen.blit(text, (text_x, text_y))

        text = font.render(
            "Всего очков у человечества: " + str(int(igr)), 1, color)
        text_x = 150 + 500 + 20
        text_y = 500 + 40
        screen.blit(text, (text_x, text_y))

        text = font.render(
            "Рекорд ИИ: " + str(int(best_comp)), 1, color)
        text_x = 150 + 500 + 20
        text_y = 500 + 60
        screen.blit(text, (text_x, text_y))

        text = font.render(
            "Рекорд человечества: " + str(int(best_igr)), 1, color)
        text_x = 150 + 500 + 20
        text_y = 500 + 80
        screen.blit(text, (text_x, text_y))

        # mile = pymorphy2.MorphAnalyzer().parse('метр')[0]
        mile = stroka

        text = font.render("Всего пройдено курсором: " + str(int(lenqth // 3793)) + ' ' + mile.make_agree_with_number(
            int(lenqth // 3793)).word, 1, color)
        text_x = 150 + 500 + 20
        text_y = 500 + 100
        screen.blit(text, (text_x, text_y))

        if v == 4:
            p = 'Легкий'
        elif v == 2:
            p = 'Средний'
        else:
            p = 'Тяжелый'
        font = pygame.font.Font(None, 23)
        text = font.render(
            "Уровень сложности: " + p + ', ' + str(h) + ' мин на поле', 1, color)
        text_x = 690
        text_y = 120 - text.get_height()
        screen.blit(text, (text_x, text_y))

    def otbit(self):
        global v_x, v_y  # 3 easy, 2 medium, 1 hard
        if (pos[0] - pos_shaiba[0]) ** 2 + (pos[1] - pos_shaiba[1]) ** 2 <= 40 ** 2:
            v_x = (-pos[0] + pos_shaiba[0]) // v  # <-- this chislo (1, 2 ili 2)
            v_y = (-pos[1] + pos_shaiba[1]) // v
        if (pos_vrag[0] - pos_shaiba[0]) ** 2 + (pos_vrag[1] - pos_shaiba[1]) ** 2 <= 40 ** 2:
            v_x = (-pos_vrag[0] + pos_shaiba[0]) // v
            v_y = (-pos_vrag[1] + pos_shaiba[1]) // v

    def kraya(self):
        global v_y, v_x
        if pos_shaiba[0] - 20 <= 150 or pos_shaiba[0] + 20 >= 150 + 500:
            v_x *= -1
        if pos_shaiba[1] - 20 <= 0 or pos_shaiba[1] + 20 >= 700:
            v_y *= -1

    def vorota(self):
        global schet_comp, schet_igr, obsh_igr, obsh_comp, comp, igr, best_comp, best_igr, f_win, f_lose
        if pos_shaiba[1] - 20 in range(20) or pos_shaiba[1] + 20 in range(680, 700):
            if pos_shaiba[0] in range(150 + 150, 150 + 350):
                if pos_shaiba[1] - 20 in range(20):
                    schet_igr += 1

                    if schet_igr == 5:
                        obsh_igr += 1
                        f_win = 1
                        igr += 1
                        schet_igr = 0
                        schet_comp = 0
                        if obsh_igr > best_igr:
                            best_igr = obsh_igr
                            # print('igr')
                else:
                    schet_comp += 1

                    if schet_comp == 5:
                        obsh_comp += 1
                        f_lose = 1
                        comp += 1
                        schet_igr = 0
                        schet_comp = 0
                        if obsh_comp > best_comp:
                            best_comp = obsh_comp
                self.vozvrat()

    def vozvrat(self):
        global pos, pos_vrag, pos_shaiba, v_y, v_x
        pos = (400, int(350 * 1.5))
        pos_shaiba = (400, 350)
        pos_vrag = (400, 175)
        v_x = v_y = 0


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, color_pole, (
                    self.left + self.cell_size * i, self.top + self.cell_size * j,
                    self.cell_size, self.cell_size), 0)
                pygame.draw.rect(screen, (20, 200, 255), (
                    self.left + self.cell_size * i, self.top + self.cell_size * j,
                    self.cell_size, self.cell_size), 1)


class Minesweeper(Board):
    def __init__(self, x, y):
        global height, width
        super().__init__(x, y)
        self.x = self.y = 0
        self.arr = []
        self.fool = 0
        self.opened = 0
        for i in range(height):
            a = []
            for j in range(width):
                a += [0]
            self.arr += [a]

    def drawing(self):
        global arr, pos, screen
        if self.fool == 1:
            for i in range(8):
                for j in range(8):
                    if arr[i][j] != 10:
                        x = 0
                        for i1 in range(pos[0] - 1, pos[0] + 2):
                            for j1 in range(pos[1] - 1, pos[1] + 2):
                                if i1 in range(len(arr)) and j1 in range(len(arr[0])) and \
                                        arr[i1][j1] == 10:
                                    x += 1
                        font = pygame.font.Font(None, 30)
                        text = font.render(str(int(x)), 1, (255, 255, 255))
                        text_x = pos[0] * self.cell_size + self.cell_size * 0.5 + self.left
                        text_y = pos[1] * self.cell_size + self.cell_size * 0.5 + self.top
                        screen.blit(text, (text_x, text_y))
                        pygame.display.flip()
                    else:
                        pygame.draw.rect(screen, (108, 52, 97), (
                            self.left + self.cell_size * i, self.top + self.cell_size * j,
                            self.cell_size, self.cell_size), 0)
                        pygame.display.flip()

    def open_cell(self, pos, q):
        pass

    def get_click(self, mouse_pos, x=1):
        cell = self.get_cell(mouse_pos)
        if cell:
            if x == 0:
                self.open_cell(cell, x)
            else:
                self.open_cell(cell, x)  # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    def get_cell(self, mouse_pos):
        if mouse_pos[0] in range(self.left, self.left + self.height * self.cell_size) and \
                mouse_pos[1] in range(self.top, self.top + self.width * self.cell_size):
            return ((mouse_pos[0] - self.left) // self.cell_size,
                    (mouse_pos[1] - self.top) // self.cell_size)
        else:
            return None


# if entered == 1:
arr = []
c = 8
a = b = 8
font1 = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 30)
for i in range(8):
    x = []
    for j in range(8):
        x += [-1]
    arr += [x]
arr_1 = []
for i in range(c):
    q, w = random.choice([j for j in range(a)]), random.choice([j for j in range(b)])
    while (q, w) in arr_1:
        q, w = random.choice([j for j in range(a)]), random.choice([j for j in range(b)])
    arr[q][w] = 10
    arr_1 += [(q, w)]
board = Minesweeper(a, b)
board.set_view(150 + 500 + 40, 80 + 40, 45)
# board.render()
pos_last = (400, int(350 * 1.5))
hokkey = Hokkey()

# hokkey.draw()
pygame.display.flip()
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        all_sprites.update(event)
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            if pygame.mouse.get_pos()[0] in range(150 + 20, 150 + 500 - 20) and pygame.mouse.get_pos()[1] in \
                    range(350 + 20, 700 - 20):
                pos = pygame.mouse.get_pos()
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
        pygame.draw.circle(screen, (255, 61, 51), pos, 20)
        pygame.draw.circle(screen, (255, 13, 0), pos, 10)
        pygame.draw.circle(screen, (51, 61, 255), pos_vrag, 20)
        pygame.draw.circle(screen, (0, 13, 255), pos_vrag, 10)
        pos_shaiba = (pos_shaiba[0] + v_x, pos_shaiba[1] + v_y)
        if pos_shaiba[0] > pos_vrag[0]:
            pos_vrag = (pos_vrag[0] + abs(v_x) // 3 * 2, pos_vrag[1])
        elif pos_shaiba[0] < pos_vrag[0]:
            pos_vrag = (pos_vrag[0] - abs(v_x) // 3 * 2, pos_vrag[1])
        # pos_vrag = (pos_vrag[0] + v_x // 3, pos_vrag[1])
        pygame.draw.circle(screen, (255, 255, 0), pos_shaiba, 20)

        pygame.display.flip()
        clock.tick(24)

    pygame.display.flip()
    clock.tick(25)
# print(time, comp, igr)
