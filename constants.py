from pygame.transform import scale
from pygame.image import load
from os.path import join


WIDTH, HEIGHT = 1080, 720
ROWS, COLS = 17, 17
SQUARE_SIZE_16 = 29
AREA_SQUARE_16 = (SQUARE_SIZE_16, SQUARE_SIZE_16)
SQUARE_SIZE_10 = 40
AREA_SQUARE_10 = (SQUARE_SIZE_10, SQUARE_SIZE_10)
WHITE = (255,255,255)


# coord y dim imagenes
INICIAR_COORDS = (338, 247)
CARGAR_COORDS =(338, 363)
GUARDAR_COORDS = (338, 479)
SALIR_COORDS = (338, 595)
BOTON_MENU_DIM = (400, 52)


CONTINUAR_COORDS = (448, 537)
CONTINUAR_DIM = (187, 57)


CUAD_16_COORDS = (409.5,269)
CUAD_10_COORDS = (568.25,277.5)
BOTON_CUAD_DIM = (109,42)

BOTON_BARCOS_2_COORDS = (430.5,395)
BOTON_BARCOS_3_COORDS = (492.25,396.25)
BOTON_BARCOS_4_COORDS = (552,393.75)
BOTON_BARCOS_5_COORDS = (614,395.75)
BOTON_BARCOS_DIM = (36,47)

BOTON_PLAYERS_1_DIM = (41,52)
BOTON_PLAYERS_1_COORDS = (477.75,508.75)
BOTON_PLAYERS_2_COORDS = (561.75,508.75)

BOTON_JUGAR_COORDS = (484,593.25)
BOTON_JUGAR_DIM = (109,47)

VICTORIA_DIM = (558,712)


ANIMACION_DIM_TITULO = (128,128)
ANIMACION_COORDS_TITULO = (1845/4,1184/4)
ANIMACION_DIM_OPTIONS = (64,64)
ANIMACION_COORDS_OPTIONS = (2024/4,500/4)


# imagenes
BOTON_CONTINUAR = scale(load(join("imagenes", "boton_continuar.png")), CONTINUAR_DIM)


BOTON_INICIAR_PARTIDA = scale(load(join("imagenes", "boton_nueva_partida.png")), BOTON_MENU_DIM)
BOTON_CARGAR_PARTIDA = scale(load(join("imagenes", "boton_cargar_partida.png")), BOTON_MENU_DIM)
BOTON_GUARDAR_PARTIDA = scale(load(join("imagenes", "boton_guardar_partida.png")), BOTON_MENU_DIM)
BOTON_SALIR = scale(load(join("imagenes", "boton_salir.png")), BOTON_MENU_DIM)


BOTON_CUAD_16 = scale(load(join("imagenes", "boton_cuad_16.png")), BOTON_CUAD_DIM)
BOTON_CUAD_10 = scale(load(join("imagenes", "boton_cuad_10.png")), BOTON_CUAD_DIM)
BOTON_BARCOS_1 = scale(load(join("imagenes", "boton_1.png")), BOTON_PLAYERS_1_DIM)
BOTON_BARCOS_2 = scale(load(join("imagenes", "boton_barcos_2.png")), BOTON_BARCOS_DIM)
BOTON_BARCOS_3 = scale(load(join("imagenes", "boton_barcos_3.png")), BOTON_BARCOS_DIM)
BOTON_BARCOS_4 = scale(load(join("imagenes", "boton_barcos_4.png")), BOTON_BARCOS_DIM)
BOTON_BARCOS_5 = scale(load(join("imagenes", "boton_barcos_5.png")), BOTON_BARCOS_DIM)
BOTON_JUGAR = scale(load(join("imagenes", "boton_jugar.png")), BOTON_JUGAR_DIM)

VICTORIA = scale(load(join("imagenes", "victoria.png")), VICTORIA_DIM)

SALIR_EASTER_EGG = scale(load(join("imagenes", "salir_easter_egg.png")), (767//6, 223//6))
