class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def ladomayor(self):
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado {mayor} es el lado mas grande ")

    def equilatero(self):
        