import math

# Constante de Coulomb en unidades SI
k = 9e9

# Carga puntual en Coulombs
q1 = float(input("Introduce el valor de la carga 1 en Coulombs: "))
q2 = float(input("Introduce el valor de la carga 2 en Coulombs: "))

# Distancia desde la carga puntual en metros
r1 = float(input("Introduce la distancia desde la carga 1 en metros: "))
r2 = float(input("Introduce la distancia desde la carga 2 en metros: "))

# Cálculo del campo eléctrico generado por cada carga
E1 = (k * q1) / r1 ** 2
E2 = (k * q2) / r2 ** 2
# Cálculo de la magnitud y dirección del campo eléctrico resultante
E = E1-E2

# Impresión de resultados
print("El campo eléctrico es de {:.3e} N/C".format(E))
