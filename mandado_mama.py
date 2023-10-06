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