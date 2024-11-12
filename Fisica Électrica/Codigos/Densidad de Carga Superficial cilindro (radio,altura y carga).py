import math

# Constante de Coulomb en unidades SI
k = 9e9


# Pedir al usuario que ingrese el radio del cilindro en metros
r = float(input("Ingrese el radio del cilindro en metros: "))

# Pedir al usuario que ingrese la altura del cilindro en metros
h = float(input("Ingrese la altura del cilindro en metros: "))

# Pedir al usuario que ingrese la carga de la fuente que cargó la esfera en culombios
q = float(input("Ingrese la carga en culombios: "))

# Constante dieléctrica del medio que rodea la esfera
epsilon = 8.85e-12

# Cálculo de la carga eléctrica de la esfera
area_cilindro=(2*(math.pi)*(r)*(h))


c=q/area_cilindro

# Imprimir el resultado
print("La densidad de carga superficial en el cilindro es: {:.2e}C/m^2".format(c))