class A:
    def __init__(self, a, b, c):
        # El inicializador de la clase A asigna los valores pasados como parámetros a los atributos de instancia 'a', 'b' y 'c'.
        self.a = a
        self.b = b
        self.c = c

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    # La clase D hereda tanto de B como de C, ilustrando la herencia múltiple. 
    def __init__(self, a, b, c, d=None):
        # El inicializador de D llama al inicializador de la clase base usando super(), 
        super().__init__(a, b, c)
        # Además, el inicializador de D introduce un nuevo atributo de instancia 'd', que tiene un valor predeterminado de None si no se proporciona.
        self.d = d

def main():
    d = D(1, 2, 3)
    print(isinstance(d, A), isinstance(d, B), isinstance(d, C))  
    print(d.a, d.b, d.c)

if __name__ == "__main__":
    main()

