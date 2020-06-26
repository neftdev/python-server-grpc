from settings import MONGO_DB, MONGO_HOST, MONGO_PORT
from settings import REDIS_HOST, REDIS_PORT, REDIS_DB
from google.protobuf.json_format import MessageToDict
from pymongo import MongoClient
from redis import StrictRedis
import logging
import json
import message.caso_pb2_grpc as caso_service
import message.caso_pb2 as caso_messages

client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client[MONGO_DB]
casos_mongo = db.casos
casos_redis = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


class CasoService(caso_service.CasoServicer):
    def CrearCasos(self, request, context):
        logging.basicConfig(level=logging.INFO)
        logging.info('Insertando nuevo caso...')
        try:
            response = MessageToDict(request, preserving_proto_field_name=True)
            data_list = response["casos"]
            pipe = casos_redis.pipeline()
            for val in data_list:
                data = json.dumps(val)
                pipe.lpush('casos', data)
            pipe.execute()
            logging.info('Se ha insertado con exito en Redis')
            casos_mongo.insert_many(data_list)
            logging.info('Se ha insertado con exito en MongoDB')
            return caso_messages.CasoReply(mensaje='Se ha insertado un nuevo caso')
        except Exception as e:
            logging.warning(e)
            return caso_messages.CasoReply(mensaje='No se ha insertado el caso')
