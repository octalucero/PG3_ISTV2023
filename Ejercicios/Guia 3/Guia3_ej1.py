def suma():
        while True:   
            try:
                op1 = (int(input("Ingrese un numero: ")))
                op2 = (int(input("Ingrese otro numero: ")))
                print(f"El resultado es: {op1 + op2}")
            except ValueError:
                print("El valor es incorrecto.Ingrese un numero ")
            finally:
                print("------------------")
                print("Ingrese otra suma ")
                

continuar = True

while continuar:
    option = input("Quiere seguir sumando? (s/n): ")
    if option == "s":
        num = suma()
    elif option == "n":
        print("Adios!")
        continuar = False
    else:
        print("Error, ingrese una opcion valida")