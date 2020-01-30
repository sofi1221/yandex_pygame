import pygame

# инициализация Pygame:
pygame.init()
# размеры окна:
size = width, height = 1100, 700
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
color_end = (255, 255, 0)
color_font = (255, 0, 0)


# формирование кадра:
# команды рисования на холсте
def draw():
    screen.fill(color_end)
    # шрифты
    font1 = pygame.font.Font(None, 50)
    font2 = pygame.font.Font(None, 30)

    pygame.draw.rect(screen, color_font, (940, 640, 150, 50), 0)  # кнопка играть
    text = font1.render('Играть', 1, color_end)
    text_x = 940 + 75 - text.get_width() // 2
    text_y = 640 + 25 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))

    text = font1.render('Добро пожаловать в супер новую версию ваших любимых игр!', 1, color_font)
    text_x = width // 2 - text.get_width() // 2
    text_y = 25
    screen.blit(text, (text_x, text_y))
    text_y += text.get_height() + 20

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


# ...
draw()
# смена (отрисовка) кадра:
pygame.display.flip()

# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass  # завершение работы:
pygame.quit()
