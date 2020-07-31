# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import Callable, Dict, Optional, Sequence, Tuple

from google.api_core import grpc_helpers   # type: ignore
from google.api_core import operations_v1  # type: ignore
from google import auth                    # type: ignore
from google.auth import credentials        # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore


import grpc  # type: ignore

from google.cloud.functions_v1.types import functions
from google.iam.v1 import iam_policy_pb2 as iam_policy  # type: ignore
from google.iam.v1 import policy_pb2 as policy  # type: ignore
from google.longrunning import operations_pb2 as operations  # type: ignore

from .base import CloudFunctionsServiceTransport


class CloudFunctionsServiceGrpcTransport(CloudFunctionsServiceTransport):
    """gRPC backend transport for CloudFunctionsService.

    A service that application uses to manipulate triggers and
    functions.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """
    _stubs: Dict[str, Callable]

    def __init__(self, *,
            host: str = 'cloudfunctions.googleapis.com',
            credentials: credentials.Credentials = None,
            credentials_file: str = None,
            scopes: Sequence[str] = None,
            channel: grpc.Channel = None,
            api_mtls_endpoint: str = None,
            client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
            quota_project_id: Optional[str] = None) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]): The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): The mutual TLS endpoint. If
                provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]): A
                callback to provide client SSL certificate bytes and private key
                bytes, both in PEM format. It is ignored if ``api_mtls_endpoint``
                is None.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        if channel:
            # Sanity check: Ensure that channel and credentials are not both
            # provided.
            credentials = False

            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
        elif api_mtls_endpoint:
            host = api_mtls_endpoint if ":" in api_mtls_endpoint else api_mtls_endpoint + ":443"

            if credentials is None:
                credentials, _ = auth.default(scopes=self.AUTH_SCOPES, quota_project_id=quota_project_id)

            # Create SSL credentials with client_cert_source or application
            # default SSL credentials.
            if client_cert_source:
                cert, key = client_cert_source()
                ssl_credentials = grpc.ssl_channel_credentials(
                    certificate_chain=cert, private_key=key
                )
            else:
                ssl_credentials = SslCredentials().ssl_credentials

            # create a new channel. The provided one is ignored.
            self._grpc_channel = type(self).create_channel(
                host,
                credentials=credentials,
                credentials_file=credentials_file,
                ssl_credentials=ssl_credentials,
                scopes=scopes or self.AUTH_SCOPES,
                quota_project_id=quota_project_id,
            )

        self._stubs = {}  # type: Dict[str, Callable]

        # Run the base constructor.
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes or self.AUTH_SCOPES,
            quota_project_id=quota_project_id,
        )

    @classmethod
    def create_channel(cls,
                       host: str = 'cloudfunctions.googleapis.com',
                       credentials: credentials.Credentials = None,
                       credentials_file: str = None,
                       scopes: Optional[Sequence[str]] = None,
                       quota_project_id: Optional[str] = None,
                       **kwargs) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            address (Optionsl[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        scopes = scopes or cls.AUTH_SCOPES
        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            **kwargs
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Sanity check: Only create a new channel if we do not already
        # have one.
        if not hasattr(self, '_grpc_channel'):
            self._grpc_channel = self.create_channel(
                self._host,
                credentials=self._credentials,
            )

        # Return the channel from cache.
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Sanity check: Only create a new client if we do not already have one.
        if 'operations_client' not in self.__dict__:
            self.__dict__['operations_client'] = operations_v1.OperationsClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self.__dict__['operations_client']

    @property
    def list_functions(self) -> Callable[
            [functions.ListFunctionsRequest],
            functions.ListFunctionsResponse]:
        r"""Return a callable for the list functions method over gRPC.

        Returns a list of functions that belong to the
        requested project.

        Returns:
            Callable[[~.ListFunctionsRequest],
                    ~.ListFunctionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_functions' not in self._stubs:
            self._stubs['list_functions'] = self.grpc_channel.unary_unary(
                '/google.cloud.functions.v1.CloudFunctionsService/ListFunctions',
                request_serializer=functions.ListFunctionsRequest.serialize,
                response_deserializer=functions.ListFunctionsResponse.deserialize,
            )
        return self._stubs['list_functions']

    @property
    def get_function(self) -> Callable[
            [functions.GetFunctionRequest],
            functions.CloudFunction]:
        r"""Return a callable for the get function method over gRPC.

        Returns a function with the given name from the
        requested project.

        Returns:
            Callable[[~.GetFunctionRequest],
                    ~.CloudFunction]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_function' not in self._stubs:
            self._stubs['get_function'] = self.grpc_channel.unary_unary(
                '/google.cloud.functions.v1.CloudFunctionsService/GetFunction',
                request_serializer=functions.GetFunctionRequest.serialize,
                response_deserializer=functions.CloudFunction.deserialize,
            )
        return self._stubs['get_function']

    @property
    def create_function(self) -> Callable[
            [functions.CreateFunctionRequest],
            operations.Operation]:
        r"""Return a callable for the create function method over gRPC.

        Creates a new function. If a function with the given name
        already exists in the specified project, the long running
        operation will return ``ALREADY_EXISTS`` error.

        Returns:
            Callable[[~.CreateFunctionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_function' not in self._stubs:
            self._stubs['create_function'] = self.grpc_channel.unary_unary(
                '/google.cloud.functions.v1.CloudFunctionsService/CreateFunction',
                request_serializer=functions.CreateFunctionRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs['create_function']

    @property
    def update_function(self) -> Callable[
            [functions.UpdateFunctionRequest],
            operations.Operation]:
        r"""Return a callable for the update function method over gRPC.

        Updates existing function.

        Returns:
            Callable[[~.UpdateFunctionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_function' not in self._stubs:
            self._stubs['update_function'] = self.grpc_channel.unary_unary(
                '/google.cloud.functions.v1.CloudFunctionsService/UpdateFunction',
                request_serializer=functions.UpdateFunctionRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs['update_function']

    @property
    def delete_function(self) -> Callable[
            [functions.DeleteFunctionRequest],
            operations.Operation]:
        r"""Return a callable for the delete function method over gRPC.

        Deletes a function with the given name from the
        specified project. If the given function is used by some
        trigger, the trigger will be updated to remove this
        function.

        Returns:
            Callable[[~.DeleteFunctionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_function' not in self._stubs:
            self._stubs['delete_function'] = self.grpc_channel.unary_unary(
                '/google.cloud.functions.v1.CloudFunctionsService/DeleteFunction',
                request_serializer=functions.DeleteFunctionRequest.serialize,
                response_deserializer=operations.Operation.FromString,
            )
        return self._stubs['delete_function']

    @property
    def call_function(self) -> Callable[
            [functions.CallFunctionRequest],
            functions.CallFunctionResponse]:
        r"""Return a callable for the call function method over gRPC.

        Synchronously invokes a deployed Cloud Function. To be used for
        testing purposes as very limited traffic is allowed. For more
        information on the actual limits, refer to `Rate
        Limits <https://cloud.google.com/functions/quotas#rate_limits>`__.

        Returns:
            Callable[[~.CallFunctionRequest],
                    ~.CallFunctionResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'call_function' not in self._stubs:
            self._stubs['call_function'] = self.grpc_channel.unary_unary(
                '/google.cloud.functions.v1.CloudFunctionsService/CallFunction',
                request_serializer=functions.CallFunctionRequest.serialize,
                response_deserializer=functions.CallFunctionResponse.deserialize,
            )
        return self._stubs['call_function']

    @property
    def generate_upload_url(self) -> Callable[
            [functions.GenerateUploadUrlRequest],
            functions.GenerateUploadUrlResponse]:
        r"""Return a callable for the generate upload url method over gRPC.

        Returns a signed URL for uploading a function source code. For
        more information about the signed URL usage see:
        https://cloud.google.com/storage/docs/access-control/signed-urls.
        Once the function source code upload is complete, the used
        signed URL should be provided in CreateFunction or
        UpdateFunction request as a reference to the function source
        code.

        When uploading source code to the generated signed URL, please
        follow these restrictions:

        -  Source file type should be a zip file.
        -  Source file size should not exceed 100MB limit.
        -  No credentials should be attached - the signed URLs provide
           access to the target bucket using internal service identity;
           if credentials were attached, the identity from the
           credentials would be used, but that identity does not have
           permissions to upload files to the URL.

        When making a HTTP PUT request, these two headers need to be
        specified:

        -  ``content-type: application/zip``
        -  ``x-goog-content-length-range: 0,104857600``

        And this header SHOULD NOT be specified:

        -  ``Authorization: Bearer YOUR_TOKEN``

        Returns:
            Callable[[~.GenerateUploadUrlRequest],
                    ~.GenerateUploadUrlResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'generate_upload_url' not in self._stubs:
            self._stubs['generate_upload_url'] = self.grpc_channel.unary_unary(
                '/google.cloud.functions.v1.CloudFunctionsService/GenerateUploadUrl',
                request_serializer=functions.GenerateUploadUrlRequest.serialize,
                response_deserializer=functions.GenerateUploadUrlResponse.deserialize,
            )
        return self._stubs['generate_upload_url']

    @property
    def generate_download_url(self) -> Callable[
            [functions.GenerateDownloadUrlRequest],
            functions.GenerateDownloadUrlResponse]:
        r"""Return a callable for the generate download url method over gRPC.

        Returns a signed URL for downloading deployed
        function source code. The URL is only valid for a
        limited period and should be used within minutes after
        generation.
        For more information about the signed URL usage see:
        https://cloud.google.com/storage/docs/access-
        control/signed-urls

        Returns:
            Callable[[~.GenerateDownloadUrlRequest],
                    ~.GenerateDownloadUrlResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'generate_download_url' not in self._stubs:
            self._stubs['generate_download_url'] = self.grpc_channel.unary_unary(
                '/google.cloud.functions.v1.CloudFunctionsService/GenerateDownloadUrl',
                request_serializer=functions.GenerateDownloadUrlRequest.serialize,
                response_deserializer=functions.GenerateDownloadUrlResponse.deserialize,
            )
        return self._stubs['generate_download_url']

    @property
    def set_iam_policy(self) -> Callable[
            [iam_policy.SetIamPolicyRequest],
            policy.Policy]:
        r"""Return a callable for the set iam policy method over gRPC.

        Sets the IAM access control policy on the specified
        function. Replaces any existing policy.

        Returns:
            Callable[[~.SetIamPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'set_iam_policy' not in self._stubs:
            self._stubs['set_iam_policy'] = self.grpc_channel.unary_unary(
                '/google.cloud.functions.v1.CloudFunctionsService/SetIamPolicy',
                request_serializer=iam_policy.SetIamPolicyRequest.SerializeToString,
                response_deserializer=policy.Policy.FromString,
            )
        return self._stubs['set_iam_policy']

    @property
    def get_iam_policy(self) -> Callable[
            [iam_policy.GetIamPolicyRequest],
            policy.Policy]:
        r"""Return a callable for the get iam policy method over gRPC.

        Gets the IAM access control policy for a function.
        Returns an empty policy if the function exists and does
        not have a policy set.

        Returns:
            Callable[[~.GetIamPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_iam_policy' not in self._stubs:
            self._stubs['get_iam_policy'] = self.grpc_channel.unary_unary(
                '/google.cloud.functions.v1.CloudFunctionsService/GetIamPolicy',
                request_serializer=iam_policy.GetIamPolicyRequest.SerializeToString,
                response_deserializer=policy.Policy.FromString,
            )
        return self._stubs['get_iam_policy']

    @property
    def test_iam_permissions(self) -> Callable[
            [iam_policy.TestIamPermissionsRequest],
            iam_policy.TestIamPermissionsResponse]:
        r"""Return a callable for the test iam permissions method over gRPC.

        Tests the specified permissions against the IAM access control
        policy for a function. If the function does not exist, this will
        return an empty set of permissions, not a NOT_FOUND error.

        Returns:
            Callable[[~.TestIamPermissionsRequest],
                    ~.TestIamPermissionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'test_iam_permissions' not in self._stubs:
            self._stubs['test_iam_permissions'] = self.grpc_channel.unary_unary(
                '/google.cloud.functions.v1.CloudFunctionsService/TestIamPermissions',
                request_serializer=iam_policy.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy.TestIamPermissionsResponse.FromString,
            )
        return self._stubs['test_iam_permissions']


__all__ = (
    'CloudFunctionsServiceGrpcTransport',
)
