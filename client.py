# https://grpc.io/docs/languages/python/basics/
# To run start server.py in one terminal and run client.py in another terminal.
import grpc
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import time

# import the generated classes
import protos.sleep_pb2 as sleep_pb2
import protos.sleep_pb2_grpc as sleep_pb2_grpc


class GrpcClient:

    # open a gRPC channel (You should share a single channel across threads)
    channel = grpc.insecure_channel('localhost:50051')

    def __init__(self):
        self.executor = ThreadPoolExecutor()

    def sleep(self, seconds, callback):
        # create a stub (client)
        stub = sleep_pb2_grpc.SleepTimeStub(self.__class__.channel)
        print(f'sending {seconds} seconds...')
        number = sleep_pb2.Seconds(value=seconds)
        # call service method Sleep
        future = self.executor.submit(stub.Sleep, number)
        #future.add_done_callback(self.callback)
        future.add_done_callback(callback)
