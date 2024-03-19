# Manipulación de Puntos en 2D y 3D

Este script de Python define dos clases, `Punto2D` y `Punto3D`, para representar y manipular puntos en espacios bidimensionales y tridimensionales, respectivamente. `Punto3D` es una subclase de `Punto2D`, ampliando su funcionalidad al espacio 3D.

## Características

- **Punto2D**: Representa un punto en el espacio 2D con coordenadas x e y. Soporta la operación de traslación a lo largo de los ejes x e y.
- **Punto3D**: Hereda de `Punto2D` y añade una coordenada z para representar un punto en el espacio 3D. Soporta la operación de traslación a lo largo de los ejes x, y y z.


# Ejemplo de Herencia Múltiple en Python

Este script de Python demuestra el uso de la herencia múltiple a través de la definición de varias clases. La clase `D` hereda de las clases `B` y `C`, las cuales a su vez heredan de la clase base `A`.

## Descripción de las Clases

- **Clase A**: Clase base que inicializa tres atributos `a`, `b`, y `c` con los valores proporcionados al instanciar un objeto.
- **Clase B**: Subclase de la clase `A`. No introduce modificaciones o atributos adicionales.
- **Clase C**: Otra subclase de la clase `A`, similar a la clase `B` en que no añade funcionalidades o atributos propios.
- **Clase D**: Esta clase ilustra la herencia múltiple al heredar de ambas, `B` y `C`. Inicializa los mismos atributos que `A` mediante el uso de `super()`. Adicionalmente, introduce un nuevo atributo opcional `d`, que tiene un valor predeterminado de `None`.

## Funcionamiento

El script define un método `main` que demuestra la creación de una instancia de la clase `D` y verifica su relación de herencia con las clases `A`, `B`, y `C`. También muestra el acceso a los atributos heredados y al nuevo atributo `d`.

### Creación y Verificación de Instancias

Para crear una instancia de la clase `D` y verificar su herencia:

```python
d = D(1, 2, 3)
print(isinstance(d, A), isinstance(d, B), isinstance(d, C))
```

# Herencia y Sobreescritura de Métodos en Python

Este script de Python demuestra cómo se utiliza la herencia para extender y modificar el comportamiento de una clase base en una clase derivada. Se ilustra la sobreescritura de métodos y el cambio de atributos en la clase derivada.

## Descripción de las Clases

- **Clase Base**: Define tres atributos (`a`, `b`, `c`) y tres métodos (`A()`, `B()`, `C()`) que imprimen los valores de los atributos respectivos.
- **Clase Derivada**: Hereda de la clase `Base`, modifica los valores de los atributos heredados e introduce cambios en el comportamiento de los métodos heredados.

## Funcionamiento

La clase derivada modifica los valores de algunos atributos definidos en la clase base durante su inicialización. Además, sobreescritura algunos métodos de la clase base para alterar su comportamiento estándar.

### Cambios en Atributos

- Al instanciar la clase `Derivada`, el atributo `a` se establece en `"aa"` antes de llamar al inicializador de la clase base, mientras que el atributo `c` se cambia a `"cc"` después de la llamada a `super().__init__()`.

### Sobreescritura de Métodos

- El método `A()` de la clase `Derivada` simplemente imprime el valor de `a`, mostrando el efecto de su cambio en el inicializador.
- El método `B()` modifica el valor de `b` a `"bb"`, llama al método `B()` de la clase base y luego imprime el nuevo valor de `b`.

## Ejemplo de Uso

El método `main` demuestra la creación e interacción con instancias de las clases `Base` y `Derivada`, evidenciando las diferencias en el comportamiento debido a la sobreescritura de métodos y la modificación de atributos.

```python
base = Base() 
derivada = Derivada() 

base.A()  # Imprime el valor original de 'a'
derivada.A()  # Imprime el valor modificado de 'a'
print() 
base.B()  # Imprime el valor original de 'b'
derivada.B()  # Imprime el valor modificado de 'b', luego el valor original, y nuevamente el modificado
base.C()
derivada.C()  # Ambos imprimen 'c', pero con diferente valor debido a la modificación en la clase Derivada
```

# Gestión de Superficies Acristaladas en Construcciones

Este script de Python demuestra el manejo de elementos constructivos en una edificación, específicamente paredes y ventanas, para calcular la superficie acristalada total. Utiliza conceptos de orientación a objetos como la herencia y la composición para modelar las relaciones entre las diferentes entidades.

## Descripción de las Clases

- **Clase Pared**: Representa una pared de la edificación. Cada pared tiene una orientación y puede contener múltiples ventanas. Provee métodos para agregar ventanas y calcular la superficie acristalada total.

- **Clase ParedCortina**: Especialización de `Pared` que representa una pared completamente acristalada. Su superficie acristalada total se define explícitamente en lugar de calcularse a partir de las ventanas.

- **Clase Ventana**: Representa una ventana con una superficie específica y una protección obligatoria (como persianas o estores). Cada ventana está asociada a una pared.

- **Clase Casa**: Agrupa varias paredes (incluyendo paredes cortina) y calcula la superficie acristalada total de la edificación.

## Funcionamiento

El script define un método `main` que demuestra la creación de una casa con varias paredes y ventanas. Muestra cómo calcular la superficie acristalada total antes y después de reemplazar una pared común por una pared cortina.

### Instanciación y Cálculo de Superficies

- Se crean instancias de `Pared` y `Ventana`, asignando a cada ventana una superficie y protección, y agregándolas a su pared correspondiente.

- Se instancia una `Casa` con las paredes creadas y se calcula la superficie acristalada inicial.

- Una de las paredes es reemplazada por una `ParedCortina` con una superficie acristalada definida, y se recalcula la superficie acristalada total de la casa.

## Ejemplo de Uso

```python
pared_norte = Pared("NORTE")
ventana_norte = Ventana(pared_norte, 0.5, "Persiana")
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
print("Superficie acristalada inicial:", casa.superficie_acristalada())
casa.paredes[2] = ParedCortina("SUR", 10)
print("Superficie acristalada final:", casa.superficie_acristalada())


