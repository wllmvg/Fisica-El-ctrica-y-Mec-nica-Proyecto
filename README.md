# Física Eléctrica y Mecánica

## Descripción

Proyecto académico desarrollado en Python para resolver diferentes ejercicios y problemas de Física Mecánica y Física Eléctrica mediante una interfaz de consola. El sistema permite realizar cálculos relacionados con caída libre, campo eléctrico, fuerza de atracción entre cargas y densidad de carga superficial en diferentes geometrías.

El proyecto está organizado en dos módulos principales:

- **Física Mecánica:** herramientas para resolver problemas de movimiento vertical y caída libre.
- **Física Eléctrica:** herramientas para calcular magnitudes eléctricas utilizando la Ley de Coulomb y conceptos de electrostática.

---

## Características

### Física Mecánica
Permite resolver problemas de:

- Determinar el tiempo de caída de un objeto.
- Hallar la posición de un objeto a partir de datos conocidos.
- Calcular la altura máxima de un objeto lanzado verticalmente.
- Determinar la altura inicial de lanzamiento.
- Menú interactivo basado en consola.

### Física Eléctrica
Permite realizar cálculos de:

#### Campo Eléctrico
- Campo eléctrico generado por una carga puntual.
- Campo eléctrico generado por dos cargas.
- Campo eléctrico generado por tres cargas.

#### Fuerza entre Cargas
- Calcular fuerza eléctrica conociendo ambas cargas y la distancia.
- Calcular distancia entre cargas conociendo la fuerza.
- Calcular una carga desconocida usando la Ley de Coulomb.

#### Densidad de Carga Superficial
- Esfera.
- Cilindro.
- Rectángulo.

---

## Estructura del Proyecto

```text
Fisica-El-ctrica-y-Mec-nica-Proyecto-master/
│
├── PRUEBA2.py
│
├── Fisica Mecánica/
│   └── prueba.py
│
└── Fisica Électrica/
    ├── Programa.py
    │
    └── Codigos/
        ├── Campo Electrico (1 carga).py
        ├── Campo Electrico (2 cargas).py
        ├── Campo Electrico (3 cargas).py
        ├── Densidad de Carga Superficial cilindro (radio,altura y carga).py
        ├── Densidad de Carga Superficial esfera (radio y carga).py
        ├── Densidad de Carga Superficial rectangulo (radio y carga).py
        ├── Fuerza de atraccion entre cargas (se tiene valor de 1 carga y fuerza atraccion).py
        ├── Fuerza de atraccion entre cargas (se tiene valor de las 2 cargas y distancia).py
        └── Fuerza de atraccion entre cargas (se tiene valor de las 2 cargas y fuerza de atraccion).py
```

---

## Requisitos

### Software
- Python 3.8 o superior

### Librerías utilizadas

El proyecto utiliza únicamente librerías estándar de Python:

```python
math
os
sys
msvcrt
```

**Nota:** `msvcrt` solo está disponible en Windows.

---

## Instalación

1. Clonar el repositorio:

```bash
git clone <url-del-repositorio>
```

2. Ingresar al directorio:

```bash
cd Fisica-El-ctrica-y-Mec-nica-Proyecto-master
```

3. Ejecutar el programa deseado:

```bash
python PRUEBA2.py
```

o

```bash
python "Fisica Électrica/Programa.py"
```

---

## Funcionalidades Analizadas

### 1. Módulo de Física Mecánica

Implementa cálculos relacionados con movimiento vertical uniformemente acelerado y caída libre.

Incluye fórmulas derivadas de:

- Ecuaciones de movimiento rectilíneo uniformemente acelerado.
- Gravedad terrestre.
- Movimiento vertical.
- Lanzamiento hacia arriba.

### Operaciones disponibles

| Opción | Descripción |
|----------|------------|
| 1 | Determinar tiempo de caída |
| 2 | Hallar posición |
| 3 | Calcular altura máxima |
| 4 | Calcular altura inicial |
| 5 | Salir |

---

### 2. Campo Eléctrico

#### Una carga

Calcula:

```text
E = kq/r²
```

Donde:

- E = Campo eléctrico
- k = Constante de Coulomb
- q = Carga eléctrica
- r = Distancia

#### Dos cargas

Calcula el campo resultante mediante la diferencia de los campos generados por ambas cargas.

#### Tres cargas

Solicita coordenadas cartesianas para las tres cargas y para el punto de evaluación.

Intenta calcular el vector de campo eléctrico resultante.

---

### 3. Fuerza de Atracción entre Cargas

Basado en la Ley de Coulomb:

```text
F = k(q₁q₂)/r²
```

Permite:

- Hallar fuerza.
- Hallar distancia.
- Hallar una carga desconocida.

---

### 4. Densidad de Carga Superficial

Calcula:

```text
σ = Q / A
```

Para:

- Esfera.
- Cilindro.
- Rectángulo.

---

## Observaciones Técnicas

Durante el análisis del código se identificaron algunos puntos de mejora:

### Compatibilidad

- El proyecto está orientado a Windows

## Posibles Mejoras

- Interfaz gráfica con Tkinter o PyQt.
- Soporte para Linux y macOS.
- Validación robusta de entradas.
- Modularización del código.
- Pruebas automatizadas.
- Documentación técnica de fórmulas.
- Exportación de resultados a PDF o Excel.
- Uso de programación orientada a objetos.

---

## Tecnologías Utilizadas

- Python
- Matemática computacional básica
- Consola de comandos
- Librería estándar de Python

---

## Autor

Proyecto académico orientado al aprendizaje de conceptos de:

- Física Mecánica
- Física Eléctrica
- Programación en Python
- Aplicación de fórmulas científicas mediante software
