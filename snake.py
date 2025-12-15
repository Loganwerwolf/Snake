import pygame
import time
import random

pygame.init()


# Colores
blanco = (255, 255, 255) 
amarillo = (255, 255, 102)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Tamaño de la pantalla
ancho = 600
alto = 400
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Snake - Juego Clásico')

# Reloj
reloj = pygame.time.Clock()
velocidad_snake = 15

# Tamaño del bloque
tam_bloque = 10

# Fuente
fuente = pygame.font.SysFont("bahnschrift", 25)
fuente_puntaje = pygame.font.SysFont("comicsansms", 35)

def puntaje(valor):
    texto = fuente_puntaje.render(f"Puntaje: {valor}", True, amarillo)
    pantalla.blit(texto, [0, 0])

def snake(tam_bloque, lista_snake):
    for x in lista_snake:
        pygame.draw.rect(pantalla, verde, [x[0], x[1], tam_bloque, tam_bloque])

def mensaje(msg, color):
    texto = fuente.render(msg, True, color)
    pantalla.blit(texto, [ancho / 6, alto / 3])

def juego():
    fin_juego = False
    game_over = False

    x1 = ancho / 2
    y1 = alto / 2

    x1_cambio = 0
    y1_cambio = 0

    lista_snake = []
    longitud_snake = 1

    comida_x = round(random.randrange(0, ancho - tam_bloque) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto - tam_bloque) / 10.0) * 10.0

    while not fin_juego:

        while game_over:
            pantalla.fill(azul)
            mensaje("Perdiste! Presiona C-Continuar o Q-Salir", rojo)
            puntaje(longitud_snake - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fin_juego = True
                        game_over = False
                    if evento.key == pygame.K_c:
                        juego()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fin_juego = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_cambio = -tam_bloque
                    y1_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_cambio = tam_bloque
                    y1_cambio = 0
                elif evento.key == pygame.K_UP:
                    y1_cambio = -tam_bloque
                    x1_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y1_cambio = tam_bloque
                    x1_cambio = 0

        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            game_over = True

        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(azul)
        pygame.draw.rect(pantalla, rojo, [comida_x, comida_y, tam_bloque, tam_bloque])
        cabeza_snake = []
        cabeza_snake.append(x1)
        cabeza_snake.append(y1)
        lista_snake.append(cabeza_snake)
        if len(lista_snake) > longitud_snake:
            del lista_snake[0]

        for x in lista_snake[:-1]:
            if x == cabeza_snake:
                game_over = True

        snake(tam_bloque, lista_snake)
        puntaje(longitud_snake - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho - tam_bloque) / 10.0) * 10.0
            comida_y = round(random.randrange(0, alto - tam_bloque) / 10.0) * 10.0
            longitud_snake += 1

        reloj.tick(velocidad_snake)

    pygame.quit()
    quit()

juego()