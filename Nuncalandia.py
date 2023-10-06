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