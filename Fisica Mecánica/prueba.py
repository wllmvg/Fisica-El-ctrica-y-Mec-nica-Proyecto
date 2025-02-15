import os
import sys
import math




def generar_menu(lista):
    num = 1
    for elem in lista:
        print("     " + str(num) + ". " + elem)
        num += 1
    print()


def print_menu():
    print_mensaje_entre_espacios("Programa para Desarrollar de Caida Libre")
    lista = ["Determinar el tiempo de caída.", "Hallar la posición de un objeto a partir de otros datos.",
             "Conocer la altura máxima de un objeto lanzado hacia arriba.", "¿Desde qué altura se lanza?",
             "Salir"]
    generar_menu(lista)


def print_numero_invalido():
    print("Oops!  Ese no es un número valido. Intenta de nuevo...")


def select_menu_option():
    return solicitar_numero_int("Ingrese la opción que desea: ")


def run():
    while True:
        try:
            os.system("cls")
            print_menu()
            opcion = select_menu_option()
            action_menu(opcion)
        except KeyboardInterrupt:
            salir()



def action_menu(opcion):
    if opcion == 1:
        caso1()
    elif opcion == 2:
        caso2()
    elif opcion == 3:
        caso3()
    elif opcion == 4:
        caso4()
    elif opcion == 5:
        salir()


def caso1():
    print_mensaje_entre_espacios('Determinaremos el tiempo de caída libre a partir  de algunos datos.')
    h_0 = solicitar_numero_float(
        'Ingrese la altura inicial del cuerpo (en metros): h_0 = ')  # creamos la variable h_0 (es un número real por
    # eso usamos float)
    v_0 = solicitar_numero_float('Ingrese la velocidad inicial del cuerpo (en m/s) recuerde que será negativa cuando'
                                 ' se lance hacia abajo y positiva si se lanza hacia arriba: v_0 = ')
    # creamos la variable v_0

    # usamos la funcion tiempo_caida_libre que se encuentra en funciones.py
    print('El tiempo de caída es: ', tiempo_caida_libre(v_0, h_0), ' segundos.')
    confirmar_volver_menu()


def caso2():
    print_mensaje_entre_espacios('Podemos conocer la altura de un objeto en determinado tiempo o bien saber en qué'
                                 ' momento se encuentra para cierta altura.')
    h_0 = solicitar_numero_float('Ingrese la altura inicial del cuerpo (en metros): h_0 = ')  # creamos la variable h_0
    v_0 = solicitar_numero_float('Ingrese la velocidad inicial del cuerpo (en m/s) recuerde que será negativa cuando'
                                 ' se lance hacia abajo y positiva si se lanza hacia arriba: v_0 = ')
    # creamos la variable v_0
    opcion_2 = str(input('¿Qué desea saber? (altura, tiempo): '))
    if opcion_2 == 'altura':
        t = solicitar_numero_float('Ingrese el tiempo en el que desea conocer la altura del objeto (en segundos): ')
        y = pos_vertical(h_0, v_0, t)
        print('La altura del objeto es de ', round(y, 2), ' metros')
    else:
        y = solicitar_numero_float('Ingrese la altura del cuerpo (en metros), hallaremos el tiempo que demora en '
                                   'llegar hasta allí. y= ')
        if v_0 ** 2 - 4 * (-4.9) * (h_0 - y) >= 0:  # Es el discriminante de la función
            t1 = round(tiempo_1(v_0, h_0 - y), 2)
            t2 = round(tiempo_2(v_0, h_0 - y), 2)
            if t1 == 0:
                print('El cuerpo pasa por la altura y = ', y, ' metros en t = ', t2, ' segundos.')
            elif t1 >= 0 and t2 == 0 and t2 >= 0:
                print('El cuerpo pasa por la altura y = ', y, ' metros en los momentos t1 = ', t1, ' segundos y t2 = ',
                      t2, ' segundos.')
            else:
                print(
                    'Parece que el cuerpo no pasará por allí en ningún momento. Es posible que esa altura supere la '
                    'altura máxima.')
    confirmar_volver_menu()


def caso3():
    print_mensaje_entre_espacios('Calcularemos la altura máxima que alcanza un objeto lanzado hacia arriba.')
    h_0 = solicitar_numero_float('Ingrese la altura inicial del cuerpo (en metros): h_0 = ')
    v_0 = solicitar_numero_float('Ingrese la velocidad inicial del cuerpo (en m/s) recuerde que será negativa cuando '
                                 'se lance hacia abajo y positiva si se lanza hacia arriba: v_0 = ')
    if v_0 <= 0:
        print('Si el objeto parte del reposo o es lanzado hacia abajo, la altura máxima será la altura inicial,'
              ' es decir ', h_0, ' metros.')
    else:
        # A partir de la ecuación de la velocidad en función del
        # tiempo ( v = v_0 -g.t) despejamos el tiempo, imponiendo la condición
        # de que la velocidad en la altura máxima es cero. Llamaremos a esta
        # variable t_hmax

        t_hmax = round(v_0 / 9.8, 2)
        # Ahora calculamos la altura máxima(h_max) sustituyendo el tiempo
        # por t_hmax en la función pos_vertical()

        h_max = round(pos_vertical(h_0, v_0, t_hmax), 2)
        print('El cuerpo alcanza su máxima altura en un tiempo de ', t_hmax, ' segundos, y tiene un valor de ', h_max,
              ' metros.')
    confirmar_volver_menu()


def caso4():
    print_mensaje_entre_espacios(
        'Suponga que se suelta un objeto desde cierta altura, que llamaremos h_0. Vamos a calcularla suponiendo que '
        'conocemos el tiempo de caída (t_caída).')
    t_caida = solicitar_numero_float(
        'Ingrese el tiempo de caída (en segundos), t_caída= ')  # ingresamos la variable t_caida
    # A partir de la ecuación de posición y = h_0 + v_0.t - 1/2.g.t²
    # despejamos h_0 imponiendo la condición y=0.
    if t_caida < 0:
        print('Un valor negativo para el tiempo no tiene mucho sentido en este contexto. Revise sus datos.')
    else:
        h_0 = round(4.9 * t_caida ** 2, 2)
        # Como el objeto se suelta (asumimos velocidad inicial 0)
        print('El objeto se suelta desde una altura de ', h_0, ' metros.')
    confirmar_volver_menu()


def salir():
    sys.exit(0)


def confirmar_volver_menu():
    input('Presione enter para volver al menú. ')


def print_mensaje_entre_espacios(mensaje):
    print("")
    print(mensaje)
    print()


def solicitar_numero(mensaje, funcion):
    valido = False
    numero = None
    while not valido:
        try:
            numero = funcion(input(mensaje))
            valido = True
        except ValueError:
            print_numero_invalido()
    return numero


def solicitar_numero_int(mensaje):
    return solicitar_numero(mensaje, int)


def solicitar_numero_float(mensaje):
    return solicitar_numero(mensaje, float)


def pos_vertical(h_0, v_0, t):
    return h_0 + v_0 * t - 4.9 * (t ** 2)


def tiempo_1(v, y):
    return (-v + math.sqrt(v ** 2 - 4 * (-4.9) * y)) / (-9.8)


def tiempo_2(v, y):
    return (-v - math.sqrt(v ** 2 - 4 * (-4.9) * y)) / (-9.8)


def tiempo_caida_libre(v_0, h_0):
    # a partir de la ecuación de posición: y = h_0 +v_0t -gt²/2
    # despejamos t igualando y = 0 (pues está en el suelo!)
    # como es una ecuación de segundo grado nos arrojará dos resultados
    # que llamaremos t1 y t2. Descartamos la solución negativa.
    t1 = tiempo_1(v_0, h_0)
    t2 = tiempo_2(v_0, h_0)
    return round(max(t1, t2), 2)

# -*- coding: utf-8 -*-
# Correr en python3 para evitar problemas de codificación (tildes)
# o usar la codificación anterior.

run()

