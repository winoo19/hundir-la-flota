import pygame as pg 
from sys import exit
from os.path import join
from constants import *
from copy import deepcopy
from ast import literal_eval
from random import sample, choice


FPS = 60
# Animación del barco del título y del menu
DICT_FRAMES = {0: "f1.png", 1: "f2.png", 2: "f3.png", 3: "f4.png", 4: "f5.png", 5: "f6.png",
               6: "f7.png", 7: "f8.png", 8: "f9.png", 9: "f10.png", 10: "f11.png", 11: "f12.png"}

pg.init()
pg.font.init()
font = pg.font.Font(join("imagenes", "8514fix.fon"), 40)

TITULO = scale(load(join("imagenes", "fondo_titulo.png")), (WIDTH, HEIGHT))
OPTIONS = scale(load(join("imagenes", "fondo_options.png")), (WIDTH, HEIGHT))
MENU = scale(load(join("imagenes", "fondo_menu.png")), (WIDTH, HEIGHT))
EASTER_EGG = scale(load(join("imagenes", "fondo_easter_egg.png")), (WIDTH, HEIGHT))
GAMEBOARD_10 = scale(load(join("imagenes", "board10.png")), (WIDTH, HEIGHT))
GAMEBOARD_16 = scale(load(join("imagenes", "battleship_board.png")), (WIDTH, HEIGHT))


WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Hundir la flota")


def draw_barcos(boat, square_size):
    # dibuja los barcos completos(en colocación y cuando se hunden)

    AREA_SQUARE = (square_size, square_size)

    SPRITE_H_I = scale(load(join("imagenes", "hundido_h_i.png")), AREA_SQUARE)
    SPRITE_H_M = scale(load(join("imagenes", "hundido_h_m.png")), AREA_SQUARE)
    SPRITE_H_F = scale(load(join("imagenes", "hundido_h_f.png")), AREA_SQUARE)
    SPRITE_V_I = scale(load(join("imagenes", "hundido_v_i.png")), AREA_SQUARE)
    SPRITE_V_M = scale(load(join("imagenes", "hundido_v_m.png")), AREA_SQUARE)
    SPRITE_V_F = scale(load(join("imagenes", "hundido_v_f.png")), AREA_SQUARE)

    if boat[0][0] == boat[1][0]:
        vertical = True
    else:
        vertical = False
    for i, coord in enumerate(boat):
        if vertical:
            if i == 0:
                WIN.blit(SPRITE_V_I, coord)
            elif i == len(boat) - 1:
                WIN.blit(SPRITE_V_F, coord)
            else:
                WIN.blit(SPRITE_V_M, coord)
        else:
            if i == 0:
                WIN.blit(SPRITE_H_I, coord)
            elif i == len(boat) - 1:
                WIN.blit(SPRITE_H_F, coord)
            else:
                WIN.blit(SPRITE_H_M, coord)


def mostrar_barcos(barcos, hundidos, area_square):
    # muestra los barcos no hundidos cuando se acaba la partida

    SPRITE_H_I_NARANJA = scale(load(join("imagenes", "hundido_h_i_naranja.png")), area_square)
    SPRITE_H_M_NARANJA = scale(load(join("imagenes", "hundido_h_m_naranja.png")), area_square)
    SPRITE_H_F_NARANJA = scale(load(join("imagenes", "hundido_h_f_naranja.png")), area_square)
    SPRITE_V_I_NARANJA = scale(load(join("imagenes", "hundido_v_i_naranja.png")), area_square)
    SPRITE_V_M_NARANJA = scale(load(join("imagenes", "hundido_v_m_naranja.png")), area_square)
    SPRITE_V_F_NARANJA = scale(load(join("imagenes", "hundido_v_f_naranja.png")), area_square)

    for i, barco in enumerate(barcos):
        if i not in hundidos:
            if barco[0][0] == barco[1][0]:
                vertical = True
            else:
                vertical = False

            for num, casilla in enumerate(barco):
                if vertical:
                    if not num:
                        WIN.blit(SPRITE_V_I_NARANJA, casilla)
                        pg.display.update()
                        pg.time.delay(350)
                    elif num == len(barco)-1:
                        WIN.blit(SPRITE_V_F_NARANJA, casilla)
                        pg.display.update()
                        pg.time.delay(350)
                    else:
                        WIN.blit(SPRITE_V_M_NARANJA, casilla)
                        pg.display.update()
                        pg.time.delay(350)
                else:
                    if not num:
                        WIN.blit(SPRITE_H_I_NARANJA, casilla)
                        pg.display.update()
                        pg.time.delay(350)
                    elif num == len(barco)-1:
                        WIN.blit(SPRITE_H_F_NARANJA, casilla)
                        pg.display.update()
                        pg.time.delay(350)
                    else:
                        WIN.blit(SPRITE_H_M_NARANJA, casilla)
                        pg.display.update()
                        pg.time.delay(350)
    pg.time.delay(2000)


def draw_titulo(boton_continuar, frames):
    # Función del título, solo imprime una imagen, una animación y el botón continuar
    WIN.blit(TITULO, (0, 0))

    if boton_continuar:
        WIN.blit(BOTON_CONTINUAR, CONTINUAR_COORDS)
        
    WIN.blit(pg.transform.scale(pg.image.load(join("imagenes/Frames",
            DICT_FRAMES[frames//10])), ANIMACION_DIM_TITULO), ANIMACION_COORDS_TITULO)

    pg.display.update()


def draw_menu(boton_iniciar, boton_cargar, boton_guardar, boton_salir, boton_easter_egg, frames):
    # Las funciones draw solo imprimen las imágenes correspondientes
    WIN.blit(MENU, (0, 0))
    if boton_iniciar:
        WIN.blit(BOTON_INICIAR_PARTIDA, INICIAR_COORDS)
    if boton_cargar:
        WIN.blit(BOTON_CARGAR_PARTIDA, CARGAR_COORDS)
    if boton_guardar:
        WIN.blit(BOTON_GUARDAR_PARTIDA, GUARDAR_COORDS)
    if boton_salir:
        WIN.blit(BOTON_SALIR, SALIR_COORDS)

    WIN.blit(pg.transform.scale(pg.image.load(join("imagenes/Frames",
            DICT_FRAMES[frames//10])), ANIMACION_DIM_OPTIONS), ANIMACION_COORDS_OPTIONS)


def draw_easter_egg(frames, frames2):
    # es una función "draw": imprime imágenes en pantalla
    WIN.blit(EASTER_EGG, (0,0))

    mensaje = "Juego diseñado por Pepe y Dani"
    mensaje2 = "Esperamos que le guste"

    width, height = font.size(mensaje[:frames//10])
    text_surface = scale(font.render(mensaje[:frames//10], True, (160, 160, 160)), (2*width,2*height))
    WIN.blit(text_surface, ((WIDTH-5-2*width)/2, 300))

    width2, height2 = font.size(mensaje2[:frames2//10])
    text_surface2 = scale(font.render(mensaje2[:frames2//10], True, (160, 160, 160)), (2*width2,2*height2))
    WIN.blit(text_surface2, ((WIDTH-5-2*width2)/2, 400))

    if frames2 == 250:
        WIN.blit(SALIR_EASTER_EGG, (WIDTH//2-64, 500))

    pg.display.update()


def draw_options(cuadricula, cantidad_barcos, jugadores, jugar,
                 cuadricula_nueva, cantidad_barcos_nuevo, jugadores_nuevo, frames):
    # es una función "draw": imprime imágenes en pantalla
    WIN.blit(OPTIONS, (0, 0))

    for s in ((cuadricula, cantidad_barcos, jugadores),
              (cuadricula_nueva, cantidad_barcos_nuevo, jugadores_nuevo)):
        if s[0] == 16:
            WIN.blit(BOTON_CUAD_16, CUAD_16_COORDS)
        elif s[0] == 10:
            WIN.blit(BOTON_CUAD_10, CUAD_10_COORDS)

        if s[1] == 2:
            WIN.blit(BOTON_BARCOS_2, BOTON_BARCOS_2_COORDS)
        elif s[1] == 3:
            WIN.blit(BOTON_BARCOS_3, BOTON_BARCOS_3_COORDS)
        elif s[1] == 4:
            WIN.blit(BOTON_BARCOS_4, BOTON_BARCOS_4_COORDS)
        elif s[1] == 5:
            WIN.blit(BOTON_BARCOS_5, BOTON_BARCOS_5_COORDS)
        
        if s[2] == 1:
            WIN.blit(BOTON_BARCOS_1, BOTON_PLAYERS_1_COORDS)
        elif s[2] == 2:
            WIN.blit(BOTON_BARCOS_2, BOTON_PLAYERS_2_COORDS)
        
    WIN.blit(pg.transform.scale(pg.image.load(join("imagenes/Frames",
            DICT_FRAMES[frames//10])), ANIMACION_DIM_OPTIONS), ANIMACION_COORDS_OPTIONS)

    if jugar:
        WIN.blit(BOTON_JUGAR, BOTON_JUGAR_COORDS)

    pg.display.update()


def draw_gameboard(pressed_square, cuadrado_verde, boats, len_barco, casillas_agua,
                   casillas_tocado, barcos_hundidos_1, barcos_hundidos_2, boats_player_1,
                   boats_player_2, victoria, casillas_prov, frames, square_size, cuadricula, last_att_square):
    # Imprime el tablero según todas las condiciones dadas...
    cond = False

    AREA_SQUARE = (square_size, square_size)
    PRESSED_SQUARE = scale(load(join("imagenes", "casilla.png")), AREA_SQUARE)
    POSSIBLE_PLACEMENT = scale(load(join("imagenes", "casilla_naranja.png")), AREA_SQUARE)
    CASILLA_AGUA = scale(load(join("imagenes", "casilla_agua.png")), AREA_SQUARE)
    CASILLA_AGUA_NARANJA = scale(load(join("imagenes", "casilla_agua_naranja.png")), AREA_SQUARE)
    CASILLA_AGUA2 = scale(load(join("imagenes", "casilla_agua2.png")), AREA_SQUARE)
    CASILLA_AGUA2_NARANJA = scale(load(join("imagenes", "casilla_agua2_naranja.png")), AREA_SQUARE)
    CASILLA_TOCADO = scale(load(join("imagenes", "casilla_tocado.png")), AREA_SQUARE)
    CASILLA_TOCADO_NARANJA = scale(load(join("imagenes", "casilla_tocado_naranja.png")), AREA_SQUARE)

    if square_size == SQUARE_SIZE_16:
        WIN.blit(GAMEBOARD_16, (0, 0))
    else:
        WIN.blit(GAMEBOARD_10, (0, 0))
    WIN.blit(PRESSED_SQUARE, (pressed_square))  # cuadrado verde

    if len_barco != 8:
        if casillas_prov:
            for casilla in casillas_prov:
                WIN.blit(POSSIBLE_PLACEMENT, casilla[0])
            WIN.blit(PRESSED_SQUARE, (pressed_square))

        if cuadrado_verde:
            WIN.blit(PRESSED_SQUARE, cuadrado_verde)

        if len_barco != 10:
            
            width, height = font.size("Introduzca la posición de inicio y fin del barco de longitud 1")
            a = pg.transform.scale(font.render(f"Introduzca la posición de inicio y fin del barco de longitud {len_barco}",
             True, (0,0,0)), (width,height))
            WIN.blit(a, (230, 20))

        for boat in boats:
            if boat:
                draw_barcos(boat, square_size)

    else:
        for casilla in casillas_agua:
            if (frames//20)%2 == 0:
                WIN.blit(CASILLA_AGUA, casilla)
            else:
                WIN.blit(CASILLA_AGUA2, casilla)

        for casilla in casillas_tocado:
            WIN.blit(CASILLA_TOCADO, casilla)

        for num in barcos_hundidos_1:
            draw_barcos(boats_player_1[num], square_size)
            if last_att_square in boats_player_1[num]:
                cond = True

        for num in barcos_hundidos_2:
            draw_barcos(boats_player_2[num], square_size)

        if last_att_square and not cond:
            if last_att_square in casillas_agua:
                if (frames//20)%2 == 0:
                    WIN.blit(CASILLA_AGUA_NARANJA, last_att_square)
                else:
                    WIN.blit(CASILLA_AGUA2_NARANJA, last_att_square)
            elif last_att_square in casillas_tocado:
                WIN.blit(CASILLA_TOCADO_NARANJA, last_att_square)
            

        if victoria == -1:
            if cuadricula == 10:
                WIN.blit(VICTORIA, (500, 0))
            else:
                WIN.blit(VICTORIA, (540, 0))
            width, height = font.size("Jugador 1")
            a = pg.transform.scale(font.render("Jugador 1", True, (0,0,0)), (2*width,2*height))
            WIN.blit(a, (715,368))
            pg.draw.rect(WIN, WHITE, (0, 622, HEIGHT, 612))
            pg.display.update()
            mostrar_barcos(boats_player_1, barcos_hundidos_1, AREA_SQUARE)

        elif victoria == -2:
            WIN.blit(VICTORIA, (-33, 0))
            width, height = font.size("Jugador 2")
            a = pg.transform.scale(font.render("Jugador 2", True, (0,0,0)), (2*width,2*height))
            WIN.blit(a, (174,368))
            pg.draw.rect(WIN, WHITE, (500, 622, HEIGHT, 612))
            pg.display.update()
            mostrar_barcos(boats_player_2, barcos_hundidos_2, AREA_SQUARE)

    pg.display.update()


def colocacion_automatica(squares_2, cantidad_barcos, square_size):
    # Función que proporciona una colocación aleatoria a los barcos del ordenador
    boats_ai = []
    while not boats_ai:  # bucle hasta que seleccione una colocación correcta de barcos
        try:
            # elijo aleatoriamente tantas casillas de inicio de los barcos como cantidad de barcos hay
            starting_squares = sample(squares_2, cantidad_barcos)
            
            # genero las casillas posibles de final del barco, y elijo una aleatoriamente. Si no las hay, da error
            for i, square in enumerate(starting_squares):
                boats_ai.append(choice(casillas_y_barcos_correctos(square, i+2, boats_ai, square_size))[1])
        except:
            boats_ai = []
    return boats_ai


def ataque_automatico(squares_1, casillas_agua, casillas_tocado_1, barcos_restantes, square_size):
    # Función que hace ataques aleatorios hasta encontrar un barco que atacará a las casillas contiguas
    if square_size == 29:
        cuadricula = 16
    else:
        cuadricula = 10

    ataque, c_solo_tocadas, counter = (), [], 0
    casillas_tocado = casillas_tocado_1.copy()

    x_range = range(2*square_size, (cuadricula+2)*square_size)
    y_range = range((14+cuadricula)*square_size//6, (14+7*cuadricula)*square_size//6)

    # bucle hasta que seleccione una casilla no atacada
    while ataque in casillas_agua or ataque in casillas_tocado or not ataque:

        # encuentro las casillas que están tocadas pero no hundidas
        for barco in barcos_restantes:
            for casilla in barco:
                if casilla in casillas_tocado:
                    c_solo_tocadas.append(casilla)
        
        if c_solo_tocadas:  # si hay casillas solo tocadas, hago que ataque alrededor
            if len(c_solo_tocadas) != 1:
                
                # encuentro las casillas a los extremos del barco, las guardo en casillas posibles
                if c_solo_tocadas[0][0] == c_solo_tocadas[-1][0]:  # barco vertical
                    casillas_posibles = [(c_solo_tocadas[0][0], c_solo_tocadas[0][1]-square_size),
                                         (c_solo_tocadas[-1][0], c_solo_tocadas[-1][1]+square_size)]
                else:  # barco horizontal
                    casillas_posibles = [(c_solo_tocadas[0][0]-square_size, c_solo_tocadas[0][1]),
                                         (c_solo_tocadas[-1][0]+square_size, c_solo_tocadas[-1][1])]

                # miro a los extremos de la sucesión de casillas tocadas, si ambos extremos están cubiertos es que hay
                # varios barcos pegados, así que voy probando con cada casilla tocada hasta que haya alguna que no
                # esté rodeada por casillas ya tocadas: si una no funciona, entra en el except, donde aumento el counter
                # en uno, así que en la siguiente vuelta del bucle probará con la siguiente casilla
                p, f = casillas_posibles[0], casillas_posibles[1]
                if p not in casillas_agua and p not in casillas_tocado and p[0] in x_range and p[1] in y_range:
                    ataque = p
                elif f not in casillas_agua and f not in casillas_tocado and f[0] in x_range and f[1] in y_range:
                    ataque = f
                else:
                    c_solo_tocadas = [c_solo_tocadas[counter]]

            if len(c_solo_tocadas) == 1:  # si solo hay una casilla tocada o si hay varios barcos pegados
                try:
                    casillas_tocado.remove(c_solo_tocadas[0])  # si no, me daría error todas las veces

                    # uso esta función para que me encuentre las casillas no tocadas a distancia 1, si no hay devuelve None
                    casillas_posibles = casillas_y_barcos_correctos(
                        c_solo_tocadas[0], 2, (casillas_agua, casillas_tocado), square_size)

                    # si no hay casillas no tocadas a distancia 1, esto da TypeError, porque casillas posibles sería None
                    casillas_posibles = [elemento[0] for elemento in casillas_posibles]
                    ataque = choice(casillas_posibles)
                except TypeError:
                    casillas_tocado.append(c_solo_tocadas[0])  # deshago lo del try
                    counter += 1
                    c_solo_tocadas = []

        else:  # si no hay casillas solo tocadas, que elija aleatoriamente hasta que encuentre una no atacada previamente
            ataque = choice(squares_1)
            ataque = (ataque.left, ataque.top)

    return ataque


def flatten(t):
    # Devuelve una matriz unidimensional
    return [item for sublist in t for item in sublist]


def generar_barco(c, limite_x_l, limite_x_r, len_barco, casilla, square_size):
    # genera un barco sabiendo la posición inicial, la dirección y el tamaño del barco

    if square_size == 29:
        cuadricula = 16
    else:
        cuadricula = 10

    barcox = []
    if c[0] >= limite_x_l and c[0] <= limite_x_r and c[1] >= (14+cuadricula)/6 * \
            square_size and c[1] < (14+7*cuadricula)/6 * square_size:
        if casilla[1] == c[1]:
            for num in range(len_barco):
                barcox.append(
                    (min(casilla[0], c[0]) + num * square_size, casilla[1]))
        else:
            for num in range(len_barco):
                barcox.append(
                    (casilla[0], min(casilla[1], c[1]) + num * square_size))
        return barcox
    return None


def casillas_y_barcos_correctos(cuadrado_verde, len_barco, boats, square_size):
    # Función que determina todas las posiciones finales posibles una vez puesta 
    # la posición inicial del barco (durante la fase de colocación)
    if square_size == 29:
        cuadricula = 16
    else:
        cuadricula = 10

    if cuadrado_verde[0] < (cuadricula+3) * square_size:
        limite_x_l = 2 * square_size
        limite_x_r = (cuadricula+1) * square_size
    else:
        limite_x_l = (cuadricula+4) * square_size
        limite_x_r = (2*cuadricula+3) * square_size

    # vertical
    casilla_1 = (cuadrado_verde[0], (len_barco - 1)
                 * square_size + cuadrado_verde[1])
    casilla_2 = (cuadrado_verde[0],
                 cuadrado_verde[1] - (len_barco - 1) * square_size)

    # horizontal
    casilla_3 = ((len_barco - 1) * square_size +
                 cuadrado_verde[0], cuadrado_verde[1])
    casilla_4 = (cuadrado_verde[0] - (len_barco - 1)
                 * square_size, cuadrado_verde[1])

    casillas_posibles = [casilla_1, casilla_2, casilla_3, casilla_4]

    barco1 = generar_barco(casilla_1, limite_x_l,
                           limite_x_r, len_barco, cuadrado_verde, square_size)
    barco2 = generar_barco(casilla_2, limite_x_l,
                           limite_x_r, len_barco, cuadrado_verde, square_size)
    barco3 = generar_barco(casilla_3, limite_x_l,
                           limite_x_r, len_barco, cuadrado_verde, square_size)
    barco4 = generar_barco(casilla_4, limite_x_l,
                           limite_x_r, len_barco, cuadrado_verde, square_size)

    barcos_posibles = [barco1, barco2, barco3, barco4]
    casillas_incorrectas = set()

    for i, barco in enumerate(barcos_posibles):
        if barco:
            for boat in boats:
                for casilla in barco:
                    if casilla in boat:
                        casillas_incorrectas.add(i)
        else:
            casillas_incorrectas.add(i)

    counter = 0
    for num in casillas_incorrectas:
        casillas_posibles.pop(num - counter)
        barcos_posibles.pop(num - counter)
        counter += 1

    if casillas_posibles:
        return list(zip(casillas_posibles, barcos_posibles))
    return None


def turno_ataque(cuadrado_verde, barcos_hundidos_x,
                 restantes_x, casillas_agua, casillas_tocado):
    # Función que comprueba si es agua, tocado, hundido o victoria
    victoria = 0
    for i, boat in enumerate(restantes_x):
        if cuadrado_verde in boat:
            restantes_x[i].remove(cuadrado_verde)
            casillas_tocado.append(cuadrado_verde)
            if not restantes_x[i]:
                barcos_hundidos_x.append(i)
        if restantes_x[i]:
            victoria += 1

    if cuadrado_verde not in casillas_tocado:
        casillas_agua.append(cuadrado_verde)

    return barcos_hundidos_x, restantes_x, victoria, casillas_agua, casillas_tocado


def titulo():
    #Función del titulo: va cambiando de frame de la animación cada x frames de clock. Termina si se da a continuar.
    continuar = pg.Rect(CONTINUAR_COORDS, CONTINUAR_DIM)

    clock = pg.time.Clock()
    titulo = True
    pressed = False
    boton_continuar = False
    frames = 0

    while titulo:  # bucle principal titulo
        clock.tick(FPS)
        boton_continuar = False

        pos = pg.mouse.get_pos()  # da la posición del puntero
        if continuar.collidepoint(pos):
            boton_continuar = True
            if pressed == True:
                titulo = False
        pressed = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True


        if frames == 119: frames = 0
        else: frames += 1

        draw_titulo(boton_continuar, frames)


def menu(boats_player_1, boats_player_2, casillas_agua, casillas_tocado, barcos_hundidos_1, barcos_hundidos_2,
         restantes_1, restantes_2, turno_1, cantidad_barcos, cuadricula, jugadores, len_barco, victoria):
    # Consta de 4 botones: Nueva Partida, Guardar, Cargar y Salir
    iniciar = pg.Rect(INICIAR_COORDS, BOTON_MENU_DIM)
    cargar = pg.Rect(CARGAR_COORDS, BOTON_MENU_DIM)
    guardar = pg.Rect(GUARDAR_COORDS, BOTON_MENU_DIM)
    salir = pg.Rect(SALIR_COORDS, BOTON_MENU_DIM)

    clock = pg.time.Clock()
    menu = True
    frames = 0
    pressed = writing_g = writing_c = fin_escribir = False
    text = ""
    text_surface = None
    variables = (boats_player_1, boats_player_2, casillas_agua, casillas_tocado, barcos_hundidos_1,
                 barcos_hundidos_2, restantes_1, restantes_2, turno_1, cantidad_barcos, cuadricula, jugadores, len_barco)

    while menu:  # bucle principal menú
        clock.tick(FPS)
        boton_iniciar = boton_cargar = boton_guardar = boton_salir = boton_easter_egg = False
        writing = any((writing_g, writing_c))

        pos = pg.mouse.get_pos()  # da la posición del puntero

        if iniciar.collidepoint(pos) and not writing: # Nueva Partida
            boton_iniciar = True
            if pressed == True:
                return frames

        elif (cargar.collidepoint(pos) and not writing_g) or writing_c: # Cargar Partida
            boton_cargar = True
            if fin_escribir:
                writing_c = False

            if writing_c:
                width, height = font.size("Nombre del fichero:")
                text_surface = pg.transform.scale(font.render("Nombre del fichero:", True, (160,160,160)), (width,height))
                WIN.blit(text_surface, ((450, 412)))
                width, height = font.size(text)
                text_surface = pg.transform.scale(font.render(text, True, (0,0,0)), (2*width,2*height))
                WIN.blit(text_surface, ((WIDTH-5-2*width)/2, 430))

            if not writing_c and fin_escribir:
                if text == "Daniel Sánchez" or text == "Pepe Ridruejo":
                    return "Easter Egg"
                try:
                    with open(text, "r") as h:
                        lines = tuple(literal_eval(h.readline()) if num < 9 else int(h.readline()) for num in range(13))

                        boats_player_1, boats_player_2, casillas_agua, casillas_tocado, barcos_hundidos_1, barcos_hundidos_2 = lines[:6]
                        restantes_1, restantes_2, turno_1, cantidad_barcos, cuadricula, jugadores, len_barco = lines[6:]

                    return (boats_player_1, boats_player_2, casillas_agua, casillas_tocado, barcos_hundidos_1,
                            barcos_hundidos_2, restantes_1, restantes_2, turno_1, cantidad_barcos, cuadricula, jugadores, len_barco)
                except FileNotFoundError:
                    text, text_surface, fin_escribir = "", None, False

            if pressed == True:
                writing_c = True

        elif ((guardar.collidepoint(pos) and not writing_c) or writing_g) and not victoria and len_barco: # Guardar Partida
            boton_guardar = True
            if fin_escribir:
                writing_g = False

            if writing_g:
                width, height = font.size("Nombre del fichero:")
                text_surface = pg.transform.scale(font.render("Nombre del fichero:", True, (160,160,160)), (width,height))
                WIN.blit(text_surface, ((450, 530)))
                width, height = font.size(text)
                text_surface = pg.transform.scale(font.render(text, True, (0,0,0)), (2*width,2*height))
                WIN.blit(text_surface, ((WIDTH-5-2*width)/2, 545))

            if not writing_g and fin_escribir:
                with open(text, "w") as h:
                    for variable in variables:
                        h.write(f"{variable}\n")
                text, text_surface, fin_escribir = "", None, False

            if pressed == True:
                writing_g = True

        elif salir.collidepoint(pos): # Salir
            boton_salir = True
            if pressed == True:
                pg.quit()
                exit()

        pressed = False

        for event in pg.event.get(): # Boton "X"
            if event.type == pg.QUIT:
                pg.quit()
                exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

            if event.type == pg.KEYDOWN and (writing_g or writing_c):
                if event.key == pg.K_RETURN:
                    fin_escribir = True
                elif event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        pg.display.update()
        
        if frames == 119: frames = 0
        else: frames += 1

        draw_menu(boton_iniciar, boton_cargar, boton_guardar, boton_salir, boton_easter_egg, frames)


def easter_egg():

    salir = pg.Rect((WIDTH//2-64, 500), (767//6, 223//6))

    clock = pg.time.Clock()
    easter_egg = True
    frames = frames2 = 0

    while easter_egg:  # bucle principal menú
        clock.tick(FPS)

        pos = pg.mouse.get_pos()  # da la posición del puntero

        if frames2 == 250 and salir.collidepoint(pos) and pressed:
            easter_egg = False

        pressed = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        if frames < 300:
            frames += 1
        elif frames2 < 250:
            frames2 += 1

        draw_easter_egg(frames, frames2)


def options(frames):
    # Permite elegir entre cuadrícula 10x10 o 16x16, número de barcos (de 2 a 5) y número de jugadores (1 o 2)
    cuadricula_16 = pg.Rect(CUAD_16_COORDS, BOTON_CUAD_DIM)
    cuadricula_10 = pg.Rect(CUAD_10_COORDS, BOTON_CUAD_DIM)
    players_1 = pg.Rect(BOTON_PLAYERS_1_COORDS, BOTON_PLAYERS_1_DIM)
    players_2 = pg.Rect(BOTON_PLAYERS_2_COORDS, BOTON_BARCOS_DIM)
    barcos_2 = pg.Rect(BOTON_BARCOS_2_COORDS, BOTON_BARCOS_DIM)
    barcos_3 = pg.Rect(BOTON_BARCOS_3_COORDS, BOTON_BARCOS_DIM)
    barcos_4 = pg.Rect(BOTON_BARCOS_4_COORDS, BOTON_BARCOS_DIM)
    barcos_5 = pg.Rect(BOTON_BARCOS_5_COORDS, BOTON_BARCOS_DIM)
    jugar = pg.Rect(BOTON_JUGAR_COORDS, BOTON_JUGAR_DIM)

    clock = pg.time.Clock()
    options = True
    pressed = False

    cuadricula = cantidad_barcos = cuadricula_nueva = cantidad_barcos_nuevo = jugadores = 0
    cuadricula_pressed = cantidad_barcos_pressed = jugadores_pressed = jugar_on_top = False

    while options:
        clock.tick(FPS)

        cuadricula_nueva = 0
        cantidad_barcos_nuevo = 0
        jugadores_nuevo = 0
        jugar_on_top = False
        # Botones
        pos = pg.mouse.get_pos()
        if cuadricula_16.collidepoint(pos):
            cuadricula_nueva = 16
            if pressed:
                cuadricula_pressed = True
                cuadricula = 16

        elif cuadricula_10.collidepoint(pos):
            cuadricula_nueva = 10
            if pressed:
                cuadricula_pressed = True
                cuadricula = 10

        elif barcos_2.collidepoint(pos):
            cantidad_barcos_nuevo = 2
            if pressed:
                cantidad_barcos_pressed = True
                cantidad_barcos = 2

        elif barcos_3.collidepoint(pos):
            cantidad_barcos_nuevo = 3
            if pressed:
                cantidad_barcos_pressed = True
                cantidad_barcos = 3

        elif barcos_4.collidepoint(pos):
            cantidad_barcos_nuevo = 4
            if pressed:
                cantidad_barcos_pressed = True
                cantidad_barcos = 4

        elif barcos_5.collidepoint(pos):
            cantidad_barcos_nuevo = 5
            if pressed:
                cantidad_barcos_pressed = True
                cantidad_barcos = 5

        elif players_1.collidepoint(pos):
            jugadores_nuevo = 1
            if pressed:
                jugadores_pressed = True
                jugadores = 1
        elif players_2.collidepoint(pos):
            jugadores_nuevo = 2
            if pressed:
                jugadores_pressed = True
                jugadores = 2

        elif jugar.collidepoint(pos) and cantidad_barcos_pressed and cuadricula_pressed and jugadores_pressed:
            jugar_on_top = True
            if pressed:
                options = False

        pressed = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

        if frames == 119: frames = 0
        else: frames += 1

        draw_options(cuadricula, cantidad_barcos, jugadores, jugar_on_top,
                     cuadricula_nueva, cantidad_barcos_nuevo, jugadores_nuevo, frames)

    return cuadricula, cantidad_barcos, jugadores


def main(cuadricula, cantidad_barcos, jugadores, cargar):
    # Función principal del juego

    if cuadricula == 16:
        SQUARE_SIZE = SQUARE_SIZE_16
    else:
        SQUARE_SIZE = SQUARE_SIZE_10

    # creo en una lista rectángulos = a los cuadraditos del tablero 1
    squares_1 = [pg.Rect((SQUARE_SIZE * (2 + num_1), SQUARE_SIZE * (7/3+cuadricula/6 + num_2)),
                 (SQUARE_SIZE, SQUARE_SIZE)) for num_1 in range(cuadricula) for num_2 in range(cuadricula)]

    # creo en una lista rectángulos = a los cuadraditos del tablero 2
    squares_2 = [pg.Rect((SQUARE_SIZE * (cuadricula+4 + num_1), SQUARE_SIZE * (7/3+cuadricula/6 + num_2)),
                 (SQUARE_SIZE, SQUARE_SIZE)) for num_1 in range(cuadricula) for num_2 in range(cuadricula)]
    
    # Si es una partida cargada:
    if not isinstance(cargar, int):
        boats_player_1, boats_player_2, casillas_agua, casillas_tocado = cargar[:4]
        barcos_hundidos_1, barcos_hundidos_2, restantes_1, restantes_2, turno_1 = cargar[4:9]
        len_barco = cargar[12]
    else:
        boats_player_1, boats_player_2, casillas_agua, casillas_tocado, restantes_1, restantes_2 = [], [], [], [], [], []
        barcos_hundidos_1, barcos_hundidos_2, len_barco, turno_1 = [], [], 2, True

    clock = pg.time.Clock()

    game, colocacion_auto, pressed, change, cuadrado_verde, last_att_square,  = True, False, False, False, None, None
    boats, casillas_prov = [], []
    victoria = frames = 0

    if jugadores == 1: ataque_auto = True
    else: ataque_auto = False

    while game:  # bucle principal juego
        clock.tick(FPS)
        victoria = 0

        # pongo el cuadrado verde fuera de la pantalla
        pressed_square = (-100, -100)
        change = False
        pos = pg.mouse.get_pos()  # da la posición del puntero

        # Comprueba si ya se ha terminado la fase de colocación de barcos
        if len_barco == 10:
            pg.time.delay(1000)
            if turno_1:
                turno_1 = False
                boats_player_1 = boats
                restantes_1 = deepcopy(boats_player_1)
                boats, len_barco = [], 2
                if jugadores == 1:
                    colocacion_auto = True
                else: colocacion_auto = False
            else:
                if not colocacion_auto:
                    boats_player_2 = boats
                colocacion_auto = False
                restantes_2 = deepcopy(boats_player_2)
                boats, len_barco = [], 8
            cuadrado_verde = None

        if turno_1:  # seleccionar, iluminar cuadrados turno 1
            for square in squares_1:  # compruebo todos los cuadrados en el tablero 1
                if square.collidepoint(pos):
                    s = (square.left, square.top)
                    if not casillas_prov or s in flatten(casillas_prov) or s == cuadrado_verde:
                        pressed_square = s
                        if pressed == True:  # cuadrado_verde = a las coord del cuadrado en el que se hace click
                            if s != cuadrado_verde:
                                cuadrado_verde = s
                                change = True
                            elif casillas_prov:
                                cuadrado_verde = None
                                casillas_prov = None
        # turno 2
        else:  # seleccionar, iluminar cuadrados turno 2
            for square in squares_2:  # hago lo mismo con el tablero 2
                if square.collidepoint(pos):
                    s = (square.left, square.top)
                    if not casillas_prov or s in flatten(
                            casillas_prov) or s == cuadrado_verde:
                        pressed_square = s
                        if pressed == True:  # cuadrado_verde = a las coord del cuadrado en el que se hace click
                            if s != cuadrado_verde:
                                cuadrado_verde = s
                                change = True
                            elif casillas_prov:
                                cuadrado_verde = None
                                casillas_prov = None
        pressed = False

        for event in pg.event.get():
            if event.type == pg.QUIT:  # si le doy a la cruz, que se salga del programa
                pg.quit()
                exit()

            # si presiono un botón del ratón, y si es click izquierdo, pressed
            # = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    game = False
        
        if colocacion_auto: # si es colocación automática
            len_barco = 10
            boats_player_2 = colocacion_automatica(squares_2, cantidad_barcos, SQUARE_SIZE)

        if len_barco < cantidad_barcos + 2 and cuadrado_verde:  # colocar barco
            if not colocacion_auto:  # si es colocación normal
                if casillas_prov and change:  # si se ha seleccionado una casilla final de barco en la frame
                    # añado el barco seleccionado a boats
                    for i, option in enumerate(casillas_prov):
                        if cuadrado_verde in option:
                            boats.append(casillas_prov[i][1])
                    casillas_prov = None
                    len_barco += 1
                    if len_barco == cantidad_barcos + 2:  # si se han puesto todos los barcos, cambio len_barco a 10
                        len_barco = 10
                elif change:  # si se ha seleccionado una casilla inicial de barco en la frame
                    # genero las casillas de barco finales posibles
                    casillas_prov = casillas_y_barcos_correctos(cuadrado_verde, len_barco, boats, SQUARE_SIZE)
                    if not casillas_prov:
                        cuadrado_verde = None

        elif turno_1 and (cuadrado_verde or (ataque_auto and len_barco == 8)):  # ataque jugador 2
            
            if ataque_auto:
                barcos_restantes = [barco for i, barco in enumerate(boats_player_1) if i not in barcos_hundidos_1]
                cuadrado_verde = ataque_automatico(
                    squares_1, casillas_agua, casillas_tocado, barcos_restantes, SQUARE_SIZE)
                last_att_square = cuadrado_verde
            
            if (cuadrado_verde not in casillas_tocado and cuadrado_verde not in casillas_agua) or ataque_auto:
                prov = turno_ataque(
                    cuadrado_verde, barcos_hundidos_1, restantes_1, casillas_agua, casillas_tocado)
                barcos_hundidos_1, restantes_1, victoria, casillas_agua, casillas_tocado = prov
                if victoria == 0:
                    victoria = -2
                    game = False
                turno_1 = not turno_1
            cuadrado_verde = None

        elif cuadrado_verde:  # ataque jugador 1
            if cuadrado_verde not in casillas_tocado and cuadrado_verde not in casillas_agua:
                prov = turno_ataque(
                    cuadrado_verde, barcos_hundidos_2, restantes_2, casillas_agua, casillas_tocado)
                barcos_hundidos_2, restantes_2, victoria, casillas_agua, casillas_tocado = prov
                if victoria == 0:
                    victoria = -1
                    game = False
                turno_1 = not turno_1
            cuadrado_verde = None

        if frames == 39: frames = 0
        else: frames += 1

        draw_gameboard(pressed_square, cuadrado_verde, boats, len_barco, casillas_agua,
                       casillas_tocado, barcos_hundidos_1, barcos_hundidos_2, boats_player_1,
                       boats_player_2, victoria, casillas_prov, frames, SQUARE_SIZE, cuadricula, last_att_square)

    return (boats_player_1, boats_player_2, casillas_agua, casillas_tocado, barcos_hundidos_1, barcos_hundidos_2,
            restantes_1, restantes_2, turno_1, cantidad_barcos, cuadricula, jugadores, len_barco, victoria)


if __name__ == "__main__":
    titulo()
    game = True
    t = None, None, None, None, None, None, None, None, None, None, None, None, None, None
    while game: # bucle principal
        cargar = menu(t[0], t[1], t[2], t[3], t[4], t[5], t[6],
                      t[7], t[8], t[9], t[10], t[11], t[12], t[13])
        if isinstance(cargar, int):
            option = options(cargar)
        elif cargar == "Easter Egg":
            easter_egg()
        else:
            option = (cargar[10], cargar[9], cargar[11])
        if cargar != "Easter Egg":
            t = main(option[0], option[1], option[2], cargar)
