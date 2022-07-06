
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ....cosmos.auth.v1beta1 import query_pb2 as cosmos_dot_auth_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    'Query defines the gRPC querier service.\n    '

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Accounts = channel.unary_unary('/cosmos.auth.v1beta1.Query/Accounts', request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsRequest.SerializeToString, response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsResponse.FromString)
        self.Account = channel.unary_unary('/cosmos.auth.v1beta1.Query/Account', request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountRequest.SerializeToString, response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountResponse.FromString)
        self.Params = channel.unary_unary('/cosmos.auth.v1beta1.Query/Params', request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString)
        self.ModuleAccounts = channel.unary_unary('/cosmos.auth.v1beta1.Query/ModuleAccounts', request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountsRequest.SerializeToString, response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountsResponse.FromString)
        self.Bech32Prefix = channel.unary_unary('/cosmos.auth.v1beta1.Query/Bech32Prefix', request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.Bech32PrefixRequest.SerializeToString, response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.Bech32PrefixResponse.FromString)
        self.AddressBytesToString = channel.unary_unary('/cosmos.auth.v1beta1.Query/AddressBytesToString', request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressBytesToStringRequest.SerializeToString, response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressBytesToStringResponse.FromString)
        self.AddressStringToBytes = channel.unary_unary('/cosmos.auth.v1beta1.Query/AddressStringToBytes', request_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressStringToBytesRequest.SerializeToString, response_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressStringToBytesResponse.FromString)

class QueryServicer(object):
    'Query defines the gRPC querier service.\n    '

    def Accounts(self, request, context):
        'Accounts returns all the existing accounts\n\n        Since: cosmos-sdk 0.43\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Account(self, request, context):
        'Account returns account details based on address.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        'Params queries all parameters.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModuleAccounts(self, request, context):
        'ModuleAccounts returns all the existing module accounts.\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Bech32Prefix(self, request, context):
        'Bech32 queries bech32Prefix\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddressBytesToString(self, request, context):
        'AddressBytesToString converts Account Address bytes to string\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddressStringToBytes(self, request, context):
        'AddressStringToBytes converts Address string to bytes\n        '
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Accounts': grpc.unary_unary_rpc_method_handler(servicer.Accounts, request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsRequest.FromString, response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsResponse.SerializeToString), 'Account': grpc.unary_unary_rpc_method_handler(servicer.Account, request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountRequest.FromString, response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'ModuleAccounts': grpc.unary_unary_rpc_method_handler(servicer.ModuleAccounts, request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountsRequest.FromString, response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountsResponse.SerializeToString), 'Bech32Prefix': grpc.unary_unary_rpc_method_handler(servicer.Bech32Prefix, request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.Bech32PrefixRequest.FromString, response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.Bech32PrefixResponse.SerializeToString), 'AddressBytesToString': grpc.unary_unary_rpc_method_handler(servicer.AddressBytesToString, request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressBytesToStringRequest.FromString, response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressBytesToStringResponse.SerializeToString), 'AddressStringToBytes': grpc.unary_unary_rpc_method_handler(servicer.AddressStringToBytes, request_deserializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressStringToBytesRequest.FromString, response_serializer=cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressStringToBytesResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.auth.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    'Query defines the gRPC querier service.\n    '

    @staticmethod
    def Accounts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.auth.v1beta1.Query/Accounts', cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsRequest.SerializeToString, cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Account(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.auth.v1beta1.Query/Account', cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountRequest.SerializeToString, cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryAccountResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.auth.v1beta1.Query/Params', cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModuleAccounts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.auth.v1beta1.Query/ModuleAccounts', cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountsRequest.SerializeToString, cosmos_dot_auth_dot_v1beta1_dot_query__pb2.QueryModuleAccountsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Bech32Prefix(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.auth.v1beta1.Query/Bech32Prefix', cosmos_dot_auth_dot_v1beta1_dot_query__pb2.Bech32PrefixRequest.SerializeToString, cosmos_dot_auth_dot_v1beta1_dot_query__pb2.Bech32PrefixResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddressBytesToString(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.auth.v1beta1.Query/AddressBytesToString', cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressBytesToStringRequest.SerializeToString, cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressBytesToStringResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddressStringToBytes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.auth.v1beta1.Query/AddressStringToBytes', cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressStringToBytesRequest.SerializeToString, cosmos_dot_auth_dot_v1beta1_dot_query__pb2.AddressStringToBytesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
