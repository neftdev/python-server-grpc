from concurrent import futures
import logging
import time
import grpc
import message.caso_pb2_grpc as caso_service
import message.caso_pb2 as caso_messages
from service.caso import CasoService

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

PORT = 9000

def gprc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    caso_service.add_CasoServicer_to_server(CasoService(), server)
    server.add_insecure_port(f'[::]:{PORT}')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info(f'Starting server. Listening on port {PORT}')
    gprc_server()
