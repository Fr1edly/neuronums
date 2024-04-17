import pygame
import sys

pygame.init()

# Настройки окна
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Draw a Number with Pygame")

# Цвета и шрифты
black = (0, 0, 0)
white = (255, 255, 255)
font_color = (0, 0, 255)
font = pygame.font.Font(None, 36)

# Заполнение фона
screen.fill(white)

drawing = False  # Флаг для отслеживания рисования
text_input = ""  # Текстовый ввод для имени файла
input_active = False  # Флаг активности текстового поля


def draw_text_input():
    text_surface = font.render(text_input, True, font_color)
    screen.blit(text_surface, (50, 550))


# Главный цикл приложения
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                drawing = True
            elif event.button == 3:  # Правая кнопка мыши для очистки экрана
                screen.fill(white)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
        elif event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode
                input_active = False  # Деактивировать ввод после нажатия Enter
            if event.key == pygame.K_RETURN:
                pygame.image.save(screen, f"./draws/{text_input}.png")
                pygame.quit()
            if event.key == pygame.K_s:  # Нажатие 's' активирует ввод
                input_active = True

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                pygame.draw.circle(screen, black, event.pos, 5)

    screen.fill(white, (0, 540, 800, 60))  # Очистка области ввода
    draw_text_input()  # Отрисовка текстового поля
    pygame.display.flip()
