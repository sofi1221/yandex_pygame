import pygame
import random
import os
import pymorphy2


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    return image


# инициализация Pygame:
pygame.init()
# размеры окна:
size = width, height = 1100, 700
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
color_end = (255, 255, 0)
color_font = (255, 0, 0)
pos = (400, 350 + 175)
pos_vrag = (400, 175)
pos_shaiba = (400, 350)
x = 0
v_x = 0
v_y = 0
n = 0
stroka = pymorphy2.MorphAnalyzer().parse('метр')[0]
pygame.display.set_caption("4k3s")
image_flag = pygame.image.load('dark.png').convert_alpha()
pygame.display.set_icon(image_flag)

schet_igr = 0
schet_comp = 0
obsh_igr = 0
obsh_comp = 0

theme = 0
level = 0

x_x = 0
screen.fill((87, 87, 87))

time = 0
comp = 0
igr = 0
best_comp = 0
best_igr = 0
lenqth = 0

f_saper = 0
with open('data/statistic.txt', 'rt') as f:
    r = f.read()
    arr = [float(x) for x in r.split()]
    time = arr[0]
    comp = arr[1]
    igr = arr[2]
    best_comp = arr[3]
    best_igr = arr[4]
    lenqth = arr[5]

font = pygame.font.Font(None, 296)
color1 = (255, 13, 0)
color = (255, 255, 255)
text = font.render("WIN", 1, color)
text_x_win = 500 // 2 - text.get_width() // 2
text_y_win = 350 // 2 - text.get_height() // 2
image_win = pygame.Surface((500, 350))
image_win.set_alpha(128)
pygame.draw.rect(image_win, color1, (0, 0, 500, 350), 0)
image_win.blit(text, (text_x_win, text_y_win))

color1 = (51, 61, 255)
image_lose = pygame.Surface((500, 350))
image_lose.set_alpha(128)
pygame.draw.rect(image_lose, color1, (0, 0, 500, 350), 0)
image_lose.blit(text, (text_x_win, text_y_win))

f_win = 0
y_win = 700

f_lose = 0
y_lose = -350

all_sprites = pygame.sprite.Group()


# формирование кадра:
# команды рисования на холсте
def draw():
    screen.fill(color_end)
    # шрифты
    font1 = pygame.font.Font(None, 50)
    font2 = pygame.font.Font(None, 30)
def test(pos, r, text):
    color = (0, 255, 0)
    image_instr = pygame.Surface((1100, 700))
    image_instr.fill((0, 0, 0))
    pygame.draw.circle(image_instr, color, (pos), r)
    font = pygame.font.Font(None, 88)
    if theme == 1:
        text = font.render(text, 1, (100, 255, 100))
    else:
        text = font.render(text, 1, (255, 100, 255))
    text_x = 1100 // 2 - text.get_width() // 2
    if pos[1] >= 500:
        text_y = 100
    else:
        text_y = 600
    image_instr.blit(text, (text_x, text_y))
    image_instr.set_colorkey(color)
    image_instr.set_alpha(192)

    screen.blit(image_instr, (0, 0))
    # pygame.display.flip()


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

    pygame.draw.rect(screen, color_font, (940, 640, 150, 50), 0)  # кнопка играть
    text = font1.render('Играть', 1, color_end)
    text_x = 940 + 75 - text.get_width() // 2
    text_y = 640 + 25 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
        font = pygame.font.Font(None, 25)
        color = color_green
        time_1 = time
        hh = time_1 // 3600
        time_1 %= 3600
        mm = time_1 // 60
        time_1 %= 60
        ss = time_1 // 1

    text = font1.render('Добро пожаловать в супер новую версию ваших любимых игр!', 1, color_font)
    text_x = width // 2 - text.get_width() // 2
    text_y = 25
    screen.blit(text, (text_x, text_y))
    text_y += text.get_height() + 20
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

    text = font2.render('В данной программе вы можете играть в разные игры, при этом ваш счет всегда сохраняется.', 1,
                        color_font)
    text_x = width // 2 - text.get_width() // 2
    screen.blit(text, (text_x, text_y))
    text_y += text.get_height() + 12

    sp = ['Слева и справа от стола для аэрохокея расположен счет аэрохокея и общий соответственно. Когда один ',
          'из игроков достигнет 5 очков в аэрохокее, счет слева обновится, а на счете справа данному игроку',
          'добавится 1 очко.', 'При победе в игре "Сапер", очко добавляется сразу в общий счет.']
    for t in sp:
        text = font2.render(t, 1, color_font)
        screen.blit(text, (5, text_y))
        text_y += text.get_height() + 12
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
    text = font1.render('Правила игры в аэрохокей:', 1, color_font)
    text_x = width // 2 - text.get_width() // 2
    screen.blit(text, (text_x, text_y))
    text_y += text.get_height() + 20

    sp = ['Это спортивная игра, которая проводится на специальном столе небольших размеров с бортиками.',
          'Суть игры весьма проста: вы должны забить максимальное количество голов в ворота противника. У вас ',
          'будут свои ворота и клюшка красного цвета и одна шайба. Мышкой вы управляете клюшкой, ей вы ',
          'можете отбивать шайбу. Обратите внимание, что вы  можете управлять клюшкой только на своей половине',
          'игрового поля.']
    for t in sp:
        text = font2.render(t, 1, color_font)
        screen.blit(text, (5, text_y))
        text_y += text.get_height() + 12

    text = font1.render('Правила игры в сапера:', 1, color_font)
    text_x = width // 2 - text.get_width() // 2
    text_y -= 20
    screen.blit(text, (text_x, text_y))
    text_y += text.get_height() + 20
                    if schet_comp == 5:
                        obsh_comp += 1
                        f_lose = 1
                        comp += 1
                        schet_igr = 0
                        schet_comp = 0
                        if obsh_comp > best_comp:
                            best_comp = obsh_comp
                self.vozvrat()

    sp = ['Перед вами поле 8х8. Сначала нажмите на произвольную клетку. Число в ячейке показывает, сколько мин ',
          'скрыто вокруг данной клетки. Поле вокруг нее - это квадрат 3х3, в центре которого находится данная ',
          'ячейка. Это число поможет понять, где находятся безопасные ячейки, а где находятся бомбы. Если рядом',
          'с открытой ячейкой есть пустая клетка, то она откроется автоматически. Если вы открыли ячейку с миной,',
          'все клетки с бомбами станут синими, а игра обновится, так как вы проиграли.',
          'Игра продолжается до тех пор, пока вы не откроете все не заминированные ячейки.']
    for t in sp:
        text = font2.render(t, 1, color_font)
        screen.blit(text, (5, text_y))
        text_y += text.get_height() + 12
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
        global arr, obsh_comp, obsh_igr, comp, igr, best_comp, best_igr, f_win, f_lose, f_saper
        if q == 1:
            if arr[pos[0]][pos[1]] == -1:
                if f_saper == 1:
                    f_saper = 0
                self.opened += 1
                x = 0
                for i in range(pos[0] - 1, pos[0] + 2):
                    for j in range(pos[1] - 1, pos[1] + 2):
                        if i in range(len(arr)) and j in range(len(arr[pos[0]])) and \
                                (arr[i][j] == 10 or arr[i][j] == -12):
                            x += 1
                font = pygame.font.Font(None, 30)
                text = font.render(str(int(x)), 1, color_green)
                text_x = pos[0] * self.cell_size + self.cell_size * 0.5 + self.left
                text_y = pos[1] * self.cell_size + self.cell_size * 0.5 + self.top
                screen.blit(text, (text_x, text_y))
                pygame.display.flip()
                arr[pos[0]][pos[1]] = 0
                if x == 0:
                    for i1 in range(pos[0] - 1, pos[0] + 2):
                        for j1 in range(pos[1] - 1, pos[1] + 2):
                            if i1 in range(0, self.width) and j1 in range(0, self.height):
                                self.open_cell((i1, j1), 1)
            elif arr[pos[0]][pos[1]] == 10:
                if f_saper == 1:
                    arr = []
                    c = h
                    a = b = 8
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
                    f_saper = 1
                    board = Minesweeper(8, 8)
                    board.set_view(150 + 500 + 40, 80 + 40, 45)
                    # board.render()
                    board.open_cell(pos, 1)
                    # print('12345')
                else:
                    self.fool = 1
                    obsh_comp += 1
                    comp += 1
                    f_lose = 1
                    if obsh_comp > best_comp:
                        best_comp = obsh_comp
                    self.drawing()
        else:
            if arr[pos[0]][pos[1]] == -1:
                arr[pos[0]][pos[1]] = -2
                # pygame.draw.rect(screen, (255, 61, 51), (
                #     self.left + self.cell_size * pos[0], self.top + self.cell_size * pos[1],
                #     self.cell_size, self.cell_size), 0)
                screen.blit(image_flag, (self.left + self.cell_size * pos[0], self.top + self.cell_size * pos[1]))
                pygame.draw.rect(screen, (20, 200, 255), (
                    self.left + self.cell_size * pos[0], self.top + self.cell_size * pos[1],
                    self.cell_size, self.cell_size), 1)
            elif arr[pos[0]][pos[1]] == 10:
                arr[pos[0]][pos[1]] = -12
                screen.blit(image_flag, (self.left + self.cell_size * pos[0], self.top + self.cell_size * pos[1]))
                pygame.draw.rect(screen, (20, 200, 255), (
                    self.left + self.cell_size * pos[0], self.top + self.cell_size * pos[1],
                    self.cell_size, self.cell_size), 1)
                # pygame.draw.rect(screen, (255, 61, 51), (
                #     self.left + self.cell_size * pos[0], self.top + self.cell_size * pos[1],
                #     self.cell_size, self.cell_size), 0)
                # self.opened += 1
            elif arr[pos[0]][pos[1]] == -2:
                arr[pos[0]][pos[1]] = -1
                pygame.draw.rect(screen, color_pole, (
                    self.left + self.cell_size * pos[0], self.top + self.cell_size * pos[1],
                    self.cell_size, self.cell_size), 0)
                pygame.draw.rect(screen, (20, 200, 255), (
                    self.left + self.cell_size * pos[0], self.top + self.cell_size * pos[1],
                    self.cell_size, self.cell_size), 1)
            elif arr[pos[0]][pos[1]] == -12:
                arr[pos[0]][pos[1]] = 10
                pygame.draw.rect(screen, color_pole, (
                    self.left + self.cell_size * pos[0], self.top + self.cell_size * pos[1],
                    self.cell_size, self.cell_size), 0)
                pygame.draw.rect(screen, (20, 200, 255), (
                    self.left + self.cell_size * pos[0], self.top + self.cell_size * pos[1],
                    self.cell_size, self.cell_size), 1)

        if self.opened == self.width * self.height - h:
            obsh_igr += 1
            igr += 1
            f_win = 1
            if obsh_igr > best_igr:
                best_igr = obsh_igr

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
print(a)
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pass

            elif event.button == 3:
                print(event.pos)
                # board.get_click(event.pos, 1)
                board.get_click(event.pos, 0)
                # Bomb(all_sprites, event.pos)
        elif event.type == pygame.KEYDOWN :
            if event.key == 32:
                hokkey.vozvrat()

    with open('data/statistic.txt', 'w') as f1:
        f1.write(' '.join([str(x) for x in [time, comp, igr, best_comp, best_igr, lenqth]]))
    time += 0.04
    n += 1
    if f_win != 0:
        # y_win -= 20
        screen.blit(image_win, (150, y_win))
        if y_win <= 350:
            f_win = -1
            # y_win = 700
        if f_win == 1:
            y_win -= 20
        else:
            y_win += 40
        if y_win >= 700:
            f_win = 0
            y_win = 700
    if f_lose != 0:
        # y_lose += 20
        screen.blit(image_lose, (150, y_lose))
        if y_lose >= 0:
            f_lose = -1
            # print('a')
            # y_lose = -350
        if f_lose == 1:
            y_lose += 20
        else:
            # print('000')
            y_lose -= 40
        if y_lose <= -350:
            f_lose = 0
            y_lose = -350
    if n % 25 == 0:
        n = 0
        if pygame.mouse.get_focused():
            lenqth += int(((pos_last[0] - pygame.mouse.get_pos()[0]) ** 2 +
                           (pos_last[1] - pygame.mouse.get_pos()[1]) ** 2) ** 0.5)
        pos_last = pygame.mouse.get_pos()
        # print(lenqth // 3793)

    pygame.display.flip()
    clock.tick(25)
# print(time, comp, igr)
