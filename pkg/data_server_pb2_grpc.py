# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pkg import data_server_pb2 as pkg_dot_data__server__pb2


class TrainingDataServiceStub(object):
    """The service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Convert = channel.stream_stream(
                '/data_server.TrainingDataService/Convert',
                request_serializer=pkg_dot_data__server__pb2.RawDataRequest.SerializeToString,
                response_deserializer=pkg_dot_data__server__pb2.ResponseStatus.FromString,
                )
        self.GetTrainingData = channel.unary_unary(
                '/data_server.TrainingDataService/GetTrainingData',
                request_serializer=pkg_dot_data__server__pb2.GetTrainingDataRequest.SerializeToString,
                response_deserializer=pkg_dot_data__server__pb2.TrainingData.FromString,
                )
        self.AddTrainingData = channel.stream_stream(
                '/data_server.TrainingDataService/AddTrainingData',
                request_serializer=pkg_dot_data__server__pb2.MoreRawData.SerializeToString,
                response_deserializer=pkg_dot_data__server__pb2.ResponseStatus.FromString,
                )
        self.RemoveTrainingData = channel.unary_unary(
                '/data_server.TrainingDataService/RemoveTrainingData',
                request_serializer=pkg_dot_data__server__pb2.RemoveRequest.SerializeToString,
                response_deserializer=pkg_dot_data__server__pb2.ResponseStatus.FromString,
                )


class TrainingDataServiceServicer(object):
    """The service definition
    """

    def Convert(self, request_iterator, context):
        """Convert raw data to training data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTrainingData(self, request, context):
        """Return the final data created
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddTrainingData(self, request_iterator, context):
        """Convert and append new raw data to existing training data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveTrainingData(self, request, context):
        """Delete x lines of training data from the file
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrainingDataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Convert': grpc.stream_stream_rpc_method_handler(
                    servicer.Convert,
                    request_deserializer=pkg_dot_data__server__pb2.RawDataRequest.FromString,
                    response_serializer=pkg_dot_data__server__pb2.ResponseStatus.SerializeToString,
            ),
            'GetTrainingData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTrainingData,
                    request_deserializer=pkg_dot_data__server__pb2.GetTrainingDataRequest.FromString,
                    response_serializer=pkg_dot_data__server__pb2.TrainingData.SerializeToString,
            ),
            'AddTrainingData': grpc.stream_stream_rpc_method_handler(
                    servicer.AddTrainingData,
                    request_deserializer=pkg_dot_data__server__pb2.MoreRawData.FromString,
                    response_serializer=pkg_dot_data__server__pb2.ResponseStatus.SerializeToString,
            ),
            'RemoveTrainingData': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveTrainingData,
                    request_deserializer=pkg_dot_data__server__pb2.RemoveRequest.FromString,
                    response_serializer=pkg_dot_data__server__pb2.ResponseStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'data_server.TrainingDataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TrainingDataService(object):
    """The service definition
    """

    @staticmethod
    def Convert(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/data_server.TrainingDataService/Convert',
            pkg_dot_data__server__pb2.RawDataRequest.SerializeToString,
            pkg_dot_data__server__pb2.ResponseStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTrainingData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data_server.TrainingDataService/GetTrainingData',
            pkg_dot_data__server__pb2.GetTrainingDataRequest.SerializeToString,
            pkg_dot_data__server__pb2.TrainingData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddTrainingData(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/data_server.TrainingDataService/AddTrainingData',
            pkg_dot_data__server__pb2.MoreRawData.SerializeToString,
            pkg_dot_data__server__pb2.ResponseStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveTrainingData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/data_server.TrainingDataService/RemoveTrainingData',
            pkg_dot_data__server__pb2.RemoveRequest.SerializeToString,
            pkg_dot_data__server__pb2.ResponseStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)