from concurrent import futures
import grpc
from pkg import data_server_pb2_grpc
from pkg import data_server_pb2

class TrainingDataService(data_server_pb2_grpc.TrainingDataServiceServicer):

    def Convert(self, request_iterator, context):
        # Implement your logic here
        # For example, yield trainingdata_pb2.ResponseStatus(status=trainingdata_pb2.ResponseStatus.SUCCESS)
        pass

    def GetTrainingData(self, request, context):
        # Implement your logic here
        # For example, return trainingdata_pb2.TrainingData(data='some training data')
        pass

    def AddTrainingData(self, request_iterator, context):
        # Implement your logic here
        pass

    def RemoveTrainingData(self, request, context):
        # Implement your logic here
        # For example, return trainingdata_pb2.ResponseStatus(status=trainingdata_pb2.ResponseStatus.SUCCESS)
        pass
