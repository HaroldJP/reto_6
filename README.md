# reto_6
En este repo voy a mostarr cómo hice cada uno de los programas del reto 6.
### Punto 1
Dado la figura de la imagen, desarrolle:

Una función matemática para calcular el volumen y el área superficial.
Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
Revise como utilizar el valor de pi usando import math y math.pi

El programa para este punto se hizo así:

```python
def area_superficial_cono(r2 : float, h : float) -> float:
    import math
    area_cono = (math.pi*r2*h)+(math.pi*r2**2)
    return area_cono

def area_superficial_esfera(r1) -> float:
    import math
    area_esfera = 4*math.pi*r1**2
    return area_esfera

def volumen_total_esfera(r1) -> float:
    import math
    volumen_esfera = (4/3)*math.pi*(r1**3)
    return volumen_esfera

def volumen_total_cono(r2, h) -> float:
    import math
    volumen_cono = (1/3)*math.pi*(r2**2)*h
    return volumen_cono

if __name__ == "__main__":
    r1 = float(input("Ingrese el radio de la esfera: "))
    r2 = float(input("Ingrese el radio del cono: "))
    h = float(input("Ingrese la altura del cono: "))
    area1 = area_superficial_cono(r2, h)
    area2 = area_superficial_esfera(r1)
    volumen1 = volumen_total_esfera(r1)
    volumen2 = volumen_total_cono(r2, h)
    print("El área del cono es " +str(area1))
    print("El área de la esfera es " +str(area2))
    print("El volumen de la esfera es " +str(volumen1))
    print("El volumen del cono es " +str(volumen2))
```
### Punto 2
Dado la figura de la imagen, desarrolle:

Una función matemática para calcular el área y el perimetro.
Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
Revise como utilizar el valor de pi usando import math y math.pi

El programa para este punto se hizo así:

```python
def area_rectangulo(a : float, b : float) -> float:
    area_r = a*b
    return area_r

def area_circulos(r : float) -> float:
    import math
    area_c = math.pi*(r**2)*2 ##son dos círculos y por eso el 2 del final
    return area_c

def perimetro_rectangulo(a, b) -> float:
    perimetro_r = (a*2)+(b*2)
    return perimetro_r

def perimetro_circulos(r) -> float:
    import math
    perimetro_c = 2*math.pi*r*2 ##son dos círculos y por eso el 2 del final
    return perimetro_c

if __name__ == "__main__":
    a = float(input("Ingrese la altura del rectángulo:"))
    b = float(input("Ingrese el largo del rectángulo: "))
    r = float(input("Ingrese el radio que será igual para los dos círculos: "))
    area1 = area_rectangulo(a, b)
    area2 = area_circulos(r)
    perimetro1 = perimetro_rectangulo(a, b)
    perimetro2 = perimetro_circulos(r)
    print("El área del rectángulo es " +str(area1))
    print("El perímetro del rectángulo es " +str(perimetro1))
    print("El área de los dos círculos es " +str(area2))
    print("El perímetro de los dos círculos es " +str(perimetro2))
```

* Explicación de cómo utilizar el valor de pi:
Para utilizar el número pi en python es necesario importar la función math con el comando "import math", y seguido a esto, el número pi se puede traer a través del comando "math.pi". A continuación el ejemplo:

```python
import math
math.pi
```

### Punto 3

Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

El respectivo programa para este punto lo hice así:

```python
gallina : int = 6
gallo : int = 7
pollito : int = 1
def cantidad_carne(n : int, m : int, k : int) -> int:
    carne_gallina = n*gallina
    carne_gallo = m*gallo
    carne_pollito = k*pollito
    carne_total = carne_gallina+carne_gallo+carne_pollito
    return carne_total

if __name__ == "__main__":
    n = int(input("Ingrese una cantidad de gallinas: "))
    m = int(input("Ingrese una cantidad de gallos: "))
    k = int(input("Ingrese una cantidad de pollitos: "))
    carne = cantidad_carne(n, m, k)
    print("La cantidad de carne que se tiene entre gallinas, gallos y pollitos es " +str(carne)+ " Kg")
```

### Punto 4

Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

El programa de este punto se hizo así:

```pyhton
pan : int = 300
leche : int = 3300
huevo : int = 350
def vueltas(p : int, m : int, h : int, b : int) -> int:
    precio_panes = p*pan
    precio_leche = m*leche
    precio_huevo = h*huevo
    precio_total = precio_panes+precio_leche+precio_huevo
    vuelta = b - precio_total
    if vuelta >= 0:
        vuelta == vuelta
        print("Le quedan " +str(vuelta)+ " pesos de vueltas")
    else:
        vuelta == vuelta*(-1)
        print("Usted quedó debiendo " +str(vuelta*(-1))+ " pesos")    
    return vuelta

if __name__ == "__main__":
    p = int(input("Ingrese cuántos panes le mandó a comprar su mamá: "))
    m = int(input("Ingrese cuántas bolsas de leche le mandío a comprar su mamá: "))
    h = int(input("Ingrese cuántos huevos le mandó a comprar su mamá: "))
    b = int(input("Ingrese el valor del billete que le dió su mamá: "))
    vuelta1 = vueltas(p, m, h, b)
```

### Punto 5

Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

Este programa fue hecho así:

```pyhton
def valor_prestamo(c:float, i:float, n:float) -> float:
    interes = i/12
    prestamo = c*((1+interes)**n)
    return prestamo

if __name__ == "__main__":
    c = float(input("Ingrese el valor del préstamo: "))
    i = float(input("Ingrese el interés por año: "))
    n = float(input("Ingrese el número total de meses:"))
    prestamo1 = valor_prestamo(c, i, n)
    print("El interés compuesto del préstamo es " + str(prestamo1))
```

### Punto 6

El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

Este punto se desarrolló de la siguiente forma:

```python
c : int
c = int(input("Ingrese el número actual de contagiados en NuncaLandia: "))
n : int
n = int(input("Escriba el número de días que han pasado en NuncaLandia desde el primer registro: "))
def contagios(c, n) -> int:
    contagiados = c*(2**n)
    return contagiados
if __name__ == "__main__":
    contagios1 = contagios(c, n)
    print("El número de contagiados en NuncaLandia después de " +str(n)+ " días será de " +str(contagios1))
```

### Punto 7

Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

El promedio
La mediana
El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
Ordenar los números de forma ascendente
Ordenar los números de forma descendente
La potencia del mayor número elevado al menor número
La raíz cúbica del menor número

Este punto se hizo así:

```pyhton
a : float
b : float
c : float
d : float
e : float
a = float(input("Ingrese el primer número real: "))
b = float(input("Ingrese e segundo número real: "))
c = float(input("Ingrese el tercer número real: "))
d = float(input("Ingrese el cuarto número real: "))
e = float(input("Ingrese el quinto número real: "))
def promedio(a, b, c, d, e) -> float:
    prom = (a+b+c+d+e)/5
    return prom
def promedio_multiplicativo(a, b, c, d, e) -> float:
    promm = (a*b*c*d*e)**(1/5)
    return promm
def orden_ascendente(a, b, c, d, e) -> float:
    lista1 = [a, b, c, d, e]
    ascendencia = sorted(lista1)
    return ascendencia
def orden_descendente(a, b, c, d, e) -> float:
    lista2 = [a, b, c, d, e]
    descendencia = sorted(lista2, reverse = True)
    return descendencia
def mediana(a, b, c, d, e) -> float:
    lista3 = [a, b, c, d, e]
    lista3ord = sorted(lista3)
    lista3long = len(lista3)
    mediana3 = lista3ord[lista3long // 2]
    return mediana3
def potencia(a, b, c, d, e) -> float:
    lista4 = [a, b, c, d, e]
    mayor = max(lista4)
    menor = min(lista4)
    potenciaa = mayor**menor
    return potenciaa
def cubica(a, b, c, d, e) -> float:
    lista5 = [a, b, c, d, e]
    menor1 = min(lista5)
    raiz = menor1**(1/3)
    return raiz
if __name__ == "__main__":
    promedio1 = promedio(a, b, c, d, e)
    print("El promedio es " +str(promedio1))
    promediom1 = promedio_multiplicativo(a, b, c, d, e)
    print("El promedio multiplicatvo es " +str(promediom1))
    ordena1 = orden_ascendente(a, b, c, d, e)
    print("Números ordenados en forma ascendente: " +str(ordena1))
    ordena2 = orden_descendente(a, b, c, d, e)
    print("Números ordenados en forma descendente: " +str(ordena2))
    mediana1 = mediana(a, b, c, d, e)
    print("La mediana es el número " +str(mediana1))
    potencia1 = potencia(a, b, c, d, e)
    print("La potencia del mayor número elevado al menor número es: " +str(potencia1))
    cubica1 = cubica(a, b, c, d, e)
    print("La raís cúbica del menor número es: " +str(cubica1))
```

### Punto 8

Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

Es importante mencionar que el archivo independiente con las funciones se encuentra adjunto en este repo con el nombre funciones.py
Ahora el programa como tal que utiliza las funciones de este archivo se hizo así:

```python
a : float
b : float
c : float
d : float
e : float
a = float(input("Ingrese el primer número real: "))
b = float(input("Ingrese e segundo número real: "))
c = float(input("Ingrese el tercer número real: "))
d = float(input("Ingrese el cuarto número real: "))
e = float(input("Ingrese el quinto número real: "))
from funciones import promedio
from funciones import promedio_multiplicativo
from funciones import orden_ascendente
from funciones import orden_descendente
from funciones import mediana
from funciones import potencia
from funciones import cubica
if __name__ == "__main__":
    promedio1 = promedio(a, b, c, d, e)
    print("El promedio es " +str(promedio1))
    promediom1 = promedio_multiplicativo(a, b, c, d, e)
    print("El promedio multiplicatvo es " +str(promediom1))
    ordena1 = orden_ascendente(a, b, c, d, e)
    print("Números ordenados en forma ascendente: " +str(ordena1))
    ordena2 = orden_descendente(a, b, c, d, e)
    print("Números ordenados en forma descendente: " +str(ordena2))
    mediana1 = mediana(a, b, c, d, e)
    print("La mediana es el número " +str(mediana1))
    potencia1 = potencia(a, b, c, d, e)
    print("La potencia del mayor número elevado al menor número es: " +str(potencia1))
    cubica1 = cubica(a, b, c, d, e)
    print("La raís cúbica del menor número es: " +str(cubica1))
```

### Punto 9

Consultar qué es y cómo funciona pip en python.

PIP is a package management system for Python that is used to install and manage software packages and their dependencies during deployment. It connects to an online repository of public packages called the Python Package Index (PyPI). PIP can be used to install packages from PyPI and other indexes, and it can be configured to connect to other package repositories, provided that they comply with Python Enhancement Proposal 503. Most distributions of Python come with PIP preinstalled, and Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include PIP by default. PIP is a command-line interface that allows the installation of Python software packages by issuing a command. PIP's command-line interface can be used to install, upgrade, and remove packages, as well as to list installed packages and their dependencies. PIP is also used to create and manage virtual environments, which are isolated Python environments that can be used to install packages without affecting the system Python installation. To install PIP, you can download and install it from the PyPI website or use the system package manager. To check if PIP is installed, you can navigate to the location of Python's script directory and type "pip --version" in the command line. If you do not have PIP installed, you can install it using the command "python3 -m pip install --user --upgrade pip".

### Punto 10

Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.

Here's a list of popular Python modules that can be installed using pip, along with instructions on how to install them:
* NumPy - used for numerical computing and data analysis
To install: pip install numpy
* pandas - used for data manipulation and analysis
To install: pip install pandas
* Matplotlib - used for data visualization
To install: pip install matplotlib
* Seaborn - used for statistical data visualization
To install: pip install seaborn
* scikit-learn - used for machine learning and data mining
To install: pip install scikit-learn
* Requests - used for making HTTP requests
To install: pip install requests
* TensorFlow - used for machine learning and deep learning
To install: pip install tensorflow
* PyTorch - used for machine learning and deep learning
To install: pip install torch
* Flask - used for web development
To install: pip install flask
* Django - used for web development
To install: pip install django

To install any of these modules, you can use the pip install command followed by the name of the module. For example, to install NumPy, you would run pip install numpy in the command line. If you need to install a specific version of a module, you can specify the version number using the == operator. For example, to install version 1.0.0 of NumPy, you would run pip install numpy==1.0.0.
Related
Python libraries list
What are built-in modules in Python
Python packages list
