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