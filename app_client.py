from client import GrpcClient
from random import randint


def callback(future):
    print(f'receiving {future.result().value} ')

def main():
    for i in range(5):
        grpc_client = GrpcClient()
        grpc_client.sleep(randint(1, 10), callback)


if __name__ == "__main__":
    main()

# python -m grpc_tools.protoc -I ./ --python_out=./ --grpc_python_out=./ ./protos/sleep.proto
