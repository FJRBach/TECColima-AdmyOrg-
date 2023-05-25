def main():
    print("Ejercicio 4")
    xh = input("Ingresa las horas totales")
    xr = input("Ingresa las horas trabajadas:")
    flh = float(xh)
    fr = float(xr)
    if fr >40:
        
        print("Fuera del tiempo a lograr")
    else: 
        print("Regular")
    z = float(xh) * float(xr)
    print("Pago: ", z)
if __name__ == "__main__":
    main()