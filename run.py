cadena = " "
while cadena != "fin":
    cadena = str(input("ingresar palabra: "))
    if cadena[0] == cadena[len(cadena) - 1] :
        print(cadena)
