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