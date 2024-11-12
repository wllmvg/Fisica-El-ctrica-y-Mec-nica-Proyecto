import math

# Constante de Coulomb en unidades SI
k = 9e9


# Pedir al usuario que ingrese el radio de la esfera en metros
r = float(input("Ingrese el radio de la esfera en metros: "))

# Pedir al usuario que ingrese la carga de la fuente que cargó la esfera en culombios
q = float(input("Ingrese la carga en culombios: "))

# Constante dieléctrica del medio que rodea la esfera
epsilon = 8.85e-12

# Cálculo de la carga eléctrica de la esfera
area_esfera=((4)*(math.pi)*(r)**2)
xd = ((4)*(math.pi)*(r)**2)

c=q/xd

# Imprimir el resultado
print("La densidad de carga superficial en la esfera es: {:.2e}C/m^2".format(c))