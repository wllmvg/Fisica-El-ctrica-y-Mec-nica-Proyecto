import math

# Constante de Coulomb en unidades SI
k = 9e9

# Carga puntual en Coulombs, proporcionada por el usuario
print("Ingrese los datos en notación cientifica.")
print("Ejemplo: 10X10^-9")
print("Se escribiria: 10e-9")
print(" ")
q = float(input("Ingrese la carga puntual en Coulombs : ")) 

# Distancia desde la carga puntual en metros, proporcionada por el usuario
r = float(input("Ingrese la distancia desde la carga puntual en metros: "))

# Cálculo de la magnitud del campo eléctrico
E = (k * q) / r**2

# Cálculo del ángulo de la dirección del campo eléctrico
theta = math.degrees(math.atan2(0, 2))

# Impresión de resultados
print("El campo eléctrico es de {:.3e} N/C".format(E))