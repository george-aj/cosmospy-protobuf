
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....cosmos.params.v1beta1 import query_pb2 as cosmos_dot_params_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Params = channel.unary_unary('/cosmos.params.v1beta1.Query/Params', request_serializer=cosmos_dot_params_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=cosmos_dot_params_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString)
        self.Subspaces = channel.unary_unary('/cosmos.params.v1beta1.Query/Subspaces', request_serializer=cosmos_dot_params_dot_v1beta1_dot_query__pb2.QuerySubspacesRequest.SerializeToString, response_deserializer=cosmos_dot_params_dot_v1beta1_dot_query__pb2.QuerySubspacesResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service.\n    '

    def Params(self, request, context):
        'Params queries a specific parameter of a module, given its subspace and\n        key.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subspaces(self, request, context):
        'Subspaces queries for all registered subspaces and all keys for a subspace.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=cosmos_dot_params_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=cosmos_dot_params_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'Subspaces': grpc.unary_unary_rpc_method_handler(servicer.Subspaces, request_deserializer=cosmos_dot_params_dot_v1beta1_dot_query__pb2.QuerySubspacesRequest.FromString, response_serializer=cosmos_dot_params_dot_v1beta1_dot_query__pb2.QuerySubspacesResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.params.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service.\n    '

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.params.v1beta1.Query/Params', cosmos_dot_params_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, cosmos_dot_params_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subspaces(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.params.v1beta1.Query/Subspaces', cosmos_dot_params_dot_v1beta1_dot_query__pb2.QuerySubspacesRequest.SerializeToString, cosmos_dot_params_dot_v1beta1_dot_query__pb2.QuerySubspacesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
