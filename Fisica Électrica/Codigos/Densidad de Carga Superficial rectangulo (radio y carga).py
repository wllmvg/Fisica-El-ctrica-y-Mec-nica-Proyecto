import math

# Constante de Coulomb en unidades SI
k = 9e9


# Pedir al usuario que ingrese las dimensiones del rectángulo en metros
l = float(input("Ingrese la longitud del rectángulo en metros: "))
w = float(input("Ingrese el ancho del rectángulo en metros: "))

# Pedir al usuario que ingrese la carga de la fuente que cargó la esfera en culombios
q = float(input("Ingrese la carga en culombios: "))

# Constante dieléctrica del medio que rodea la esfera
epsilon = 8.85e-12

# Cálculo de la carga eléctrica de la esfera
area_cilindro=(l*w)


c=q/area_cilindro

# Imprimir el resultado
print("La densidad de carga superficial en el rectangulo es: {:.2e}C/m^2".format(c))