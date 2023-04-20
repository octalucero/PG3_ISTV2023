def numero():
    try:
        num = int(input("Ingrese un numero: "))
        return num
    except ValueError:
        print("Ingreso de numero erroneo, pruebe otra vez")
        return numero()
    
    
def division(dividendo, divisor):
    try:
        divid = dividendo / divisor
        return divid
    except ZeroDivisionError:
        print("No es posible didivir por 0 ")

num1 = numero()
num2 = numero()
print(division(num1, num2))