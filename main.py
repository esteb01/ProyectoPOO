import pandas as pd

"""
Proyecto POO: Gestion de Bar
"""

# Clase padre bebida
class Bebida:
    def __init__(self, nombre, marca, grado_alcohol, precio):
        self._nombre = nombre
        self._marca = marca
        self._grado_alcohol = grado_alcohol
        self._precio = precio
        self.validar_grado_alcohol(grado_alcohol)

    # Setters y getters nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Setters y getters marca
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    # Setters y getters grado de alcohol
    @property
    def grado_alcohol(self):
        return self._grado_alcohol

    @grado_alcohol.setter
    def grado_alcohol(self, grado_alcohol):
        self.validar_grado_alcohol(grado_alcohol)
        self._grado_alcohol = grado_alcohol

    # Setters y getters precio
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = precio

    # metodo para validar el grado de alcohol
    def validar_grado_alcohol(self, grado_alcohol):
        if grado_alcohol < 0 or grado_alcohol > 100:
            raise ValueError("El grado de alcohol debe estar entre 0 y 100.")

    # metodo para mostrar informacion de la bebida
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Marca: {self.marca}, Grado de Alcohol: {self.grado_alcohol}%, Precio: ${self.precio:.2f}"

# Clase que hereda de Bebida
class Cerveza(Bebida):
    def __init__(self, nombre, marca, grado_alcohol, precio, tipo):
        super().__init__(nombre, marca, grado_alcohol, precio)
        self._tipo = tipo

    # Setters y getters tipo
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    # metodo para mostrar informacion que hereda de la clase Bebida
    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Tipo: {self.tipo}"

# subclase Vino que hereda de Cerveza
class Vino(Cerveza):
    def __init__(self, nombre, marca, grado_alcohol, precio, tipo, anio):
        super().__init__(nombre, marca, grado_alcohol, precio, tipo)
        self._anio = anio
        self.validar_anio(anio)

    # Setters y getters anio
    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, anio):
        self.validar_anio(anio)
        self._anio = anio

    # metodo para validar anio
    def validar_anio(self, anio):
        if  anio > 2024:
            raise ValueError("El año debe ser igual o menor año actual.")

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Año: {self.anio}"

# sub clase que hereda de bebida
class Licor(Bebida):
    def __init__(self, nombre, marca, grado_alcohol, precio, sabor):
        super().__init__(nombre, marca, grado_alcohol, precio)
        self._sabor = sabor

    # getters y setters sabor
    @property
    def sabor(self):
        return self._sabor

    @sabor.setter
    def sabor(self, sabor):
        self._sabor = sabor

    # metodo para mostrar informacion que hereda de la clase padre
    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Sabor: {self.sabor}"

# clase registro de ventas para llevar un control de las ventas
class RegistroVentas:
    def __init__(self):
        self.ventas = {}  # para almacenar la cantidad vendida de cada bebida
        self.ganancias_totales = 0.0  # ganancias totales

    # metodo para registrar las ventas
    def registrar_venta(self, bebida):
        if bebida.nombre in self.ventas:
            self.ventas[bebida.nombre] += 1
        else:
            self.ventas[bebida.nombre] = 1
        self.ganancias_totales += bebida.precio  # agregar el precio de la bebida a las ganancias

    # metodo para mostrar el informe de ventas
    def mostrar_informe(self):
        print("\n--- Informe de Ventas ---")
        for nombre_bebida, cantidad in self.ventas.items():
            print(f"{nombre_bebida}: {cantidad} vendidos")
        print(f"Ganancias Totales: ${self.ganancias_totales:.2f}")

# clase para manejar la cuenta de un cliente
class Cuenta:
    def __init__(self, cliente):
        self.cliente = cliente
        self.bebidas = []  # lista de bebidas consumidas

    # metodo para agregar bebidas a la cuenta del cliente
    def agregar_bebida(self, bebida):
        self.bebidas.append(bebida)

    # metodo para mostrar el ticket final del cliente
    def mostrar_ticket(self):
        total = sum(bebida.precio for bebida in self.bebidas)
        ticket = f"--- Ticket para {self.cliente.nombre} ---\n"
        for bebida in self.bebidas:
            ticket += f"{bebida.nombre} - ${bebida.precio:.2f}\n"
        ticket += f"Total: ${total:.2f}\n"

        # aplicar descuento si es VIP
        if isinstance(self.cliente, VIP):
            descuento = self.cliente.descuento / 100
            total_descuento = total * descuento
            ticket += f"Descuento: ${total_descuento:.2f}\n"
            total -= total_descuento

        ticket += f"Total a Pagar: ${total:.2f}\n"
        return ticket


# variables globales para almacenar las ventas
registro_ventas = RegistroVentas()

# clase para crear clientes
class Cliente:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        self.validar_edad(edad)
        self.cuenta = None

    # getter y setter nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # getter y setter edad
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self.validar_edad(edad)
        self._edad = edad

    # metodo para validar edad
    def validar_edad(self, edad):
        if edad < 18:
            raise ValueError("La edad debe ser mayor o igual a 18.")

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# subclase de Cliente
class Regular(Cliente):
    def __init__(self, nombre, edad, frecuencia_visitas):
        super().__init__(nombre, edad)
        self._frecuencia_visitas = frecuencia_visitas
        self.validar_frecuencia_visitas(frecuencia_visitas)

    # getter y setter de frencuencia de visitas
    @property
    def frecuencia_visitas(self):
        return self._frecuencia_visitas

    @frecuencia_visitas.setter
    def frecuencia_visitas(self, frecuencia_visitas):
        self.validar_frecuencia_visitas(frecuencia_visitas)
        self._frecuencia_visitas = frecuencia_visitas

    # validacion de frecuencia de visitas
    def validar_frecuencia_visitas(self, frecuencia_visitas):
        if frecuencia_visitas < 0:
            raise ValueError("La frecuencia de visitas no puede ser negativa.")

    # metodo mostrar informacion heredado de clase padre
    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Frecuencia de Visitas: {self.frecuencia_visitas} veces por mes"


# sub clase cliente VIP
class VIP(Cliente):
    def __init__(self, nombre, edad, descuento):
        super().__init__(nombre, edad)
        self._descuento = descuento
        self.validar_descuento(descuento)

    # getter y setter descuento
    @property
    def descuento(self):
        return self._descuento

    @descuento.setter
    def descuento(self, descuento):
        self.validar_descuento(descuento)
        self._descuento = descuento

    # metodo para validar descuentos
    def validar_descuento(self, descuento):
        if descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

    # metodo heredado para mostrar informacion agregando atributos extras de la subclase
    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Descuento: {self.descuento}%"

# funcion gestion para mostrar funcionamiento del programa
def gestion():
    bar = cargar_bebidas()  # cargar bebidas desde CSV
    clientes = []  # lista de clientes

    while True:
        print("\n*** Gestion de Bar 'Popeye' ***")
        print("1. Agregar Cliente")
        print("2. Mostrar Bebidas")
        print("3. Mostrar Clientes")
        print("4. Abrir Cuenta")
        print("5. Informe de Ventas")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_cliente(clientes)
        elif opcion == "2":
            mostrar_bebidas(bar)
        elif opcion == "3":
            mostrar_clientes(clientes)
        elif opcion == "4":
            abrir_cuenta(clientes, bar)
        elif opcion == "5":
            registro_ventas.mostrar_informe()
        elif opcion == "6":
            print("Vuelve pronto :D")
            break
        else:
            print("Opción no válida. Por favor intenta de nuevo.")


# funcion para cargar bebidas desde el archivo CSV
def cargar_bebidas():
    try:
        df = pd.read_csv("bebidas.csv")
        bebidas = []
        for index, row in df.iterrows():
            tipo = row['tipo']
            if tipo == 'Cerveza':
                bebida = Cerveza(row['nombre'], row['marca'], row['grado_alcohol'], row['precio'], row['sabor'])
            elif tipo == 'Vino':
                bebida = Vino(row['nombre'], row['marca'], row['grado_alcohol'], row['precio'], row['sabor'], row['o_anio'])
            elif tipo == 'Licor':
                bebida = Licor(row['nombre'], row['marca'], row['grado_alcohol'], row['precio'], row['sabor'])
            else:
                continue
            bebidas.append(bebida)
        return bebidas
    except FileNotFoundError:
        print("Error: El archivo bebidas.csv no fue encontrado.")
        return []


# función para mostrar las bebidas del bar
def mostrar_bebidas(bar):
    print("\n--- Bebidas en el Bar ---")
    if not bar:
        print("No hay bebidas disponibles.")
    else:
        for bebida in bar:
            print(bebida.mostrar_informacion())


# funcion para mostrar clientes del bar
def mostrar_clientes(clientes):
    print("\n--- Clientes del Bar ---")
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for cliente in clientes:
            print(cliente.mostrar_informacion())


# funcion para agregar clientes
def agregar_cliente(clientes):
    print("\n*** Agregar Cliente ***")
    tipo = input("Tipo (regular, vip): ").lower()
    nombre = input("Nombre: ")

    try:
        edad = int(input("Edad: "))
    except ValueError:
        print("Error: La edad debe ser un número entero.")
        return

    if tipo == "regular":
        try:
            frecuencia_visitas = int(input("Frecuencia de Visitas (veces por mes): "))
            cliente = Regular(nombre, edad, frecuencia_visitas)
        except ValueError as e:
            print(f"Error: {e}")
            return
    elif tipo == "vip":
        try:
            descuento = float(input("Descuento (%): "))
            cliente = VIP(nombre, edad, descuento)
        except ValueError as e:
            print(f"Error: {e}")
            return
    else:
        print("Tipo de cliente no válido.")
        return

    clientes.append(cliente)
    print("Cliente agregado exitosamente.")

# funcion para abrir una cuenta para un cliente
def abrir_cuenta(clientes, bar):
    print("\n*** Abrir Cuenta ***")
    nombre_cliente = input("Nombre del cliente: ")

    cliente = next((c for c in clientes if c.nombre.lower() == nombre_cliente.lower()), None)

    if cliente is None:
        print("Cliente no encontrado.")
        return

    # inicializamos una cuenta para el cliente si no tiene una
    if not hasattr(cliente, 'cuenta') or cliente.cuenta is None:
        cliente.cuenta = Cuenta(cliente)

    while True:
        mostrar_bebidas(bar)  # mostrar las bebidas disponibles
        bebida_nombre = input("¿Qué bebida desea pedir? (escriba 'salir' para terminar): ")

        if bebida_nombre.lower() == 'salir':
            # registrar las ventas al cerrar la cuenta
            for bebida in cliente.cuenta.bebidas:
                registro_ventas.registrar_venta(bebida)
            break

        bebida = next((b for b in bar if b.nombre.lower() == bebida_nombre.lower()), None)

        if bebida is None:
            print("Bebida no encontrada.")
        else:
            cliente.cuenta.agregar_bebida(bebida)
            print(f"{bebida.nombre} ha sido agregada a la cuenta de {cliente.nombre}.")

    # mostrar el ticket
    print(cliente.cuenta.mostrar_ticket())

if __name__ == "__main__":
    gestion()






