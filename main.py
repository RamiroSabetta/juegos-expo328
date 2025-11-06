import tkinter as tk
from tkinter import messagebox
import threading
import pygame
import time
import random
import sys

# ============================================
# JUEGOS INCLUIDOS
# ============================================

def run_snake_game():
    """Juego Snake"""
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
    
    # Inicializar pygame
    pygame.init()
    
    # Crear ventana del juego
    pygame.display.set_caption('Juego de la Serpiente')
    game_window = pygame.display.set_mode((window_x, window_y))
    
    # Controlador de FPS
    fps = pygame.time.Clock()
    
    # Posición inicial de la serpiente
    snake_position = [100, 50]
    
    # Cuerpo inicial de la serpiente
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    
    # Posición inicial de la fruta
    fruit_position = [
        random.randrange(1, (window_x // 10)) * 10,
        random.randrange(1, (window_y // 10)) * 10
    ]
    fruit_spawn = True
    
    # Dirección inicial
    direction = 'RIGHT'
    change_to = direction
    
    # Puntaje inicial
    score = 0
    
    def show_score(choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        speed_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Puntaje: ' + str(score), True, color)
        speed_surface = speed_font.render('Velocidad: ' + str(snake_speed), True, color)
        score_rect = score_surface.get_rect()
        speed_rect = speed_surface.get_rect()
        score_rect.topleft = (10, 10)
        speed_rect.topleft = (score_rect.right + 20, 10)
        game_window.blit(score_surface, score_rect)
        game_window.blit(speed_surface, speed_rect)
    
    def game_over():
        nonlocal snake_speed, snake_position, snake_body, fruit_position, fruit_spawn, direction, change_to, score
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('Tu puntaje fue: ' + str(score), True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x / 2, window_y / 4)
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        snake_position = [100, 50]
        snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        fruit_position = [
            random.randrange(1, (window_x // 10)) * 10,
            random.randrange(1, (window_y // 10)) * 10
        ]
        fruit_spawn = True
        direction = 'RIGHT'
        change_to = direction
        score = 0
        snake_speed = 15
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
        
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10
        
        snake_body.insert(0, list(snake_position))
        
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
            if score >= 10:
                snake_speed += 5
        else:
            snake_body.pop()
        
        if not fruit_spawn:
            fruit_position = [
                random.randrange(1, (window_x // 10)) * 10,
                random.randrange(1, (window_y // 10)) * 10
            ]
        fruit_spawn = True
        
        game_window.fill(black)
        
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        
        pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
        
        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()
        
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()
        
        show_score(1, white, 'times new roman', 20)
        pygame.display.update()
        fps.tick(snake_speed)
    
    pygame.quit()


def run_tetris_game():
    """Juego Tetris"""
    pygame.init()
    
    ANCHO = 300
    ALTO = 600
    TAM_BLOQUE = 30
    
    NEGRO = (0, 0, 0)
    GRIS = (100, 100, 100)
    BLANCO = (255, 255, 255)
    ROJO = (255, 0, 0)
    VERDE = (0, 255, 0)
    AZUL = (0, 0, 255)
    CIAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    AMARILLO = (255, 255, 0)
    NARANJA = (255, 165, 0)
    
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("TETRIS")
    clock = pygame.time.Clock()
    
    FIGURAS = [
        [[1, 1, 1, 1]], [[1, 1], [1, 1]], [[0, 1, 0], [1, 1, 1]],
        [[1, 0, 0], [1, 1, 1]], [[0, 0, 1], [1, 1, 1]],
        [[1, 1, 0], [0, 1, 1]], [[0, 1, 1], [1, 1, 0]]
    ]
    COLORES = [CIAN, AMARILLO, MAGENTA, NARANJA, AZUL, VERDE, ROJO]
    
    class Pieza:
        def __init__(self, x, y, figura, color):
            self.x = x
            self.y = y
            self.figura = figura
            self.color = color
        
        def rotar(self):
            self.figura = [list(fila) for fila in zip(*self.figura[::-1])]
    
    def nueva_pieza():
        i = random.randint(0, len(FIGURAS) - 1)
        return Pieza(ANCHO // TAM_BLOQUE // 2 - 2, 0, FIGURAS[i], COLORES[i])
    
    FILAS = ALTO // TAM_BLOQUE
    COLUMNAS = ANCHO // TAM_BLOQUE
    tablero = [[NEGRO for _ in range(COLUMNAS)] for _ in range(FILAS)]
    
    pieza_actual = nueva_pieza()
    juego_terminado = False
    caida_tiempo = 0
    velocidad_caida = 500
    puntaje = 0
    
    def colision(pieza, dx, dy):
        for y, fila in enumerate(pieza.figura):
            for x, valor in enumerate(fila):
                if valor:
                    nuevo_x = pieza.x + x + dx
                    nuevo_y = pieza.y + y + dy
                    if nuevo_x < 0 or nuevo_x >= COLUMNAS or nuevo_y >= FILAS:
                        return True
                    if nuevo_y >= 0 and tablero[nuevo_y][nuevo_x] != NEGRO:
                        return True
        return False
    
    def fijar_pieza(pieza):
        nonlocal tablero, puntaje
        for y, fila in enumerate(pieza.figura):
            for x, valor in enumerate(fila):
                if valor and pieza.y + y >= 0:
                    tablero[pieza.y + y][pieza.x + x] = pieza.color
        eliminar_filas_completas()
    
    def eliminar_filas_completas():
        nonlocal tablero, puntaje
        nuevas_filas = [fila for fila in tablero if any(c == NEGRO for c in fila)]
        filas_eliminadas = FILAS - len(nuevas_filas)
        puntaje += filas_eliminadas * 100
        for _ in range(filas_eliminadas):
            nuevas_filas.insert(0, [NEGRO for _ in range(COLUMNAS)])
        tablero[:] = nuevas_filas
    
    def dibujar_todo():
        pantalla.fill(NEGRO)
        for y in range(FILAS):
            for x in range(COLUMNAS):
                pygame.draw.rect(pantalla, tablero[y][x],
                               (x * TAM_BLOQUE, y * TAM_BLOQUE, TAM_BLOQUE, TAM_BLOQUE), 0)
                pygame.draw.rect(pantalla, GRIS,
                               (x * TAM_BLOQUE, y * TAM_BLOQUE, TAM_BLOQUE, TAM_BLOQUE), 1)
        for y, fila in enumerate(pieza_actual.figura):
            for x, valor in enumerate(fila):
                if valor:
                    pygame.draw.rect(pantalla, pieza_actual.color,
                                   ((pieza_actual.x + x) * TAM_BLOQUE,
                                    (pieza_actual.y + y) * TAM_BLOQUE,
                                    TAM_BLOQUE, TAM_BLOQUE), 0)
                    pygame.draw.rect(pantalla, GRIS,
                                   ((pieza_actual.x + x) * TAM_BLOQUE,
                                    (pieza_actual.y + y) * TAM_BLOQUE,
                                    TAM_BLOQUE, TAM_BLOQUE), 1)
        fuente = pygame.font.SysFont("Arial", 24)
        texto = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
        pantalla.blit(texto, (10, 10))
        pygame.display.flip()
    
    while not juego_terminado:
        tiempo_pasado = clock.tick(30)
        caida_tiempo += tiempo_pasado
        
        if caida_tiempo > velocidad_caida:
            if not colision(pieza_actual, 0, 1):
                pieza_actual.y += 1
            else:
                fijar_pieza(pieza_actual)
                pieza_actual = nueva_pieza()
                if colision(pieza_actual, 0, 0):
                    juego_terminado = True
            caida_tiempo = 0
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_terminado = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and not colision(pieza_actual, -1, 0):
                    pieza_actual.x -= 1
                elif evento.key == pygame.K_RIGHT and not colision(pieza_actual, 1, 0):
                    pieza_actual.x += 1
                elif evento.key == pygame.K_DOWN and not colision(pieza_actual, 0, 1):
                    pieza_actual.y += 1
                elif evento.key == pygame.K_UP:
                    pieza_actual.rotar()
                    if colision(pieza_actual, 0, 0):
                        for _ in range(3):
                            pieza_actual.rotar()
        
        dibujar_todo()
    
    pantalla.fill(NEGRO)
    fuente = pygame.font.SysFont("Arial", 36)
    texto = fuente.render("Juego Terminado", True, ROJO)
    pantalla.blit(texto, (ANCHO // 2 - 100, ALTO // 2 - 30))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()


def run_pong_game():
    """Juego Pong 1 VS 1"""
    pygame.init()
    
    font20 = pygame.font.Font(None, 20)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    
    WIDTH, HEIGHT = 720, 480
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong 1 VS 1")
    clock = pygame.time.Clock()
    FPS = 30
    
    class Striker:
        def __init__(self, posx, posy, width, height, speed, color):
            self.posx = posx
            self.posy = posy
            self.width = width
            self.height = height
            self.speed = speed
            self.color = color
            self.geekRect = pygame.Rect(posx, posy, width, height)
            self.geek = pygame.draw.rect(screen, self.color, self.geekRect)
        
        def display(self):
            self.geek = pygame.draw.rect(screen, self.color, self.geekRect)
        
        def update(self, yFac):
            self.posy = self.posy + self.speed*yFac
            if self.posy <= 0:
                self.posy = 0
            elif self.posy + self.height >= HEIGHT:
                self.posy = HEIGHT-self.height
            self.geekRect = (self.posx, self.posy, self.width, self.height)
        
        def displayScore(self, text, score, x, y, color):
            text = font20.render(text+str(score), True, color)
            textRect = text.get_rect()
            textRect.center = (x, y)
            screen.blit(text, textRect)
        
        def getRect(self):
            return self.geekRect
    
    class Ball:
        def __init__(self, posx, posy, radius, speed, color):
            self.posx = posx
            self.posy = posy
            self.radius = radius
            self.speed = speed
            self.color = color
            self.xFac = 1
            self.yFac = -1
            self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
            self.firstTime = 1
        
        def display(self):
            self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
        
        def update(self):
            self.posx += self.speed*self.xFac
            self.posy += self.speed*self.yFac
            if self.posy <= 0 or self.posy >= HEIGHT:
                self.yFac *= -1
            if self.posx <= 0 and self.firstTime:
                self.firstTime = 0
                return 1
            elif self.posx >= WIDTH and self.firstTime:
                self.firstTime = 0
                return -1
            else:
                return 0
        
        def reset(self):
            self.posx = WIDTH//2
            self.posy = HEIGHT//2
            self.xFac *= -1
            self.firstTime = 1
        
        def hit(self):
            self.xFac *= -1
        
        def getRect(self):
            return self.ball
    
    running = True
    geek1 = Striker(20, 0, 10, 100, 10, GREEN)
    geek2 = Striker(WIDTH-30, 0, 10, 100, 10, GREEN)
    ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)
    listOfGeeks = [geek1, geek2]
    geek1Score, geek2Score = 0, 0
    geek1YFac, geek2YFac = 0, 0
    
    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    geek2YFac = -1
                if event.key == pygame.K_DOWN:
                    geek2YFac = 1
                if event.key == pygame.K_w:
                    geek1YFac = -1
                if event.key == pygame.K_s:
                    geek1YFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    geek2YFac = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    geek1YFac = 0
        
        for geek in listOfGeeks:
            if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
                ball.hit()
        
        geek1.update(geek1YFac)
        geek2.update(geek2YFac)
        point = ball.update()
        
        if point == -1:
            geek1Score += 1
        elif point == 1:
            geek2Score += 1
        
        if point:
            ball.reset()
        
        geek1.display()
        geek2.display()
        ball.display()
        
        geek1.displayScore("Jugador 1: ", geek1Score, 100, 20, WHITE)
        geek2.displayScore("Jugador 2: ", geek2Score, WIDTH-100, 20, WHITE)
        
        pygame.display.update()
        clock.tick(FPS)
    
    pygame.quit()


def run_brick_breaker_game():
    """Juego Brick Breaker"""
    pygame.init()
    
    WIDTH, HEIGHT = 720, 480
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    
    font = pygame.font.Font(None, 15)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Block Breaker")
    clock = pygame.time.Clock()
    FPS = 30
    
    class Striker:
        def __init__(self, posx, posy, width, height, speed, color):
            self.posx, self.posy = posx, posy
            self.width, self.height = width, height
            self.speed = speed
            self.color = color
            self.strikerRect = pygame.Rect(self.posx, self.posy, self.width, self.height)
            self.striker = pygame.draw.rect(screen, self.color, self.strikerRect)
        
        def display(self):
            self.striker = pygame.draw.rect(screen, self.color, self.strikerRect)
        
        def update(self, xFac):
            self.posx += self.speed*xFac
            if self.posx <= 0:
                self.posx = 0
            elif self.posx+self.width >= WIDTH:
                self.posx = WIDTH-self.width
            self.strikerRect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        
        def getRect(self):
            return self.strikerRect
    
    class Block:
        def __init__(self, posx, posy, width, height, color):
            self.posx, self.posy = posx, posy
            self.width, self.height = width, height
            self.color = color
            self.damage = 100
            if color == WHITE:
                self.health = 200
            else:
                self.health = 100
            self.blockRect = pygame.Rect(self.posx, self.posy, self.width, self.height)
            self.block = pygame.draw.rect(screen, self.color, self.blockRect)
        
        def display(self):
            if self.health > 0:
                self.brick = pygame.draw.rect(screen, self.color, self.blockRect)
        
        def hit(self):
            self.health -= self.damage
        
        def getRect(self):
            return self.blockRect
        
        def getHealth(self):
            return self.health
    
    class Ball:
        def __init__(self, posx, posy, radius, speed, color):
            self.posx, self.posy = posx, posy
            self.radius = radius
            self.speed = speed
            self.color = color
            self.xFac, self.yFac = 1, 1
            self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
        
        def display(self):
            self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
        
        def update(self):
            self.posx += self.xFac*self.speed
            self.posy += self.yFac*self.speed
            if self.posx <= 0 or self.posx >= WIDTH:
                self.xFac *= -1
            if self.posy <= 0:
                self.yFac *= -1
            if self.posy >= HEIGHT:
                return True
            return False
        
        def reset(self):
            self.posx = 0
            self.posy = HEIGHT
            self.xFac, self.yFac = 1, -1
        
        def hit(self):
            self.yFac *= -1
        
        def getRect(self):
            return self.ball
    
    def collisionChecker(rect, ball):
        if pygame.Rect.colliderect(rect, ball):
            return True
        return False
    
    def populateBlocks(blockWidth, blockHeight, horizontalGap, verticalGap):
        listOfBlocks = []
        for i in range(0, WIDTH, blockWidth+horizontalGap):
            for j in range(0, HEIGHT//2, blockHeight+verticalGap):
                listOfBlocks.append(Block(i, j, blockWidth, blockHeight, random.choice([WHITE, GREEN])))
        return listOfBlocks
    
    def gameOver():
        # Mostrar mensaje de game over
        gameOverFont = pygame.font.Font(None, 36)
        messageText = gameOverFont.render("Te quedaste sin intentos", True, WHITE)
        messageRect = messageText.get_rect()
        messageRect.center = (WIDTH // 2, HEIGHT // 2)
        
        screen.fill(BLACK)
        screen.blit(messageText, messageRect)
        pygame.display.update()
        
        # Esperar 2 segundos o hasta que se presione espacio
        waiting = True
        start_time = pygame.time.get_ticks()
        while waiting:
            current_time = pygame.time.get_ticks()
            if current_time - start_time > 2000:  # 2 segundos
                return True
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return True
    
    running = True
    lives = 3
    score = 0
    
    scoreText = font.render("Puntos", True, WHITE)
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.topleft = (10, HEIGHT-25)
    
    livesText = font.render("Vidas", True, WHITE)
    livesTextRect = livesText.get_rect()
    livesTextRect.topleft = (120, HEIGHT-25)
    
    striker = Striker(0, HEIGHT-50, 100, 20, 10, WHITE)
    strikerXFac = 0
    ball = Ball(0, HEIGHT-150, 7, 5, WHITE)
    blockWidth, blockHeight = 40, 15
    horizontalGap, verticalGap = 20, 20
    listOfBlocks = populateBlocks(blockWidth, blockHeight, horizontalGap, verticalGap)
    
    while running:
        screen.fill(BLACK)
        screen.blit(scoreText, scoreTextRect)
        screen.blit(livesText, livesTextRect)
        
        scoreText = font.render("Puntos : " + str(score), True, WHITE)
        livesText = font.render("Vidas : " + str(lives), True, WHITE)
        
        if not listOfBlocks:
            listOfBlocks = populateBlocks(blockWidth, blockHeight, horizontalGap, verticalGap)
        
        if lives <= 0:
            shouldContinue = gameOver()
            if not shouldContinue:
                running = False
                break
            # Reiniciar el juego
            while listOfBlocks:
                listOfBlocks.pop(0)
            lives = 3
            score = 0
            striker = Striker(0, HEIGHT-50, 100, 20, 10, WHITE)
            strikerXFac = 0
            ball = Ball(0, HEIGHT-150, 7, 5, WHITE)
            listOfBlocks = populateBlocks(blockWidth, blockHeight, horizontalGap, verticalGap)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    strikerXFac = -1
                if event.key == pygame.K_RIGHT:
                    strikerXFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    strikerXFac = 0
        
        if collisionChecker(striker.getRect(), ball.getRect()):
            ball.hit()
        for block in listOfBlocks:
            if collisionChecker(block.getRect(), ball.getRect()):
                ball.hit()
                block.hit()
                if block.getHealth() <= 0:
                    listOfBlocks.pop(listOfBlocks.index(block))
                    score += 5
        
        striker.update(strikerXFac)
        lifeLost = ball.update()
        
        if lifeLost:
            lives -= 1
            ball.reset()
        
        striker.display()
        ball.display()
        
        for block in listOfBlocks:
            block.display()
        
        pygame.display.update()
        clock.tick(FPS)
    
    pygame.quit()


# ============================================
# INTERFAZ PRINCIPAL
# ============================================

class GameLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Instituto de Formación Docente y Técnica N° 28 Anexo 328 - Norberto De La Riestra")
        self.root.geometry("1024x600")
        self.root.resizable(False, False)
        
        self.center_window()
        self.root.configure(bg='#2c3e50')
        
        title_label = tk.Label(
            self.root,
            text="EXPO 328",
            font=("Arial", 24, "bold"),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        title_label.pack(pady=30)
        
        subtitle_label = tk.Label(
            self.root,
            text="Selecciona un juego para jugar:",
            font=("Arial", 14),
            fg='#bdc3c7',
            bg='#2c3e50'
        )
        subtitle_label.pack(pady=10)
        
        button_frame = tk.Frame(self.root, bg='#2c3e50')
        button_frame.pack(pady=30)
        
        snake_button = tk.Button(
            button_frame,
            text="SNAKE",
            font=("Arial", 16, "bold"),
            bg='#27ae60',
            fg='white',
            width=15,
            height=2,
            command=self.launch_snake,
            relief='raised',
            bd=3,
            cursor='hand2'
        )
        snake_button.pack(pady=10)
        
        tetris_button = tk.Button(
            button_frame,
            text="TETRIS",
            font=("Arial", 16, "bold"),
            bg='#e74c3c',
            fg='white',
            width=15,
            height=2,
            command=self.launch_tetris,
            relief='raised',
            bd=3,
            cursor='hand2'
        )
        tetris_button.pack(pady=10)
        
        pong_button = tk.Button(
            button_frame,
            text="PONG 1 VS 1",
            font=("Arial", 16, "bold"),
            bg="#e4e73c",
            fg='white',
            width=15,
            height=2,
            command=self.launch_pong,
            relief='raised',
            bd=3,
            cursor='hand2'
        )
        pong_button.pack(pady=10)
        
        brick_button = tk.Button(
            button_frame,
            text="BRICK BREAKER",
            font=("Arial", 16, "bold"),
            bg="#5b65ec",
            fg='white',
            width=15,
            height=2,
            command=self.launch_brick,
            relief='raised',
            bd=3,
            cursor='hand2'
        )
        brick_button.pack(pady=10)
        
        exit_button = tk.Button(
            button_frame,
            text="SALIR",
            font=("Arial", 12),
            bg='#95a5a6',
            fg='white',
            width=10,
            height=1,
            command=self.exit_app,
            relief='raised',
            bd=2,
            cursor='hand2'
        )
        exit_button.pack(pady=20)
        
        controls_label = tk.Label(
            self.root,
            font=("Arial", 10),
            fg='#7f8c8d',
            bg='#2c3e50',
            justify='center'
        )
        controls_label.pack(side='bottom', pady=10)
    
    def center_window(self):
        """Centra la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 5) - (height // 5)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def launch_game(self, game_func):
        """Ejecuta un juego en un hilo separado"""
        try:
            self.root.withdraw()
            game_thread = threading.Thread(target=game_func, daemon=True)
            game_thread.start()
            game_thread.join()
            self.root.deiconify()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo ejecutar el juego: {str(e)}")
            self.root.deiconify()
    
    def launch_snake(self):
        """Ejecuta el juego Snake"""
        self.launch_game(run_snake_game)
    
    def launch_tetris(self):
        """Ejecuta el juego Tetris"""
        self.launch_game(run_tetris_game)
    
    def launch_pong(self):
        """Ejecuta el juego Pong"""
        self.launch_game(run_pong_game)
    
    def launch_brick(self):
        """Ejecuta el juego Brick Breaker"""
        self.launch_game(run_brick_breaker_game)
    
    def exit_app(self):
        """Cierra la aplicación"""
        if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?"):
            self.root.quit()


def main():
    """Función principal"""
    root = tk.Tk()
    app = GameLauncher(root)
    root.mainloop()


if __name__ == "__main__":
    main()
