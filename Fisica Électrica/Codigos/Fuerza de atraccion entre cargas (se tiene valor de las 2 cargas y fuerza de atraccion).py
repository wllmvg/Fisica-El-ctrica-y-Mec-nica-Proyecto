def sqrt(x) -> float:
  return x**(1/2)
def distancia(q1:float,q2:float,f:float) -> float:
  k = 9e9 # Constante de Coulomb
  return sqrt((k*q1*q2)/f) # Aplicación de la formula de Coulomb con su despeje
q1 = float(input("Ingrese el valor de la primera carga: "))
q2 = float(input("Ingrese el valor de la segunda carga: "))
f = float(input("Ingrese el valor de la fuerza: "))
print("La distancia entre ambas cargas es: {:.2e}m".format(distancia(q1,q2,f)))