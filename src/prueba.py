from ConexionMongoDB import MongoDBManager
from PIL import Image as PILImage
import io
gestor = MongoDBManager("mongodb://localhost:27017/", "BaseMongoProyectoFinal", "Novelas")
resultados = gestor.consultar_documentos()

novela = resultados[0]
imagen = PILImage.open(io.BytesIO(novela["img"]))
# imagen.show()  # Verificar que la imagen es válida
imagen.save("../assets/imgTemporales/imagen.png")  # Guardar la imagen en un archivo