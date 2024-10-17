"""
Proyecto POO: Gestion de Bar
"""

# Creamos la clase principal de donde se derivaran las demas
class Bebida:
    def __init__(self, nombre, marca, grado_alcohol):
        self._nombre = nombre
        self._marca = marca
        self._grado_alcohol = grado_alcohol

    # getter y setter de nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # getter y setter de marca
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    # getter y setter de grado de alcohol
    @property
    def grado_alcohol(self):
        return self._grado_alcohol

    @grado_alcohol.setter
    def grado_alcohol(self, grado_alcohol):
        self._grado_alcohol = grado_alcohol

    # definimos un metodo mostrar para mostrar la informacion de nuestras bebidas
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Marca: {self.marca}, Grado de Alcohol: {self.grado_alcohol}%"

# Creamos una clase Cerveza que heredara de la clase bebida
class Cerveza(Bebida):
    def __init__(self, nombre, marca, grado_alcohol, tipo):
        super().__init__(nombre, marca, grado_alcohol)
        self._tipo = tipo

    # Getter y setter de tipo
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    # Usamos mostrar informacion de nuestra clase Bebida pero agregamos el atributo extra de nuestra clase
    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Tipo: {self.tipo}"

# Creamos una clase Vino que heredara de la clase bebida
class Vino(Cerveza):
    def __init__(self, nombre, marca, grado_alcohol, tipo, anio):
        super().__init__(nombre, marca, grado_alcohol, tipo)
        self._anio = anio

    # Getter y setter de anio
    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, anio):
        self._anio = anio

    # Usamos mostrar informacion de nuestra clase Bebida pero agregamos el atributo extra de nuestra clase
    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Año: {self._anio}"

# Creamos una clase Vino que heredara de la clase bebida directamente
class Licor(Bebida):
    def __init__(self, nombre, marca, grado_alcohol, sabor):
        super().__init__(nombre, marca, grado_alcohol)
        self._sabor = sabor

    # Getter y setter de sabor
    @property
    def sabor(self):
        return self._sabor

    @sabor.setter
    def sabor(self, sabor):
        self._sabor = sabor

    # Usamos mostrar informacion de nuestra clase Bebida pero agregamos el atributo extra de nuestra clase
    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Sabor: {self._sabor}"

# Creamos una clase Cliente para administrar los clientes de nuestro Bar
class Cliente:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Getter y setter para edad y nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    # metodo mostrar informacion
    def mostrar_informacion(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}"

# Creamos una sub clase de cliente para clasificar nuestros clientes del bar
class Regular(Cliente):
    def __init__(self, nombre, edad, frecuencia_visitas):
        super().__init__(nombre, edad)
        self._frecuencia_visitas = frecuencia_visitas

    # getter y setter de frecuencia visitas
    @property
    def frecuencia_visitas(self):
        return self._frecuencia_visitas

    @frecuencia_visitas.setter
    def frecuencia_visitas(self, frecuencia_visitas):
        self._frecuencia_visitas = frecuencia_visitas

    # metodo mostrar informacion agregando las nuevas propiedades de esta nueva clase
    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Frecuencia de Visitas: {self._frecuencia_visitas} veces por mes"

# Subclase de cliente VIP
class VIP(Cliente):
    def __init__(self, nombre, edad, descuento):
        super().__init__(nombre, edad)
        self._descuento = descuento

    # getter y setter cliente VIP
    @property
    def descuento(self):
        return self._descuento

    @descuento.setter
    def descuento(self, descuento):
        self._descuento = descuento

    # metodo mostrar informacion agregando las nuevas propiedades de esta nueva clase
    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Descuento: {self._descuento}%"

# Hacemos una funcion para un "interfaz" en el que podamos hacer uso de nuestras clases y subclases
def gestion():
    bar = [] # guardar bebidas
    clientes = [] # guardar clientes

    while True:
        print("\n*** Gestion de Bar 'Popeye' ***")
        print("1. Agregar Bebida")
        print("2. Agregar Cliente")
        print("3. Mostrar Bebidas")
        print("4. Mostrar Clientes")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_bebida(bar)
        elif opcion == "2":
            agregar_cliente(clientes)
        elif opcion == "3":
            mostrar_bebidas(bar)
        elif opcion == "4":
            mostrar_clientes(clientes)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# funcion para agregar bebidas
def agregar_bebida(bar):
    print("\n*** Agregar Bebida ***")
    tipo = input("Tipo (cerveza, vino, licor): ").lower()
    nombre = input("Nombre: ")
    marca = input("Marca: ")

    # hacemos uso de try - except para el manejo de errores cuando se introduce algo diferente a un numero en el grado de alcohol
    try:
        grado_alcohol = float(input("Grado de Alcohol (%): "))
    except ValueError:
        print("Error: El grado de alcohol debe ser un número.")
        return

    # agregar el tipo de cerveza y manejo de errores para cuando el año no es un entero
    if tipo == "cerveza":
        tipo_cerveza = input("Tipo de Cerveza: ")
        bebida = Cerveza(nombre, marca, grado_alcohol, tipo_cerveza)
    elif tipo == "vino":
        tipo = input("Tipo: ")
        try:
            anio = int(input("Año: "))
        except ValueError:
            print("Error: El año debe ser un número entero.")
            return
        bebida = Vino(nombre, marca, grado_alcohol, tipo, anio)
    elif tipo == "licor":
        sabor = input("Sabor: ")
        bebida = Licor(nombre, marca, grado_alcohol, sabor)
    else:
        print("Tipo de bebida no válido.")
        return

    # si no tiene errores cachados por el try - excpet nuestra bebida se aggrega a nuestra lista
    bar.append(bebida)
    print("Bebida agregada exitosamente.")

# funcion para agregar clientes
def agregar_cliente(clientes):
    print("\n*** Agregar Cliente ***")
    tipo = input("Tipo (regular, vip): ").lower()
    nombre = input("Nombre: ")

    # Uso de excepciones para manejo de errores en los parametros edad, frecuencia de visitas y descuento
    try:
        edad = int(input("Edad: "))
        if edad < 18:
            print("Error: La edad debe ser mayor o igual a 18.")
            return
    except ValueError:
        print("Error: La edad debe ser un número entero.")
        return

    if tipo == "regular":
        try:
            frecuencia_visitas = int(input("Frecuencia de Visitas (veces por mes): "))
        except ValueError:
            print("Error: La frecuencia de visitas debe ser un número entero.")
            return
        cliente = Regular(nombre, edad, frecuencia_visitas)
    elif tipo == "vip":
        try:
            descuento = float(input("Descuento (%): "))
        except ValueError:
            print("Error: El descuento debe ser un número.")
            return
        cliente = VIP(nombre, edad, descuento)
    else:
        print("Tipo de cliente no válido.")
        return

    # si no se cacha ingun error, agregamos al cliente a nuestra lista
    clientes.append(cliente)
    print("Cliente agregado exitosamente.")

# funcion para mostrar las bebidas del bar
def mostrar_bebidas(bar):
    print("\n--- Bebidas en el Bar ---")
    for bebida in bar:
        print(bebida.mostrar_informacion())

# funcion para mostrar clientes del bar
def mostrar_clientes(clientes):
    print("\n--- Clientes del Bar ---")
    for cliente in clientes:
        print(cliente.mostrar_informacion())


if __name__ == "__main__":
    gestion()

