from settings import MONGO_DB, MONGO_HOST, MONGO_PORT
from settings import REDIS_HOST, REDIS_PORT, REDIS_DB
from pymongo import MongoClient
from redis import Redis
import logging
import json
import message.caso_pb2_grpc as caso_service
import message.caso_pb2 as caso_messages

client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client[MONGO_DB]
casos_mongo = db.casos
casos_redis = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


class CasoService(caso_service.CasoServicer):
    def CrearCaso(self, request, context):
        logging.basicConfig(level=logging.INFO)
        logging.info('Insertando nuevo caso...')
        try:
            nuevo_caso = {
                'nombre': request.nombre,
                'departamento': request.departamento,
                'edad': request.edad,
                'forma_contagio': request.forma_contagio,
                'estado': request.estado
            }
            r_nuevo = json.dumps(nuevo_caso)
            casos_redis.lpush('casos', r_nuevo)
            logging.info('Se ha insertado con exito en Redis')
            casos_mongo.insert_one(nuevo_caso)
            logging.info('Se ha insertado con exito en MongoDB')
            return caso_messages.CasoReply(mensaje='Se ha insertado un nuevo caso')
        except Exception as e:
            logging.warning(e)
            return caso_messages.CasoReply(mensaje='No se ha insertado el caso')
