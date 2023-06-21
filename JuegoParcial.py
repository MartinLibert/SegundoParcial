import pygame
from ClaseRecord import *
from copy import deepcopy
from random import choice, randrange

ANCHO, ALTO = 10, 20
TILE = 45
RESOLUCION_JUEGO = ANCHO * TILE, ALTO * TILE
RESOLUCION_VENTANA = 750, 940
FPS = 60
"record"
record = Record()

pygame.init()
sc = pygame.display.set_mode(RESOLUCION_VENTANA)
game_sc = pygame.Surface(RESOLUCION_JUEGO)
clock = pygame.time.Clock()

# Cargar música de fondo
pygame.mixer.music.load('A:/Descargas/Wallpapers/Proyecto/World Is Mine (osanime.com).mp3')
pygame.mixer.music.set_volume(0.3)  # Ajustar el volumen de la música (opcional)
pygame.mixer.music.play(-1)  # Reproducir la música en bucle


posiciones_figuras = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
                      [(0, -1), (-1, -1), (-1, 0), (0, 0)],
                      [(-1, 0), (-1, 1), (0, 0), (0, -1)],
                      [(0, 0), (-1, 0), (0, 1), (-1, -1)],
                      [(0, 0), (0, -1), (0, 1), (-1, -1)],
                      [(0, 0), (0, -1), (0, 1), (1, -1)],
                      [(0, 0), (0, -1), (0, 1), (-1, 0)]]

figuras = [[pygame.Rect(x + ANCHO // 2, y + 1, 1, 1) for x, y in posiciones] for posiciones in posiciones_figuras]
rectangulo_figura = pygame.Rect(0, 0, TILE - 2, TILE - 2)
tablero = [[0 for i in range(ANCHO)] for j in range(ALTO)]

contador_animacion, velocidad_animacion, limite_animacion = 0, 60, 2000
en_pausa = False

fondo = pygame.image.load('A:/Descargas/Wallpapers/Proyecto/cropped-750-940-519068.jpg').convert()
fondo_juego = pygame.image.load('A:/Descargas/Wallpapers/Proyecto/cropped-450-900-649991.png').convert()

fuente_principal = pygame.font.Font('A:\Descargas\Wallpapers\Proyecto/font (1).ttf', 65)
fuente = pygame.font.Font('A:\Descargas\Wallpapers\Proyecto/font (1).ttf', 45)

titulo_tetris = fuente_principal.render('Tetris', True, pygame.Color('cyan'))
titulo_puntaje = fuente.render('puntaje:', True, pygame.Color('cyan'))
titulo_record = fuente.render('RECORD', True, pygame.Color('cyan'))

obtener_color = lambda: (randrange(30, 100), randrange(120, 256), randrange(180, 256))

figura, siguiente_figura = deepcopy(choice(figuras)), deepcopy(choice(figuras))
color, siguiente_color = obtener_color(), obtener_color()

puntaje, lineas = 0, 0
puntajes = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(ANCHO) for y in range(ALTO)]

def verificar_bordes():
    if figura[i].x < 0 or figura[i].x > ANCHO - 1:
        return False
    elif figura[i].y > ALTO - 1 or tablero[figura[i].y][figura[i].x]:
        return False
    return True
        
def dibujar_menu_pausa():
    # ...
    # Dibujar el fondo del menú
    fondo_menu = pygame.image.load('A:/Descargas/Wallpapers/Proyecto/43 sin título_20230608125203.png').convert()
    nuevo_ancho = 300  # Nuevo ancho deseado
    nuevo_alto = 400  # Nuevo alto deseado
    fondo_menu = pygame.transform.scale(fondo_menu, (nuevo_ancho, nuevo_alto))
    sc.blit(fondo_menu, (200, 300))

    # Dibujar el texto de las opciones
    fuente = pygame.font.Font("A:\Descargas\Wallpapers\Proyecto/font (1).ttf", 24)
    texto_continuar = fuente.render('Continuar', True, pygame.Color(11, 86, 97))
    texto_salir = fuente.render('Salir', True, pygame.Color(11, 86, 97))

    sc.blit(texto_continuar, (280, 409))
    sc.blit(texto_salir, (315, 450))

    # Obtener la posición y tamaño de la hitbox de "Continuar"
    hitbox_continuar = texto_continuar.get_rect()
    hitbox_continuar.topleft = (280, 409)

    # Obtener la posición y tamaño de la hitbox de "Salir"
    hitbox_salir = texto_salir.get_rect()
    hitbox_salir.topleft = (315, 450)

    # Dibujar la hitbox de "Continuar"
    #pygame.draw.rect(sc, (0, 255, 0), hitbox_continuar, 2)

    # Dibujar la hitbox de "Salir"
    #pygame.draw.rect(sc, (0, 255, 0), hitbox_salir, 2)

    pygame.display.flip()
    
while True:
    record_actual = record.obtener_record()

    dx, rotar = 0, False
    
    if en_pausa:
        dibujar_menu_pausa()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    en_pausa = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print("Clic en", event.pos) Imprimir coordenadas del clic del mouse
                if 300 <= event.pos[0] <= 500:
                    if 345 <= event.pos[1] <= 426:
                        #print("Clic en Continuar")
                        en_pausa = False
                    elif 342 <= event.pos[1] <= 465:
                        #print("Clic en Salir")
                        exit()           
        continue
    
    sc.blit(fondo, (0, 0))
    sc.blit(game_sc, (20, 20))
    game_sc.blit(fondo_juego, (0, 0))
    
    # demora para líneas completas
    for i in range(lineas):
        pygame.time.wait(200)
    
    # control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                limite_animacion = 100
            elif event.key == pygame.K_SPACE:
                rotar = True
            elif event.key == pygame.K_ESCAPE:
                en_pausa = True
    
    # mover en x
    figura_antigua = deepcopy(figura)
    for i in range(4):
        figura[i].x += dx 
        if not verificar_bordes():
            figura = deepcopy(figura_antigua)
            break
    
    # mover en y
    contador_animacion += velocidad_animacion
    if contador_animacion > limite_animacion:
        contador_animacion = 0
        figura_antigua = deepcopy(figura)
        for i in range(4):
            figura[i].y += 1
            if not verificar_bordes():
                for i in range(4):
                    tablero[figura_antigua[i].y][figura_antigua[i].x] = color
                figura, color = siguiente_figura, siguiente_color
                siguiente_figura, siguiente_color = deepcopy(choice(figuras)), obtener_color()
                limite_animacion = 2000
                break
    
    # rotar
    centro = figura[0]
    figura_antigua = deepcopy(figura)
    if rotar:
        rotated_figura = [pygame.Rect(0, 0, 0, 0) for _ in range(4)]
        for i in range(4):
            x = figura[i].y - centro.y
            y = figura[i].x - centro.x
            rotated_figura[i].x = centro.x - x
            rotated_figura[i].y = centro.y + y
            if not verificar_bordes():
                figura = deepcopy(figura_antigua)
                break
        else:
            figura = deepcopy(rotated_figura)
    
    # verificar líneas completas
    linea, lineas = ALTO - 1, 0
    for fila in range(ALTO - 1, -1, -1):
        contador = 0
        for i in range(ANCHO):
            if tablero[fila][i]:
                contador += 1
            tablero[linea][i] = tablero[fila][i]
        if contador < ANCHO:
            linea -= 1
        else:
            velocidad_animacion += 3
            lineas += 1
    
    # calcular puntaje
    puntaje += puntajes[lineas]
    
    # dibujar cuadrícula
    [pygame.draw.rect(game_sc, (0, 0, 40), i_rect, 1) for i_rect in grid]
    
    # dibujar figura
    for i in range(4):
        rectangulo_figura.x = figura[i].x * TILE
        rectangulo_figura.y = figura[i].y * TILE
        pygame.draw.rect(game_sc, color, rectangulo_figura)
    
    # dibujar tablero
    for y, fila in enumerate(tablero):
        for x, col in enumerate(fila):
            if col:
                rectangulo_figura.x, rectangulo_figura.y = x * TILE, y * TILE
                pygame.draw.rect(game_sc, col, rectangulo_figura)
    
    # dibujar siguiente figura
    for i in range(4):
        rectangulo_figura.x = siguiente_figura[i].x * TILE + 380
        rectangulo_figura.y = siguiente_figura[i].y * TILE + 185
        pygame.draw.rect(sc, siguiente_color, rectangulo_figura)
    
    # dibujar títulos
    sc.blit(titulo_tetris, (500, 50))
    sc.blit(titulo_puntaje, (500, 340))
    sc.blit(fuente.render(str(puntaje), True, pygame.Color('gray')), (500, 420))
    sc.blit(titulo_record, (500, 500))
    sc.blit(fuente.render(str(record_actual), True, pygame.Color('gray')), (500, 590))
    
    # fin del juego
    for i in range(ANCHO):
        if tablero[0][i]:
            record.establecer_record(record_actual, puntaje)
            tablero = [[0 for i in range(ANCHO)] for i in range(ALTO)]
            contador_animacion, velocidad_animacion, limite_animacion = 0, 60, 2000
            puntaje = 0
            for i_rect in grid:
                pygame.draw.rect(game_sc, obtener_color(), i_rect)
                sc.blit(game_sc, (20, 20))
                pygame.display.flip()
                clock.tick(200)
    
    pygame.display.flip()
    clock.tick(FPS)
