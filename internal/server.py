import grpc
from concurrent import futures
from pkg import data_server_pb2_grpc
from internal import methods

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    data_server_pb2_grpc.add_TrainingDataServiceServicer_to_server(methods.TrainingDataService(), server)
    
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on port 50051.")
    server.wait_for_termination()