# Definición de constantes
k = 9e9

# Lectura de datos
q1 = float(input("Ingrese el valor de la carga conocida en microcoulombs: "))
f = float(input("Ingrese el valor de la fuerza de atracción en Newtons: "))
r = float(input("Ingrese la distancia entre las cargas en metros: "))

# Cálculo de la carga desconocida
q2 = (f*(r**2))/(k*q1)


# Impresión de resultados

print("La carga desconocida es de {:.2e} N".format(q2))
