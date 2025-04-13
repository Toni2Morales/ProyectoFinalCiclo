from pymongo import MongoClient

def ejecutar_consulta_mongodb(host, puerto, nombre_base_datos, nombre_coleccion, consulta):
    """
    Realiza una consulta a MongoDB.

    :param host: Dirección del servidor MongoDB (por ejemplo, "localhost").
    :param puerto: Puerto del servidor MongoDB (por ejemplo, 27017).
    :param nombre_base_datos: Nombre de la base de datos.
    :param nombre_coleccion: Nombre de la colección.
    :param consulta: Consulta a ejecutar (por ejemplo, {"campo": "valor"}).
    :return: Resultado de la consulta.
    """
    try:
        # Conectar al cliente MongoDB
        cliente = MongoClient(host, puerto)
        
        # Seleccionar la base de datos
        base_datos = cliente[nombre_base_datos]
        
        # Seleccionar la colección
        coleccion = base_datos[nombre_coleccion]
        
        # Ejecutar la consulta
        resultados = coleccion.find(consulta)
        
        # Convertir los resultados a una lista
        lista_resultados = list(resultados)
        
        # Cerrar la conexión
        cliente.close()
        
        return lista_resultados
    
    except Exception as e:
        print("Error al ejecutar la consulta:", e)
        return None

# Ejemplo de uso
host = "localhost"
puerto = 27017
nombre_base_datos = "BaseMongoProyectoFinal"
nombre_coleccion = "Novelas"
consulta = {"original": True}

resultados = ejecutar_consulta_mongodb(host, puerto, nombre_base_datos, nombre_coleccion, consulta)
print(resultados)
