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