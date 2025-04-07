import mysql.connector
from mysql.connector import Error

def ejecutar_consulta(query, parametros=None):
    """
    Ejecuta una consulta SQL en una base de datos MySQL.

    :param query: Consulta SQL como una cadena (str).
    :param parametros: Parámetros para la consulta (tuple), opcional.
    :return: Resultados de la consulta como una lista de tuplas (si aplica).
    """
    try:
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='bbddproyecto',
            user='root',
            password='root'
        )

        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.execute(query, parametros)
            
            # Si la consulta es de tipo SELECT, obtén los resultados
            if query.strip().upper().startswith("SELECT"):
                resultados = cursor.fetchall()
                return resultados
            else:
                # Para consultas como INSERT, UPDATE o DELETE, haz commit
                conexion.commit()
                print("Consulta ejecutada correctamente.")
                return None

    except Error as error:
        print(f"Error al conectar o ejecutar la consulta: {error}")
        return None

    finally:
        if 'conexion' in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión cerrada.")


# Ejemplo de uso de la función
# correo ='ejemplo@email.com'
# consulta = f"SELECT * FROM usuarios WHERE correo = '{correo}'"
# # parametros = ()

# resultados = ejecutar_consulta(consulta)

# if resultados:
#     for fila in resultados:
#         print(f"ID: {fila[0]}, Correo: {fila[1]}, Contraseña: {fila[2]}")
