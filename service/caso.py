from settings import MONGO_DB, MONGO_HOST, MONGO_PORT
from pymongo import MongoClient
import logging
import message.caso_pb2_grpc as caso_service
import message.caso_pb2 as caso_messages

class CasoService(caso_service.CasoServicer):
    def ConnectionMongo(self):
        client = MongoClient(MONGO_HOST, MONGO_PORT)
        db = client[MONGO_DB]
        return db.casos

    def CrearCaso(self, request, context):
        logging.basicConfig(level=logging.INFO)
        logging.info('Insertando nuevo caso...')
        casos = self.ConnectionMongo()
        nuevo_caso = {
            'nombre': request.nombre,
            'departamento': request.departamento,
            'edad': request.edad,
            'forma_contagio': request.forma_contagio,
            'estado': request.estado
        }
        casos.insert_one(nuevo_caso)
        return caso_messages.CasoReply(mensaje='Se ha insertado un nuevo caso')
