import math
import os
import msvcrt  # Importar la biblioteca msvcrt para detectar una tecla presionada

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