meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre","Diciembre")

def mes():
    try:
        numero = int(input("Ingrese un numero de mes (1-12): "))
        nombre_mes = meses[numero-1]
        print("El mes ingresado:", nombre_mes)
    except ValueError:
        print("Debe ingresar un numero de un mes")
    except IndexError:
        print("El numero ingresado no es parte de ningun mes")

if __name__ == "__main__":
    mes()