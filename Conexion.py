import sys
import pyodbc
Conexion = pyodbc.connect(
    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\LUIS\Documents\VS CODE\Sofware\Prueba.accdb;")
cursor = Conexion.cursor()


def MostrarMenu():
    print("\n1. Mostrar datos")
    print("2. Insertar datos")
    print("3. Actualizar datos")
    print("4. Eliminar datos")
    print("5. Salir")
    return input("Selecciona una opción: ")

# Funciones de operaciones en la base de datos


def MostrarEnTabla(NombreTabla):
    cursor.execute(f'SELECT * FROM {NombreTabla}')
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def InsertarEnTabla(NombreTabla, Valores):
    Pocisiones = ', '.join(['?'] * len(Valores))
    cursor.execute(
        f'INSERT INTO {NombreTabla} VALUES ({Pocisiones})', Valores)
    Conexion.commit()


def update_table(NombreTabla, ActulizarColumna, NuevoValor, CondicionColumna, CondicionValor):
    cursor.execute(
        f'UPDATE {NombreTabla} SET {ActulizarColumna} = ? WHERE {CondicionColumna} = ?', NuevoValor, CondicionValor)
    Conexion.commit()


def delete_from_table(NombreTabla, CondicionColumna, CondicionValor):
    cursor.execute(
        f'DELETE FROM {NombreTabla} WHERE {CondicionColumna} = ?', CondicionValor)
    Conexion.commit()


# Loop principal
while True:
    Eleccion = MostrarMenu()

    if Eleccion == "1":
        NombreTabla = input("\nIngrese el nombre de la tabla: ")
        MostrarEnTabla(NombreTabla)

    elif Eleccion == "2":
        NombreTabla = input("\nIngrese el nombre de la tabla: ")
        Valores = input(
            "Ingrese los valores a insertar (separados por comas): ").split(',')
        InsertarEnTabla(NombreTabla, Valores)

    elif Eleccion == "3":
        NombreTabla = input("\nIngrese el nombre de la tabla: ")
        ActulizarColumna = input(
            "Ingrese el nombre de la columna a actualizar: ")
        NuevoValor = input("Ingrese el nuevo valor: ")
        CondicionColumna = input("Ingrese la columna de condición: ")
        CondicionValor = input("Ingrese el valor de condición: ")
        update_table(NombreTabla, ActulizarColumna, NuevoValor,
                     CondicionColumna, CondicionValor)

    elif Eleccion == "4":
        NombreTabla = input("\nIngrese el nombre de la tabla: ")
        CondicionColumna = input("Ingrese la columna de condición: ")
        CondicionValor = input("Ingrese el valor de condición: ")
        delete_from_table(NombreTabla, CondicionColumna, CondicionValor)

    elif Eleccion == "5":
        # Salir del programa
        break

# Cerrar cursor y conexión
cursor.close()
Conexion.close()
