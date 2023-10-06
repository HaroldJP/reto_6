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