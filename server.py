import grpc 
import time
from concurrent import futures 

import protos.sleep_pb2 as sleep_pb2
import protos.sleep_pb2_grpc as sleep_pb2_grpc

import sleep 

# create class to define server functions derived from
# sleep_pb2_grpc.SleepTimeServicer
class SleepTimeServicer(sleep_pb2_grpc.SleepTimeServicer):

    def Sleep(self, request, context):
        response = sleep_pb2.Seconds()
        response.value = sleep.sleep(request.value)
        return response

class GrpcServer:
    """
        Singleton class to init the GRPC server only once.
    """

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super(GrpcServer, cls).__new__(cls)
            # create gRPC server
            cls.server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
            # use generated function add_SleepTimeServicer_to_server to add
            # the defined class to the server
            sleep_pb2_grpc.add_SleepTimeServicer_to_server(SleepTimeServicer(), cls.server)

            # listen on port 50051
            print('start server and listen on port 50051')
            cls.server.add_insecure_port('[::]:50051')
            cls.server.start()
            cls.server.wait_for_termination()

        return cls._instance


if __name__ == "__main__":
    # start grpc server
    grpc_server = GrpcServer()
