class Base:
    def __init__(self):
        self.a = "a"
        self.b = "b"
        self.c = "c"
 
    def A(self):
        print(self.a)
 
    def B(self):
        print(self.b)
 
    def C(self):
        print(self.c)
 
# Clase derivada que hereda de Base.
class Derivada(Base):
 
    def __init__(self):
        # Modifica el valor del atributo 'a' antes de llamar al inicializador de la clase base.
        self.a = "aa"
        super().__init__() 
        self.c = "cc" 
 
    def A(self):
        # Sobreescritura del método A() para imprimir el valor de 'a' en la clase derivada.
        print(self.a)
 
    def B(self):
        # Sobreescritura del método B() para modificar 'b' antes de llamar al método B() de la clase base.
        self.b = "bb"
        super().B()
        print(self.b)


def main():
    base = Base() 
    derivada = Derivada() 
    
    base.A()  
    derivada.A() 
    print() 
    base.B()  
    derivada.B() 
    base.C()
    derivada.C() 
    
    derivada = base
    derivada.C() 

if __name__ == "__main__":
    main()
