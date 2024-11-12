import math

# Definir la constante de Coulomb en unidades SI
k = 8.9875e9

# Pedir al usuario que ingrese las coordenadas y las magnitudes de las cargas
x1, y1 = map(float, input("Ingrese las coordenadas de la primera carga (x,y) separadas por una coma: ").split(","))
q1 = float(input("Ingrese la magnitud de la primera carga en culombios: "))
x2, y2 = map(float, input("Ingrese las coordenadas de la segunda carga (x,y) separadas por una coma: ").split(","))
q2 = float(input("Ingrese la magnitud de la segunda carga en culombios: "))
x3, y3 = map(float, input("Ingrese las coordenadas de la tercera carga (x,y) separadas por una coma: ").split(","))
q3 = float(input("Ingrese la magnitud de la tercera carga en culombios: "))

# Pedir al usuario que ingrese las coordenadas del punto donde se desea calcular el campo eléctrico
xp, yp = map(float, input("Ingrese las coordenadas del punto donde se desea calcular el campo eléctrico (x,y) separadas por una coma: ").split(","))

# Calcular la distancia y el vector de distancia desde las cargas hasta el punto dado
r1 = math.sqrt((xp-x1)**2 + (yp-y1)**2)
r2 = math.sqrt((xp-x2)**2 + (yp-y2)**2)
r3 = math.sqrt((xp-x3)**2 + (yp-y3)**2)
r1_unit = ((xp-x1)/r1, (yp-y1)/r1)
r2_unit = ((xp-x2)/r2, (yp-y2)/r2)
r3_unit = ((xp-x3)/r3, (yp-y3)/r3)

# Calcular el campo eléctrico generado por cada carga y sumarlos
E1 = k * q1 / r1**2 * r1_unit
E2 = k * q2 / r2**2 * r2_unit
E3 = k * q3 / r3**2 * r3_unit
E_total = E1 + E2 + E3

# Imprimir el resultado
print("El campo eléctrico en el punto ({}, {}) es: ({}, {}) N/C".format(xp, yp, E_total[0], E_total[1]))