import pygame
import random

# Inicializamos Pygame
pygame.init()

# Tamaño de la pantalla
ANCHO = 300
ALTO = 600
TAM_BLOQUE = 30  # Tamaño de cada cuadrado del bloque

# Colores (RGB)
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

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("TETRIS")

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Figuras del Tetris
FIGURAS = [
    [[1, 1, 1, 1]],                    # I
    [[1, 1], [1, 1]],                  # O
    [[0, 1, 0], [1, 1, 1]],            # T
    [[1, 0, 0], [1, 1, 1]],            # L
    [[0, 0, 1], [1, 1, 1]],            # J
    [[1, 1, 0], [0, 1, 1]],            # S
    [[0, 1, 1], [1, 1, 0]]             # Z
]

COLORES = [CIAN, AMARILLO, MAGENTA, NARANJA, AZUL, VERDE, ROJO]

# Clase Pieza
class Pieza:
    def __init__(self, x, y, figura, color):
        self.x = x
        self.y = y
        self.figura = figura
        self.color = color

    def rotar(self):
        # Rotar la figura (transposición + inversión de filas)
        self.figura = [list(fila) for fila in zip(*self.figura[::-1])]

# Función para crear una nueva pieza
def nueva_pieza():
    i = random.randint(0, len(FIGURAS) - 1)
    return Pieza(ANCHO // TAM_BLOQUE // 2 - 2, 0, FIGURAS[i], COLORES[i])

# Crear el tablero (20 filas x 10 columnas)
FILAS = ALTO // TAM_BLOQUE
COLUMNAS = ANCHO // TAM_BLOQUE
tablero = [[NEGRO for _ in range(COLUMNAS)] for _ in range(FILAS)]

pieza_actual = nueva_pieza()
juego_terminado = False
caida_tiempo = 0
velocidad_caida = 500  # milisegundos
puntaje = 0

# Función para comprobar si la pieza puede moverse
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

# Fijar la pieza al tablero
def fijar_pieza(pieza):
    global tablero, puntaje
    for y, fila in enumerate(pieza.figura):
        for x, valor in enumerate(fila):
            if valor and pieza.y + y >= 0:
                tablero[pieza.y + y][pieza.x + x] = pieza.color
    eliminar_filas_completas()

# Eliminar filas llenas
def eliminar_filas_completas():
    global tablero, puntaje
    nuevas_filas = [fila for fila in tablero if any(c == NEGRO for c in fila)]
    filas_eliminadas = FILAS - len(nuevas_filas)
    puntaje += filas_eliminadas * 100
    for _ in range(filas_eliminadas):
        nuevas_filas.insert(0, [NEGRO for _ in range(COLUMNAS)])
    tablero[:] = nuevas_filas

# Dibujar el tablero y la pieza
def dibujar_todo():
    pantalla.fill(NEGRO)
    # Dibujar tablero
    for y in range(FILAS):
        for x in range(COLUMNAS):
            pygame.draw.rect(pantalla, tablero[y][x],
                             (x * TAM_BLOQUE, y * TAM_BLOQUE, TAM_BLOQUE, TAM_BLOQUE), 0)
            pygame.draw.rect(pantalla, GRIS,
                             (x * TAM_BLOQUE, y * TAM_BLOQUE, TAM_BLOQUE, TAM_BLOQUE), 1)
    # Dibujar pieza actual
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
    # Mostrar puntaje
    fuente = pygame.font.SysFont("Arial", 24)
    texto = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
    pantalla.blit(texto, (10, 10))
    pygame.display.flip()


# Bucle principal del juego
while not juego_terminado:
    tiempo_pasado = clock.tick(30)
    caida_tiempo += tiempo_pasado

    # Movimiento automático hacia abajo
    if caida_tiempo > velocidad_caida:
        if not colision(pieza_actual, 0, 1):
            pieza_actual.y += 1
        else:
            fijar_pieza(pieza_actual)
            pieza_actual = nueva_pieza()
            if colision(pieza_actual, 0, 0):
                juego_terminado = True
        caida_tiempo = 0

    # Eventos
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
                # Rotar la pieza
                pieza_actual.rotar()
                if colision(pieza_actual, 0, 0):  # Deshacer si hay colisión
                    for _ in range(3):
                        pieza_actual.rotar()

    dibujar_todo()

# Pantalla final
pantalla.fill(NEGRO)
fuente = pygame.font.SysFont("Arial", 36)
texto = fuente.render("GAME OVER", True, ROJO)
pantalla.blit(texto, (ANCHO // 2 - 100, ALTO // 2 - 30))
pygame.display.flip()
pygame.time.wait(2000)
pygame.quit()
