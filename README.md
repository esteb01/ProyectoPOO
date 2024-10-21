# Proyecto POO Gestión de Bar
"Proyecto de Programacion Orientada a Objetos"

Este proyecto implementa un sistema de gestión para un bar utilizando Programación Orientada a Objetos (POO) en Python. Permite manejar la información de bebidas, registrar ventas y gestionar cuentas de clientes.

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Requisitos](#requisitos)
- [Instalacion](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Caracteristicas](#características)
- [Clases Principales](#clases-principales)
- [Herencia](#herencia)
- [Manejo de Excepciones](#manejo-de-excepciones)
- [Ejemplo de Uso_con_Codigo](#ejemplo-de-uso-con-codigo)
- [Ejemplo de Uso en Interfaz](#ejemplo-de-uso-en-interfaz)
- [Contribución](#contribución)

## Descripción del Proyecto

El objetivo de este proyecto es gestionar un bar, manteniendo un registro de las bebidas disponibles, las ventas realizadas y las cuentas de los clientes. Se utiliza POO para modelar las bebidas y los clientes del bar, haciendo uso de herencia y manejo de excepciones.

## Requisitos

- Python 3.7 o superior
- Pandas

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/esteb01/ProyectoPOO.git
    cd ProyectoPOO
    ```

2. Instala las dependencias:
    ```bash
    pip install pandas
    ```

3. Asegúrate de tener un archivo `bebidas.csv` en el directorio del proyecto con el siguiente formato:

    ```csv
    nombre,marca,grado_alcohol,precio,tipo,sabor,o_anio
    Corona,Grupo Modelo,4.5,1.2,Cerveza,Lager,
    Cabernet Sauvignon,Concha y Toro,13.5,15.0,Vino,Tinto,2018
    Whisky,Jack Daniels,40.0,25.0,Licor,Dulce,
    ```

## Uso

Ejecuta el script principal:

```bash
python gestion_bar.py
```

Sigue las instrucciones en pantalla para interactuar con el sistema.

## Estructura del Proyecto

- `bebidas.csv`: Archivo CSV con la información de las bebidas.
- `gestion_bar.py`: Script principal que contiene la lógica del bar.
- `README.md`: Documentación del proyecto.

## Características

- **Clases y Herencia**:
  - Clase base `Bebida` con subclases `Cerveza`, `Vino` y `Licor`.
  - Clase base `Cliente` con subclases `Regular` y `VIP`.

- **Funciones Principales**:
  - Agregar clientes (Regular o VIP).
  - Mostrar bebidas disponibles cargadas desde un archivo CSV.
  - Mostrar clientes registrados.
  - Abrir cuentas para clientes, agregar bebidas a la cuenta y generar un ticket.
  - Aplicar descuentos a clientes VIP.
  - Registrar ventas y mostrar un informe de ventas.

- **Descripcion de Clases y Herencias**:
## Clases Principales

### Clase `Bebida`

Representa una bebida genérica en el bar.

- **Atributos:**
  - `nombre`: Nombre de la bebida.
  - `marca`: Marca de la bebida.
  - `grado_alcohol`: Grado de alcohol de la bebida.
  - `precio`: Precio de la bebida.

- **Métodos:**
  - `validar_grado_alcohol(grado_alcohol)`: Valida que el grado de alcohol esté entre 0 y 100.
  - `mostrar_informacion()`: Muestra la información de la bebida.

### Clase `Cerveza` (hereda de `Bebida`)

Representa una cerveza en el bar.

- **Atributos:**
  - `tipo`: Tipo de cerveza (e.g., Lager, IPA).

- **Métodos:**
  - `mostrar_informacion()`: Muestra la información de la cerveza, incluyendo el tipo.

### Clase `Vino` (hereda de `Cerveza`)

Representa un vino en el bar.

- **Atributos:**
  - `anio`: Año de producción del vino.

- **Métodos:**
  - `validar_anio(anio)`: Valida que el año sea menor o igual al año actual.
  - `mostrar_informacion()`: Muestra la información del vino, incluyendo el año.

### Clase `Licor` (hereda de `Bebida`)

Representa un licor en el bar.

- **Atributos:**
  - `sabor`: Sabor del licor (e.g., Chocolate, Fresa).

- **Métodos:**
  - `mostrar_informacion()`: Muestra la información del licor, incluyendo el sabor.

### Clase `RegistroVentas`

Lleva un registro de las ventas realizadas.

- **Atributos:**
  - `ventas`: Diccionario con las ventas realizadas.
  - `ganancias_totales`: Ganancias totales del bar.

- **Métodos:**
  - `registrar_venta(bebida)`: Registra una venta de una bebida.
  - `mostrar_informe()`: Muestra un informe de ventas.

### Clase `Cuenta`

Maneja la cuenta de un cliente en el bar.

- **Atributos:**
  - `cliente`: Cliente asociado a la cuenta.
  - `bebidas`: Lista de bebidas consumidas.

- **Métodos:**
  - `agregar_bebida(bebida)`: Agrega una bebida a la cuenta del cliente.
  - `mostrar_ticket()`: Muestra el ticket final de la cuenta.

### Clase `Cliente`

Representa un cliente genérico en el bar.

- **Atributos:**
  - `nombre`: Nombre del cliente.
  - `edad`: Edad del cliente.

- **Métodos:**
  - `validar_edad(edad)`: Valida que la edad sea mayor o igual a 18.
  - `mostrar_informacion()`: Muestra la información del cliente.

### Clase `Regular` (hereda de `Cliente`)

Representa un cliente regular en el bar.

- **Atributos:**
  - `frecuencia_visitas`: Frecuencia de visitas del cliente.

- **Métodos:**
  - `validar_frecuencia_visitas(frecuencia_visitas)`: Valida que la frecuencia de visitas no sea negativa.
  - `mostrar_informacion()`: Muestra la información del cliente, incluyendo la frecuencia de visitas.

### Clase `VIP` (hereda de `Cliente`)

Representa un cliente VIP en el bar.

- **Atributos:**
  - `descuento`: Descuento aplicable al cliente.

- **Métodos:**
  - `validar_descuento(descuento)`: Valida que el descuento esté entre 0 y 100.
  - `mostrar_informacion()`: Muestra la información del cliente, incluyendo el descuento.

## Herencia

La herencia se utiliza para crear clases específicas basadas en clases genéricas. Por ejemplo, `Cerveza`, `Vino` y `Licor` heredan de `Bebida`, y `Regular` y `VIP` heredan de `Cliente`. Esto permite reutilizar y extender funcionalidades de clases existentes.

## Manejo de Excepciones

El manejo de excepciones se utiliza para validar datos y manejar errores de forma controlada. Por ejemplo, se valida que el precio no sea negativo, que el grado de alcohol esté en un rango aceptable y que la edad del cliente sea mayor o igual a 18.

## Ejemplo de Uso con Codigo

Aquí hay un ejemplo básico de cómo utilizar el sistema:

### Crear bebidas
cerveza = Cerveza("Corona", "Corona", 4.5, 1.50, "Lager")
vino = Vino("Cabernet", "Casillero del Diablo", 13.5, 12.00, "Tinto", 2018)
licor = Licor("Tequila", "Jose Cuervo", 40, 25.00, "Blanco")

### Crear clientes
cliente1 = Regular("Juan Perez", 25, 4)
cliente2 = VIP("Maria Lopez", 30, 10)

### Crear cuenta y agregar bebidas
cuenta = Cuenta(cliente1)
cuenta.agregar_bebida(cerveza)
cuenta.agregar_bebida(vino)

### Mostrar ticket
print(cuenta.mostrar_ticket())

### Registrar venta
registro_ventas = RegistroVentas()
registro_ventas.registrar_venta(cerveza)
registro_ventas.registrar_venta(vino)

### Mostrar informe de ventas
registro_ventas.mostrar_informe()

## Ejemplo de Uso en Interfaz

1. **Agregar Cliente**:
    - Tipo: regular
    - Nombre: Juan
    - Edad: 25
    - Frecuencia de Visitas: 5

2. **Mostrar Bebidas**:
    - Lista de bebidas disponibles cargadas desde el archivo `bebidas.csv`.

3. **Mostrar Clientes**:
    - Lista de clientes registrados.

4. **Abrir Cuenta**:
    - Seleccionar cliente: Juan
    - Agregar bebidas a la cuenta
    - Mostrar el ticket final

5. **Informe de Ventas**:
    - Mostrar la cantidad de cada bebida vendida y las ganancias totales.

## Contribución

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.
