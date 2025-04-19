from pymongo import MongoClient
from bson.binary import Binary
from bson import ObjectId
import os
class MongoDBManager:
    def __init__(self, uri, base_de_datos, coleccion):
        # Conectar a MongoDB
        self.cliente = MongoClient(uri)
        self.base_de_datos = self.cliente[base_de_datos]
        self.coleccion = self.base_de_datos[coleccion]

    def insertar_documento(self, documento):
        """Inserta un documento en la colección."""
        resultado = self.coleccion.insert_one(documento)

    def consultar_documentos(self, filtro={}):
        """Consulta documentos en la colección."""
        documentos = self.coleccion.find(filtro)
        return list(documentos)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancia de la clase

    gestor = MongoDBManager("mongodb://localhost:27017/", "BaseMongoProyectoFinal", "Novelas")

    with open(os.path.abspath("../assets/images/LosJuegosDelHambreSinsajoParte1.jpg"), "rb") as archivo_imagen:
            datos_binarios = Binary(archivo_imagen.read())  
    # Insertar un documento
    documento = {"_id": ObjectId(), 
                "original": True, 
                "name":"Los Juegos Del Hambre Sinsajo Parte 1",
                "img":datos_binarios,
                "páginas":["página4", "Página5","6"],
                "finalizado": True,
                "meGusta": 856,
                "comentarios": ["Me encanta esta novela", "No me gusta el final"],
                "calificación": 4.5}
    gestor.insertar_documento(documento)

    # Consultar documentos
    # resultados = gestor.consultar_documentos({"name": "Los Juegos Del Hambre Sinsajo Parte 1"})
    # print("Documentos encontrados:", resultados)
