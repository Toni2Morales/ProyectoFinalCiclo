import mysql.connector
from mysql.connector import Error

def ejecutar_consulta(query, parametros=None):
    """
    Ejecuta una consulta SQL en una base de datos MySQL.

    :param query: Consulta SQL como una cadena (str).
    :param parametros: Parámetros para la consulta (tuple), opcional.
    :return: Resultados de la consulta como una lista de tuplas.
    """
    try:
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
            host='localhost',
            database='mi_base_datos',
            user='tu_usuario',
            password='tu_contraseña'
        )

        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.execute(query, parametros)
            resultados = cursor.fetchall()
            return resultados

    except Error as error:
        print(f"Error al conectar o ejecutar la consulta: {error}")
        return None

    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")

# Ejemplo de uso de la función
consulta = "SELECT * FROM usuarios WHERE edad > %s"
parametros = (18,)

resultados = ejecutar_consulta(consulta, parametros)

if resultados:
    for fila in resultados:
        print(f"ID: {fila[0]}, Nombre: {fila[1]}, Edad: {fila[2]}")
