k = 9e9
q1   = float(input("Ingrese el valor de la primera carga:"))
q2   = float(input("Ingrese el valor de la segunda carga: "))
r   = float(input("Ingrese el valor de la distancia entre ambas cargas: "))

fuerza=(k*q1*q2)/(r**2)

print("El valor de la fuerza de atracción entre las dos cargas es: {:.2e} N".format(fuerza))