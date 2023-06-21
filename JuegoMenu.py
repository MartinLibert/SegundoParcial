import pygame #proporciona funcionalidades para crear videojuegos y aplicaciones multimedia
import sys #proporciona acceso a algunas variables y funciones específicas del intérprete
import os #proporciona funciones para interactuar con el sistema operativo

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana del menu
ancho_pantalla = 800
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption("Menú del Juego")

# Cargar imagen de fondo
imagen_fondo = pygame.image.load("A:/Descargas/Wallpapers/Proyecto/cropped-800-600-430335.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, (ancho_pantalla, alto_pantalla))

# Cargar música de fondo
pygame.mixer.music.load("A:/Descargas/Wallpapers/Proyecto/DECO_27 - ゴーストルール feat. 初音ミク.mp3")
pygame.mixer.music.play(-1)  # Reproducir la música en bucle

# Colores
colorear_titulo = pygame.Color('white')
colorear_opciones = pygame.Color('pink')
colorear_marco = pygame.Color('white')

# Fuente para el texto del menú
fuente = pygame.font.Font("A:\Descargas\Wallpapers\Proyecto/font (1).ttf", 36)
fuente_titulo = pygame.font.Font("A:\Descargas\Wallpapers\Proyecto/font (1).ttf", 100)

# Opciones del menú
opciones = ["JUGAR", "LISTA SCORE", "SALIR"]
opcion_seleccionada = 0

def dibujar_menu():
    # Dibujar imagen de fondo
    pantalla.blit(imagen_fondo, (0, 0))
    
    # Renderizado del título
    titulo = fuente_titulo.render("MIKU TETRIS", True, colorear_titulo)
                                    #get_width() devuelve el ancho de una superficie en píxeles
    x_titulo = ancho_pantalla // 2 - titulo.get_width() // 2
                                    #get_height() se utiliza para obtener la altura en píxeles
    y_titulo = alto_pantalla // 4 - titulo.get_height() // 2
    pantalla.blit(titulo, (x_titulo, y_titulo))

    # Iterar sobre las opciones del menú
    for i, opcion in enumerate(opciones):
        # Renderizado de cada opción
        texto = fuente.render(opcion, True, colorear_opciones)
        x = ancho_pantalla // 2 - texto.get_width() // 2
        y = alto_pantalla // 2 - texto.get_height() // 2 + i * 50
        
        # Resaltado de la opción seleccionada con un marco
        if i == opcion_seleccionada:
            pygame.draw.rect(pantalla, colorear_marco, (x - 10, y - 10, texto.get_width() + 20, texto.get_height() + 20), 3)
        
        # Dibujar el texto de la opción
        pantalla.blit(texto, (x, y))

# Definición de la función mostrar_proximamente()
def mostrar_proximamente():
    # Crear una ventana de visualización
    ventana_proximamente = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Próximamente")
    
    # Cargar y redimensionar la imagen de fondo
    imagen_fondo_proximamente = pygame.image.load("A:/Descargas/Wallpapers/Proyecto/cropped-800-600-698074.png")
    imagen_fondo_proximamente = pygame.transform.scale(imagen_fondo_proximamente, (800, 600))
    
    # Crear una fuente para el texto
    fuente_proximamente = pygame.font.Font("A:\Descargas\Wallpapers\Proyecto/font (1).ttf", 50)
    
    # Renderizado del texto "PROXIMAMENTE"
    texto_proximamente = fuente_proximamente.render("PROXIMAMENTE", True, pygame.Color('black'))
    x_proximamente = 550 - texto_proximamente.get_width() // 2
    y_proximamente = 220 - texto_proximamente.get_height() // 2
    
    # Dibujar la imagen de fondo y el texto en la ventana
    ventana_proximamente.blit(imagen_fondo_proximamente, (0, 0))
    ventana_proximamente.blit(texto_proximamente, (x_proximamente, y_proximamente))
    
    # Actualizar la ventana de visualización
    pygame.display.flip()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.flip()
        
        if pygame.event.get(pygame.QUIT):
            pygame.quit()
            sys.exit()
        elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
            ejecutar_juego()
            

def ejecutar_juego():
    global opcion_seleccionada

    while True:
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    opcion_seleccionada = (opcion_seleccionada - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    opcion_seleccionada = (opcion_seleccionada + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    if opcion_seleccionada == 0:
                        pygame.quit()
                        ruta_juego = "A:/Descargas/Wallpapers/Proyecto/JuegoParcial.py"
                        # Coloca la ruta correcta del archivo del juego
                        os.system(f"python {ruta_juego}")
                    elif opcion_seleccionada == 1:
                        mostrar_proximamente()
                    elif opcion_seleccionada == 2:
                        pygame.quit()
                        sys.exit()

        dibujar_menu()
        pygame.display.flip()
# Iniciar el juego
ejecutar_juego()