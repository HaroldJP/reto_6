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