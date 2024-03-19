class Punto2D:
    def __init__(self, x, y):
        # Inicializa un punto en 2D con coordenadas x e y.
        self.x = x  
        self.y = y  
    
    def traslacion(self, dx, dy):
        # Traslada el punto en 2D por un desplazamiento dx en el eje X y dy en el eje Y.
        self.x += dx 
        self.y += dy 
    
    def __str__(self):
        # Devuelve una representación en cadena del punto en 2D.
        return f"X: {self.x}  Y: {self.y}" 

class Punto3D(Punto2D):
    # Hereda de Punto2D para representar un punto en 3D.
    def __init__(self, x, y, z):
        # Inicializa un punto en 3D usando super() para establecer x e y, y agrega la coordenada z.
        super().__init__(x, y) 
        self.z = z 

    def traslacion(self, dx, dy, dz):
        # Traslada el punto en 3D. Usa super() para trasladar en x e y, y añade traslación en z.
        super().traslacion(dx, dy) 
        self.z += dz  
    
    def __str__(self):
        # Devuelve una representación en cadena del punto en 3D.
        return f"X: {self.x}  Y: {self.y}  Z: {self.z}"  
    

def main():
    a = Punto2D(1, 2)  
    print("A = {}".format(a))  

    a.traslacion(-1, -2)  
    print("A = {}".format(a))  

    b = Punto2D(-3, 0)  
    print("B = {}".format(b))

    b.traslacion(5, -1)  
    print("B = {}".format(b)) 

    c = Punto3D(1, 2, 3)  
    print("C = {}".format(c))  

    c.traslacion(-1, -2, -3)  
    print("C = {}".format(c)) 

    d = Punto3D(-3, 0, 2)  
    print("D = {}".format(d))  

    d.traslacion(5, -1, 3)  
    print("D = {}".format(d)) 

if __name__ == "__main__":
    main()
