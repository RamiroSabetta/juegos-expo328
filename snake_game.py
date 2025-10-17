# Importar librerías necesarias
import pygame
import time
import random
import sys

# Velocidad inicial de la serpiente
snake_speed = 15

# Tamaño de la ventana del juego
window_x = 720
window_y = 480

# Definición de colores
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Inicializar pygame
pygame.init()

# Crear ventana del juego
pygame.display.set_caption('Juego de la Serpiente')
game_window = pygame.display.set_mode((window_x, window_y))

# Controlador de FPS (fotogramas por segundo)
fps = pygame.time.Clock()

# Posición inicial de la serpiente
snake_position = [100, 50]

# Cuerpo inicial de la serpiente (4 bloques)
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

# Posición inicial de la fruta
fruit_position = [
    random.randrange(1, (window_x // 10)) * 10,
    random.randrange(1, (window_y // 10)) * 10
]
fruit_spawn = True

# Dirección inicial de la serpiente (derecha)
direction = 'RIGHT'
change_to = direction

# Puntaje inicial
score = 0

# Función para mostrar el puntaje y velocidad
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    speed_font = pygame.font.SysFont(font, size)

    score_surface = score_font.render('Puntaje: ' + str(score), True, color)
    speed_surface = speed_font.render('Velocidad: ' + str(snake_speed), True, color)

    # Posiciones del texto
    score_rect = score_surface.get_rect()
    speed_rect = speed_surface.get_rect()

    # Puntaje a la izquierda
    score_rect.topleft = (10, 10)
    # Velocidad a la derecha del puntaje
    speed_rect.topleft = (score_rect.right + 20, 10)

    # Dibujar en pantalla
    game_window.blit(score_surface, score_rect)
    game_window.blit(speed_surface, speed_rect)

# Función para reiniciar el juego cuando se pierde
def game_over():
    global snake_speed, snake_position, snake_body, fruit_position, fruit_spawn, direction, change_to, score

    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Tu puntaje fue: ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # Mostrar mensaje de "Game Over"
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # Pausa breve para mostrar el resultado
    time.sleep(2)

    # Reiniciar las variables del juego
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                      random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0
    snake_speed = 15

# Bucle principal del juego
while True:

    # Manejo de eventos (teclas y cierre de ventana)
    for event in pygame.event.get():
        # Si se presiona la cruz de la ventana, salir del juego
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Si se presiona una tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                change_to = 'UP'
            if event.key == pygame.K_s:
                change_to = 'DOWN'
            if event.key == pygame.K_a:
                change_to = 'LEFT'
            if event.key == pygame.K_d:
                change_to = 'RIGHT'

    # Evitar que la serpiente se mueva en direcciones opuestas
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Mover la serpiente según la dirección
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Agregar nueva posición al cuerpo de la serpiente
    snake_body.insert(0, list(snake_position))

    # Si la serpiente come la fruta
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
        # Aumentar la velocidad cada 10 puntos
        if score >= 10:
            snake_speed += 5
    else:
        snake_body.pop()

    # Generar nueva fruta si fue comida
    if not fruit_spawn:
        fruit_position = [
            random.randrange(1, (window_x // 10)) * 10,
            random.randrange(1, (window_y // 10)) * 10
        ]
    fruit_spawn = True

    # Dibujar fondo negro
    game_window.fill(black)

    # Dibujar la serpiente
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Dibujar la fruta
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Condiciones de "Game Over"
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Si la serpiente choca con su propio cuerpo
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Mostrar el puntaje y velocidad actual
    show_score(1, white, 'times new roman', 20)

    # Actualizar la pantalla
    pygame.display.update()

    # Controlar la velocidad del juego
    fps.tick(snake_speed)