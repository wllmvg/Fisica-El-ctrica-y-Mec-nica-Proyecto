import os
import sys
import math
import msvcrt  # Importar la biblioteca msvcrt para detectar una tecla presionada

def menu_fisica_mecanica():
       
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

def menu_fisica_electrica():

        def esperar_tecla():
            print("Presiona cualquier tecla para continuar...")
        msvcrt.getch()  # Esperar a que el usuario presione una tecla

        def opcion1():
            opcion = 0
            while opcion != 4:
                os.system('cls')

                print("Selecciona una opción: ")
                print(" ")
                print("1. 1 Carga")
                print("2. 2 Cargas")
                print("3. 3 Cargas")
                print("4. Volver al menú principal")
                print(" ")
                opcion = int(input("Introduce el número de la opción deseada: "))
                
                
                if opcion == 1:
                    os.system('cls')
                    # Constante de Coulomb en unidades SI
                    k = 9e9

                    # Carga puntual en Coulombs, proporcionada por el usuario
                    print("--------------------------------------------------------------------------")
                    print(" ")
                    print("Ingrese los datos en notación cientifica si es necesario")
                    print("Ejemplo: 10X10^-9")
                    print("Se escribiria: 10e-9")
                    print(" ")
                    print("--------------------------------------------------------------------------")
                    print(" ")
                    # Carga puntual
                    
                    q = float(input("Ingrese la carga puntual en Coulombs : ")) 
                    print(" ")

                    # Distancia desde la carga puntual en metros, proporcionada por el usuario
                    
                    r = float(input("Ingrese la distancia desde la carga puntual en metros: "))
                    print(" ")
                    print("--------------------------------------------------------------------------")
                    

                    # Cálculo de la magnitud del campo eléctrico
                    E = (k * q) / r**2

                    # Cálculo del ángulo de la dirección del campo eléctrico
                    theta = math.degrees(math.atan2(0, 2))

                    # Impresión de resultados
                    print(" ")
                    print(" ")
                    print(" ")
                    print("El campo eléctrico es de {:.3e} N/C".format(E))
                    print(" ")
                    print(" ")
                    print(" ")
                    esperar_tecla()
                elif opcion == 2:
                    os.system('cls')

                    print("--------------------------------------------------------------------------")
                    print(" ")
                    print("Ingrese los datos en notación cientifica si es necesario")
                    print("Ejemplo: 10X10^-9")
                    print("Se escribiria: 10e-9")
                    print(" ")
                    print("--------------------------------------------------------------------------")
                    print(" ")

                    # Constante de Coulomb en unidades SI
                    k = 9e9

                    # Carga puntual en Coulombs
                    
                    q1 = float(input("Introduce el valor de la carga 1 en Coulombs: "))
                    print(" ")
                    q2 = float(input("Introduce el valor de la carga 2 en Coulombs: "))
                    print(" ")
                    print("--------------------------------------------------------------------------")

                    # Distancia desde la carga puntual en metros
                    print(" ")
                    r1 = float(input("Introduce la distancia desde la carga 1 en metros: "))
                    print(" ")
                    r2 = float(input("Introduce la distancia desde la carga 2 en metros: "))
                    print(" ")
                    print("--------------------------------------------------------------------------")

                    # Cálculo del campo eléctrico generado por cada carga
                    E1 = (k * q1) / r1 ** 2
                    E2 = (k * q2) / r2 ** 2
                    # Cálculo de la magnitud y dirección del campo eléctrico resultante
                    E = E1-E2

                    # Impresión de resultados
                    print(" ")
                    print(" ")
                    print(" ")
                    print("El campo eléctrico es de {:.3e} N/C".format(E))
                    print(" ")
                    print(" ")
                    print(" ")
                    esperar_tecla()
                elif opcion == 3:
                    os.system('cls')
                    print(" ")
                    print("CORREGIR")
                    print(" ")
                    esperar_tecla()
                elif opcion == 4:
                    os.system('cls')
                    print(" ")
                    print("Volviendo al menú principal...")
                    print(" ")
                else:
                    os.system('cls')
                    print(" ")
                    print("Opción inválida. Por favor, seleccione una opción del menú.")
                    print(" ")
                    esperar_tecla()
            
        def opcion2():
            opcion = 0
            while opcion != 4:
                os.system('cls')
                
                print("Selecciona la forma de la carga superficial a calcular: ")
                print(" ")
                print("1. Cilindro")
                print("2. Esfera")
                print("3. Rectangulo")
                print("4. Volver al menú principal")
                print(" ")
                opcion = int(input("Introduce el número de la opción deseada: "))
                
                if opcion == 1:
                    os.system('cls')

                    print("--------------------------------------------------------------------------")
                    print(" ")
                    print("Ingrese los datos en notación cientifica si es necesario")
                    print("Ejemplo: 10X10^-9")
                    print("Se escribiria: 10e-9")
                    print(" ")
                    print("--------------------------------------------------------------------------")
                    print(" ")

                    # Constante de Coulomb en unidades SI
                    k = 9e9


                    # Pedir al usuario que ingrese el radio del cilindro en metros
                    r = float(input("Ingrese el radio del cilindro en metros: "))
                    print(" ")
                    

                    # Pedir al usuario que ingrese la altura del cilindro en metros
                    h = float(input("Ingrese la altura del cilindro en metros: "))
                    print(" ")
                    # Pedir al usuario que ingrese la carga de la fuente que cargó la esfera en culombios
                    q = float(input("Ingrese la carga en culombios: "))
                    print(" ")
                    print("--------------------------------------------------------------------------")

                    # Constante dieléctrica del medio que rodea la esfera
                    epsilon = 8.85e-12

                    # Cálculo de la carga eléctrica de la esfera
                    area_cilindro=(2*(math.pi)*(r)*(h))


                    c=q/area_cilindro

                    # Imprimir el resultado
                    print(" ")
                    print(" ")
                    print(" ")
                    print("La densidad de carga superficial en el cilindro es: {:.2e}C/m^2".format(c))
                    print(" ")
                    print(" ")
                    print(" ")
                    esperar_tecla()

                elif opcion == 2:
                    os.system('cls')

                    print("--------------------------------------------------------------------------")
                    print(" ")
                    print("Ingrese los datos en notación cientifica si es necesario")
                    print("Ejemplo: 10X10^-9")
                    print("Se escribiria: 10e-9")
                    print(" ")
                    print("--------------------------------------------------------------------------")
                    print(" ")

                    # Constante de Coulomb en unidades SI
                    k = 9e9


                    # Pedir al usuario que ingrese el radio de la esfera en metros
                    r = float(input("Ingrese el radio de la esfera en metros: "))
                    print(" ")
                    # Pedir al usuario que ingrese la carga de la fuente que cargó la esfera en culombios
                    q = float(input("Ingrese la carga en culombios: "))
                    print(" ")
                    print("--------------------------------------------------------------------------")

                    # Constante dieléctrica del medio que rodea la esfera
                    epsilon = 8.85e-12

                    # Cálculo de la carga eléctrica de la esfera
                    area_esfera=((4)*(math.pi)*(r)**2)
                    xd = ((4)*(math.pi)*(r)**2)

                    c=q/xd

                    # Imprimir el resultado
                    print(" ")
                    print(" ")
                    print(" ")
                    print("La densidad de carga superficial en la esfera es: {:.2e}C/m^2".format(c))
                    print(" ")
                    print(" ")
                    print(" ")
                    esperar_tecla()
                elif opcion == 3:
                    os.system('cls')

                    print("--------------------------------------------------------------------------")
                    print(" ")
                    print("Ingrese los datos en notación cientifica si es necesario")
                    print("Ejemplo: 10X10^-9")
                    print("Se escribiria: 10e-9")
                    print(" ")
                    print("--------------------------------------------------------------------------")
                    print(" ")
                    # Constante de Coulomb en unidades SI
                    k = 9e9


                    # Pedir al usuario que ingrese las dimensiones del rectángulo en metros
                    l = float(input("Ingrese la longitud del rectángulo en metros: "))
                    print(" ")
                    w = float(input("Ingrese el ancho del rectángulo en metros: "))
                    print(" ")
                    # Pedir al usuario que ingrese la carga de la fuente que cargó la esfera en culombios
                    q = float(input("Ingrese la carga en culombios: "))
                    print(" ")
                    print("--------------------------------------------------------------------------")

                    # Constante dieléctrica del medio que rodea la esfera
                    epsilon = 8.85e-12

                    # Cálculo de la carga eléctrica de la esfera
                    area_cilindro=(l*w)


                    c=q/area_cilindro

                    # Imprimir el resultado
                    print(" ")
                    print(" ")
                    print(" ")
                    print("La densidad de carga superficial en el rectangulo es: {:.2e}C/m^2".format(c))
                    print(" ")
                    print(" ")
                    print(" ")
                    esperar_tecla()
                elif opcion == 4:
                    os.system('cls')
                    print(" ")
                    print("Volviendo al menú principal...")
                    print(" ")

                else:
                    os.system('cls')
                    print(" ")
                    print("Opción inválida. Por favor, seleccione una opción del menú.")
                    print(" ")
                    esperar_tecla()
            
        def opcion3():
            opcion = 0
            while opcion != 4:
                os.system('cls')
                
                print("Selecciona que valores tiene para calcular la fuerza de atracción: ")
                print(" ")
                print("1. Carga Desconocida")
                print("2. Fuerza De Atracción Entre Dos Cargas")
                print("3. Distancia Entre Cargas")
                print("4. Volver al menú principal")
                print(" ")
                opcion = int(input("Introduce el número de la opción deseada: "))
                
                if opcion == 1:
                    os.system('cls')
                    print("--------------------------------------------------------------------------")
                    print(" ")
                    print("Ingrese los datos en notación cientifica si es necesario")
                    print("Ejemplo: 10X10^-9")
                    print("Se escribiria: 10e-9")
                    print(" ")
                    print("--------------------------------------------------------------------------")
                    print(" ")
                    # Definición de constantes
                    k = 9e9

                    # Lectura de datos
                    q1 = float(input("Ingrese el valor de la carga conocida en microcoulombs: "))
                    print(" ")
                    f = float(input("Ingrese el valor de la fuerza de atracción en Newtons: "))
                    print(" ")
                    r = float(input("Ingrese la distancia entre las cargas en metros: "))
                    print(" ")
                    print("--------------------------------------------------------------------------")

                    # Cálculo de la carga desconocida
                    q2 = (f*(r**2))/(k*q1)


                    # Impresión de resultados
                    print(" ")
                    print(" ")
                    print(" ")
                    print("La carga desconocida es de {:.2e} N".format(q2))
                    print(" ")
                    print(" ")
                    print(" ")
                    esperar_tecla()

                elif opcion == 2:
                    os.system('cls')
                    print("--------------------------------------------------------------------------")
                    print(" ")
                    print("Ingrese los datos en notación cientifica si es necesario")
                    print("Ejemplo: 10X10^-9")
                    print("Se escribiria: 10e-9")
                    print(" ")
                    print("--------------------------------------------------------------------------")
                    print(" ")
                    k = 9e9
                    q1   = float(input("Ingrese el valor de la primera carga: "))
                    print(" ")
                    q2   = float(input("Ingrese el valor de la segunda carga: "))
                    print(" ")
                    r   = float(input("Ingrese el valor de la distancia entre ambas cargas: "))
                    print(" ")
                    print("--------------------------------------------------------------------------")

                    fuerza=(k*q1*q2)/(r**2)
                    print(" ")
                    print(" ")
                    print(" ")
                    print("El valor de la fuerza de atracción entre las dos cargas es: {:.2e} N".format(fuerza))
                    print(" ")
                    print(" ")
                    print(" ")
                    esperar_tecla()
                elif opcion == 3:
                    os.system('cls')
                    print("--------------------------------------------------------------------------")
                    print(" ")
                    print("Ingrese los datos en notación cientifica si es necesario")
                    print("Ejemplo: 10X10^-9")
                    print("Se escribiria: 10e-9")
                    print(" ")
                    print("--------------------------------------------------------------------------")
                    print(" ")
                    def sqrt(x) -> float:
                        return x**(1/2)
                    def distancia(q1:float,q2:float,f:float) -> float:
                        k = 9e9 # Constante de Coulomb
                        return sqrt((k*q1*q2)/f) # Aplicación de la formula de Coulomb con su despeje
                    q1 = float(input("Ingrese el valor de la primera carga: "))
                    print(" ")
                    q2 = float(input("Ingrese el valor de la segunda carga: "))
                    print(" ")
                    f = float(input("Ingrese el valor de la fuerza: "))
                    print(" ")
                    print("--------------------------------------------------------------------------")
                    print(" ")
                    print(" ")
                    print(" ")
                    print("La distancia entre ambas cargas es: {:.2e}m".format(distancia(q1,q2,f)))
                    print(" ")
                    print(" ")
                    print(" ")
                    esperar_tecla()
                elif opcion == 4:
                    os.system('cls')
                    print(" ")
                    print("Volviendo al menú principal...")
                    print(" ")
                else:
                    os.system('cls')
                    print(" ")
                    print("Opción inválida. Por favor, seleccione una opción del menú.")
                    print(" ")
                    esperar_tecla()

        # Creamos el menú principal utilizando la estructura while y la función input()
        opcion = 0
        while opcion != 4:
            os.system('cls')
            print("Selecciona una opción del menú principal:")
            print(" ")
            print("1. Campo Eléctrico")
            print("2. Densidad De Carga Superficial")
            print("3. Fuerza De Atracción")
            print("4. Salir")
            print(" ")
            opcion = int(input("Introduce el número de la opción deseada: "))
            
            if opcion == 1:
                opcion1()
            elif opcion == 2:
                opcion2()
            elif opcion == 3:
                opcion3()
            elif opcion == 4:
                os.system('cls')
                print(" ")
                print("¡Hasta luego!") 
                print(" ")
            else:
                os.system('cls')
                print(" ")
                print("Opción inválida. Por favor, seleccione una opción del menú.")
                print(" ")
                esperar_tecla()


def main():
    while True:
        print("¿Sobre qué materia desarrollarás ejercicios?")
        print("1. Física mecánica")
        print("2. Física eléctrica")
        print("0. Salir")
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            menu_fisica_mecanica()
            
        elif opcion == "2":
            menu_fisica_electrica()
            
        elif opcion == "0":
            print("Hasta luego!")
            break
            
        else:
            print("Opción inválida. Intente de nuevo.")
            
if __name__ == "__main__":
    main()


