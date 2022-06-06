# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.functions.v1",
    manifest={
        "CloudFunctionStatus",
        "CloudFunction",
        "SourceRepository",
        "HttpsTrigger",
        "EventTrigger",
        "FailurePolicy",
        "SecretEnvVar",
        "SecretVolume",
        "CreateFunctionRequest",
        "UpdateFunctionRequest",
        "GetFunctionRequest",
        "ListFunctionsRequest",
        "ListFunctionsResponse",
        "DeleteFunctionRequest",
        "CallFunctionRequest",
        "CallFunctionResponse",
        "GenerateUploadUrlRequest",
        "GenerateUploadUrlResponse",
        "GenerateDownloadUrlRequest",
        "GenerateDownloadUrlResponse",
    },
)


class CloudFunctionStatus(proto.Enum):
    r"""Describes the current stage of a deployment."""
    CLOUD_FUNCTION_STATUS_UNSPECIFIED = 0
    ACTIVE = 1
    OFFLINE = 2
    DEPLOY_IN_PROGRESS = 3
    DELETE_IN_PROGRESS = 4
    UNKNOWN = 5


class CloudFunction(proto.Message):
    r"""Describes a Cloud Function that contains user computation
    executed in response to an event. It encapsulate function and
    triggers configurations.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            A user-defined name of the function. Function names must be
            unique globally and match pattern
            ``projects/*/locations/*/functions/*``
        description (str):
            User-provided description of a function.
        source_archive_url (str):
            The Google Cloud Storage URL, starting with ``gs://``,
            pointing to the zip archive which contains the function.

            This field is a member of `oneof`_ ``source_code``.
        source_repository (google.cloud.functions_v1.types.SourceRepository):
            **Beta Feature**

            The source repository where a function is hosted.

            This field is a member of `oneof`_ ``source_code``.
        source_upload_url (str):
            The Google Cloud Storage signed URL used for source
            uploading, generated by calling
            [google.cloud.functions.v1.GenerateUploadUrl].

            The signature is validated on write methods (Create, Update)
            The signature is stripped from the Function object on read
            methods (Get, List)

            This field is a member of `oneof`_ ``source_code``.
        https_trigger (google.cloud.functions_v1.types.HttpsTrigger):
            An HTTPS endpoint type of source that can be
            triggered via URL.

            This field is a member of `oneof`_ ``trigger``.
        event_trigger (google.cloud.functions_v1.types.EventTrigger):
            A source that fires events in response to a
            condition in another service.

            This field is a member of `oneof`_ ``trigger``.
        status (google.cloud.functions_v1.types.CloudFunctionStatus):
            Output only. Status of the function
            deployment.
        entry_point (str):
            The name of the function (as defined in source code) that
            will be executed. Defaults to the resource name suffix, if
            not specified. For backward compatibility, if function with
            given name is not found, then the system will try to use
            function named "function". For Node.js this is name of a
            function exported by the module specified in
            ``source_location``.
        runtime (str):
            The runtime in which to run the function. Required when
            deploying a new function, optional when updating an existing
            function. For a complete list of possible choices, see the
            ```gcloud`` command
            reference <https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime>`__.
        timeout (google.protobuf.duration_pb2.Duration):
            The function execution timeout. Execution is
            considered failed and can be terminated if the
            function is not completed at the end of the
            timeout period. Defaults to 60 seconds.
        available_memory_mb (int):
            The amount of memory in MB available for a
            function. Defaults to 256MB.
        service_account_email (str):
            The email of the function's service account. If empty,
            defaults to ``{project_id}@appspot.gserviceaccount.com``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of a
            Cloud Function.
        version_id (int):
            Output only. The version identifier of the
            Cloud Function. Each deployment attempt results
            in a new version of a function being created.
        labels (Mapping[str, str]):
            Labels associated with this Cloud Function.
        environment_variables (Mapping[str, str]):
            Environment variables that shall be available
            during function execution.
        build_environment_variables (Mapping[str, str]):
            Build environment variables that shall be
            available during build time.
        network (str):
            The VPC Network that this cloud function can connect to. It
            can be either the fully-qualified URI, or the short name of
            the network resource. If the short network name is used, the
            network must belong to the same project. Otherwise, it must
            belong to a project within the same organization. The format
            of this field is either
            ``projects/{project}/global/networks/{network}`` or
            ``{network}``, where ``{project}`` is a project id where the
            network is defined, and ``{network}`` is the short name of
            the network.

            This field is mutually exclusive with ``vpc_connector`` and
            will be replaced by it.

            See `the VPC
            documentation <https://cloud.google.com/compute/docs/vpc>`__
            for more information on connecting Cloud projects.
        max_instances (int):
            The limit on the maximum number of function instances that
            may coexist at a given time.

            In some cases, such as rapid traffic surges, Cloud Functions
            may, for a short period of time, create more instances than
            the specified max instances limit. If your function cannot
            tolerate this temporary behavior, you may want to factor in
            a safety margin and set a lower max instances value than
            your function can tolerate.

            See the `Max
            Instances <https://cloud.google.com/functions/docs/max-instances>`__
            Guide for more details.
        min_instances (int):
            A lower bound for the number function
            instances that may coexist at a given time.
        vpc_connector (str):
            The VPC Network Connector that this cloud function can
            connect to. It can be either the fully-qualified URI, or the
            short name of the network connector resource. The format of
            this field is ``projects/*/locations/*/connectors/*``

            This field is mutually exclusive with ``network`` field and
            will eventually replace it.

            See `the VPC
            documentation <https://cloud.google.com/compute/docs/vpc>`__
            for more information on connecting Cloud projects.
        vpc_connector_egress_settings (google.cloud.functions_v1.types.CloudFunction.VpcConnectorEgressSettings):
            The egress settings for the connector,
            controlling what traffic is diverted through it.
        ingress_settings (google.cloud.functions_v1.types.CloudFunction.IngressSettings):
            The ingress settings for the function,
            controlling what traffic can reach it.
        kms_key_name (str):
            Resource name of a KMS crypto key (managed by the user) used
            to encrypt/decrypt function resources.

            It must match the pattern
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}``.

            If specified, you must also provide an artifact registry
            repository using the ``docker_repository`` field that was
            created with the same KMS crypto key.

            The following service accounts need to be granted the role
            'Cloud KMS CryptoKey Encrypter/Decrypter
            (roles/cloudkms.cryptoKeyEncrypterDecrypter)' on the
            Key/KeyRing/Project/Organization (least access preferred).

            1. Google Cloud Functions service account
               (service-{project_number}@gcf-admin-robot.iam.gserviceaccount.com)
               - Required to protect the function's image.
            2. Google Storage service account
               (service-{project_number}@gs-project-accounts.iam.gserviceaccount.com)
               - Required to protect the function's source code. If this
               service account does not exist, deploying a function
               without a KMS key or retrieving the service agent name
               provisions it. For more information, see
               https://cloud.google.com/storage/docs/projects#service-agents
               and
               https://cloud.google.com/storage/docs/getting-service-agent#gsutil.

            Google Cloud Functions delegates access to service agents to
            protect function resources in internal projects that are not
            accessible by the end user.
        build_worker_pool (str):
            Name of the Cloud Build Custom Worker Pool that should be
            used to build the function. The format of this field is
            ``projects/{project}/locations/{region}/workerPools/{workerPool}``
            where ``{project}`` and ``{region}`` are the project id and
            region respectively where the worker pool is defined and
            ``{workerPool}`` is the short name of the worker pool.

            If the project id is not the same as the function, then the
            Cloud Functions Service Agent
            (``service-<project_number>@gcf-admin-robot.iam.gserviceaccount.com``)
            must be granted the role Cloud Build Custom Workers Builder
            (``roles/cloudbuild.customworkers.builder``) in the project.
        build_id (str):
            Output only. The Cloud Build ID of the latest
            successful deployment of the function.
        build_name (str):
            Output only. The Cloud Build Name of the function
            deployment.
            ``projects/<project-number>/locations/<region>/builds/<build-id>``.
        secret_environment_variables (Sequence[google.cloud.functions_v1.types.SecretEnvVar]):
            Secret environment variables configuration.
        secret_volumes (Sequence[google.cloud.functions_v1.types.SecretVolume]):
            Secret volumes configuration.
        source_token (str):
            Input only. An identifier for Firebase
            function sources. Disclaimer: This field is only
            supported for Firebase function deployments.
        docker_repository (str):
            User managed repository created in Artifact Registry
            optionally with a customer managed encryption key. If
            specified, deployments will use Artifact Registry. If
            unspecified and the deployment is eligible to use Artifact
            Registry, GCF will create and use a repository named
            'gcf-artifacts' for every deployed region. This is the
            repository to which the function docker image will be pushed
            after it is built by Cloud Build.

            It must match the pattern
            ``projects/{project}/locations/{location}/repositories/{repository}``.

            Cross-project repositories are not supported. Cross-location
            repositories are not supported. Repository format must be
            'DOCKER'.
        docker_registry (google.cloud.functions_v1.types.CloudFunction.DockerRegistry):
            Docker Registry to use for this deployment.

            If ``docker_repository`` field is specified, this field will
            be automatically set as ``ARTIFACT_REGISTRY``. If
            unspecified, it currently defaults to
            ``CONTAINER_REGISTRY``. This field may be overridden by the
            backend for eligible deployments.
    """

    class VpcConnectorEgressSettings(proto.Enum):
        r"""Available egress settings.

        This controls what traffic is diverted through the VPC Access
        Connector resource. By default PRIVATE_RANGES_ONLY will be used.
        """
        VPC_CONNECTOR_EGRESS_SETTINGS_UNSPECIFIED = 0
        PRIVATE_RANGES_ONLY = 1
        ALL_TRAFFIC = 2

    class IngressSettings(proto.Enum):
        r"""Available ingress settings.

        This controls what traffic can reach the function.

        If unspecified, ALLOW_ALL will be used.
        """
        INGRESS_SETTINGS_UNSPECIFIED = 0
        ALLOW_ALL = 1
        ALLOW_INTERNAL_ONLY = 2
        ALLOW_INTERNAL_AND_GCLB = 3

    class DockerRegistry(proto.Enum):
        r"""Docker Registry to use for storing function Docker images."""
        DOCKER_REGISTRY_UNSPECIFIED = 0
        CONTAINER_REGISTRY = 1
        ARTIFACT_REGISTRY = 2

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    description = proto.Field(
        proto.STRING,
        number=2,
    )
    source_archive_url = proto.Field(
        proto.STRING,
        number=3,
        oneof="source_code",
    )
    source_repository = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="source_code",
        message="SourceRepository",
    )
    source_upload_url = proto.Field(
        proto.STRING,
        number=16,
        oneof="source_code",
    )
    https_trigger = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="trigger",
        message="HttpsTrigger",
    )
    event_trigger = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="trigger",
        message="EventTrigger",
    )
    status = proto.Field(
        proto.ENUM,
        number=7,
        enum="CloudFunctionStatus",
    )
    entry_point = proto.Field(
        proto.STRING,
        number=8,
    )
    runtime = proto.Field(
        proto.STRING,
        number=19,
    )
    timeout = proto.Field(
        proto.MESSAGE,
        number=9,
        message=duration_pb2.Duration,
    )
    available_memory_mb = proto.Field(
        proto.INT32,
        number=10,
    )
    service_account_email = proto.Field(
        proto.STRING,
        number=11,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    version_id = proto.Field(
        proto.INT64,
        number=14,
    )
    labels = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=15,
    )
    environment_variables = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=17,
    )
    build_environment_variables = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=28,
    )
    network = proto.Field(
        proto.STRING,
        number=18,
    )
    max_instances = proto.Field(
        proto.INT32,
        number=20,
    )
    min_instances = proto.Field(
        proto.INT32,
        number=32,
    )
    vpc_connector = proto.Field(
        proto.STRING,
        number=22,
    )
    vpc_connector_egress_settings = proto.Field(
        proto.ENUM,
        number=23,
        enum=VpcConnectorEgressSettings,
    )
    ingress_settings = proto.Field(
        proto.ENUM,
        number=24,
        enum=IngressSettings,
    )
    kms_key_name = proto.Field(
        proto.STRING,
        number=25,
    )
    build_worker_pool = proto.Field(
        proto.STRING,
        number=26,
    )
    build_id = proto.Field(
        proto.STRING,
        number=27,
    )
    build_name = proto.Field(
        proto.STRING,
        number=33,
    )
    secret_environment_variables = proto.RepeatedField(
        proto.MESSAGE,
        number=29,
        message="SecretEnvVar",
    )
    secret_volumes = proto.RepeatedField(
        proto.MESSAGE,
        number=30,
        message="SecretVolume",
    )
    source_token = proto.Field(
        proto.STRING,
        number=31,
    )
    docker_repository = proto.Field(
        proto.STRING,
        number=34,
    )
    docker_registry = proto.Field(
        proto.ENUM,
        number=35,
        enum=DockerRegistry,
    )


class SourceRepository(proto.Message):
    r"""Describes SourceRepository, used to represent parameters
    related to source repository where a function is hosted.

    Attributes:
        url (str):
            The URL pointing to the hosted repository where the function
            is defined. There are supported Cloud Source Repository URLs
            in the following formats:

            To refer to a specific commit:
            ``https://source.developers.google.com/projects/*/repos/*/revisions/*/paths/*``
            To refer to a moveable alias (branch):
            ``https://source.developers.google.com/projects/*/repos/*/moveable-aliases/*/paths/*``
            In particular, to refer to HEAD use ``master`` moveable
            alias. To refer to a specific fixed alias (tag):
            ``https://source.developers.google.com/projects/*/repos/*/fixed-aliases/*/paths/*``

            You may omit ``paths/*`` if you want to use the main
            directory.
        deployed_url (str):
            Output only. The URL pointing to the hosted
            repository where the function were defined at
            the time of deployment. It always points to a
            specific commit in the format described above.
    """

    url = proto.Field(
        proto.STRING,
        number=1,
    )
    deployed_url = proto.Field(
        proto.STRING,
        number=2,
    )


class HttpsTrigger(proto.Message):
    r"""Describes HttpsTrigger, could be used to connect web hooks to
    function.

    Attributes:
        url (str):
            Output only. The deployed url for the
            function.
        security_level (google.cloud.functions_v1.types.HttpsTrigger.SecurityLevel):
            The security level for the function.
    """

    class SecurityLevel(proto.Enum):
        r"""Available security level settings.

        This controls the methods to enforce security (HTTPS) on a URL.

        If unspecified, SECURE_OPTIONAL will be used.
        """
        SECURITY_LEVEL_UNSPECIFIED = 0
        SECURE_ALWAYS = 1
        SECURE_OPTIONAL = 2

    url = proto.Field(
        proto.STRING,
        number=1,
    )
    security_level = proto.Field(
        proto.ENUM,
        number=2,
        enum=SecurityLevel,
    )


class EventTrigger(proto.Message):
    r"""Describes EventTrigger, used to request events be sent from
    another service.

    Attributes:
        event_type (str):
            Required. The type of event to observe. For example:
            ``providers/cloud.storage/eventTypes/object.change`` and
            ``providers/cloud.pubsub/eventTypes/topic.publish``.

            Event types match pattern ``providers/*/eventTypes/*.*``.
            The pattern contains:

            1. namespace: For example, ``cloud.storage`` and
               ``google.firebase.analytics``.
            2. resource type: The type of resource on which event
               occurs. For example, the Google Cloud Storage API
               includes the type ``object``.
            3. action: The action that generates the event. For example,
               action for a Google Cloud Storage Object is 'change'.
               These parts are lower case.
        resource (str):
            Required. The resource(s) from which to observe events, for
            example, ``projects/_/buckets/myBucket``.

            Not all syntactically correct values are accepted by all
            services. For example:

            1. The authorization model must support it. Google Cloud
               Functions only allows EventTriggers to be deployed that
               observe resources in the same project as the
               ``CloudFunction``.
            2. The resource type must match the pattern expected for an
               ``event_type``. For example, an ``EventTrigger`` that has
               an ``event_type`` of "google.pubsub.topic.publish" should
               have a resource that matches Google Cloud Pub/Sub topics.

            Additionally, some services may support short names when
            creating an ``EventTrigger``. These will always be returned
            in the normalized "long" format.

            See each *service's* documentation for supported formats.
        service (str):
            The hostname of the service that should be observed.

            If no string is provided, the default service implementing
            the API will be used. For example,
            ``storage.googleapis.com`` is the default for all event
            types in the ``google.storage`` namespace.
        failure_policy (google.cloud.functions_v1.types.FailurePolicy):
            Specifies policy for failed executions.
    """

    event_type = proto.Field(
        proto.STRING,
        number=1,
    )
    resource = proto.Field(
        proto.STRING,
        number=2,
    )
    service = proto.Field(
        proto.STRING,
        number=3,
    )
    failure_policy = proto.Field(
        proto.MESSAGE,
        number=5,
        message="FailurePolicy",
    )


class FailurePolicy(proto.Message):
    r"""Describes the policy in case of function's execution failure.
    If empty, then defaults to ignoring failures (i.e. not retrying
    them).


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        retry (google.cloud.functions_v1.types.FailurePolicy.Retry):
            If specified, then the function will be
            retried in case of a failure.

            This field is a member of `oneof`_ ``action``.
    """

    class Retry(proto.Message):
        r"""Describes the retry policy in case of function's execution
        failure. A function execution will be retried on any failure. A
        failed execution will be retried up to 7 days with an
        exponential backoff (capped at 10 seconds).
        Retried execution is charged as any other execution.

        """

    retry = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="action",
        message=Retry,
    )


class SecretEnvVar(proto.Message):
    r"""Configuration for a secret environment variable. It has the
    information necessary to fetch the secret value from secret
    manager and expose it as an environment variable.

    Attributes:
        key (str):
            Name of the environment variable.
        project_id (str):
            Project identifier (preferrably project
            number but can also be the project ID) of the
            project that contains the secret. If not set, it
            will be populated with the function's project
            assuming that the secret exists in the same
            project as of the function.
        secret (str):
            Name of the secret in secret manager (not the
            full resource name).
        version (str):
            Version of the secret (version number or the
            string 'latest'). It is recommended to use a
            numeric version for secret environment variables
            as any updates to the secret value is not
            reflected until new instances start.
    """

    key = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id = proto.Field(
        proto.STRING,
        number=2,
    )
    secret = proto.Field(
        proto.STRING,
        number=3,
    )
    version = proto.Field(
        proto.STRING,
        number=4,
    )


class SecretVolume(proto.Message):
    r"""Configuration for a secret volume. It has the information
    necessary to fetch the secret value from secret manager and make
    it available as files mounted at the requested paths within the
    application container. Secret value is not a part of the
    configuration. Every filesystem read operation performs a lookup
    in secret manager to retrieve the secret value.

    Attributes:
        mount_path (str):
            The path within the container to mount the secret volume.
            For example, setting the mount_path as ``/etc/secrets``
            would mount the secret value files under the
            ``/etc/secrets`` directory. This directory will also be
            completely shadowed and unavailable to mount any other
            secrets.

            Recommended mount paths: /etc/secrets Restricted mount
            paths: /cloudsql, /dev/log, /pod, /proc, /var/log
        project_id (str):
            Project identifier (preferrably project
            number but can also be the project ID) of the
            project that contains the secret. If not set, it
            will be populated with the function's project
            assuming that the secret exists in the same
            project as of the function.
        secret (str):
            Name of the secret in secret manager (not the
            full resource name).
        versions (Sequence[google.cloud.functions_v1.types.SecretVolume.SecretVersion]):
            List of secret versions to mount for this secret. If empty,
            the ``latest`` version of the secret will be made available
            in a file named after the secret under the mount point.
    """

    class SecretVersion(proto.Message):
        r"""Configuration for a single version.

        Attributes:
            version (str):
                Version of the secret (version number or the string
                'latest'). It is preferrable to use ``latest`` version with
                secret volumes as secret value changes are reflected
                immediately.
            path (str):
                Relative path of the file under the mount path where the
                secret value for this version will be fetched and made
                available. For example, setting the mount_path as
                '/etc/secrets' and path as ``/secret_foo`` would mount the
                secret value file at ``/etc/secrets/secret_foo``.
        """

        version = proto.Field(
            proto.STRING,
            number=1,
        )
        path = proto.Field(
            proto.STRING,
            number=2,
        )

    mount_path = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id = proto.Field(
        proto.STRING,
        number=2,
    )
    secret = proto.Field(
        proto.STRING,
        number=3,
    )
    versions = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=SecretVersion,
    )


class CreateFunctionRequest(proto.Message):
    r"""Request for the ``CreateFunction`` method.

    Attributes:
        location (str):
            Required. The project and location in which the function
            should be created, specified in the format
            ``projects/*/locations/*``
        function (google.cloud.functions_v1.types.CloudFunction):
            Required. Function to be created.
    """

    location = proto.Field(
        proto.STRING,
        number=1,
    )
    function = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CloudFunction",
    )


class UpdateFunctionRequest(proto.Message):
    r"""Request for the ``UpdateFunction`` method.

    Attributes:
        function (google.cloud.functions_v1.types.CloudFunction):
            Required. New version of the function.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields in ``CloudFunction`` that have
            to be updated.
    """

    function = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CloudFunction",
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetFunctionRequest(proto.Message):
    r"""Request for the ``GetFunction`` method.

    Attributes:
        name (str):
            Required. The name of the function which
            details should be obtained.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class ListFunctionsRequest(proto.Message):
    r"""Request for the ``ListFunctions`` method.

    Attributes:
        parent (str):
            The project and location from which the function should be
            listed, specified in the format ``projects/*/locations/*``
            If you want to list functions in all locations, use "-" in
            place of a location. When listing functions in all
            locations, if one or more location(s) are unreachable, the
            response will contain functions from all reachable locations
            along with the names of any unreachable locations.
        page_size (int):
            Maximum number of functions to return per
            call.
        page_token (str):
            The value returned by the last ``ListFunctionsResponse``;
            indicates that this is a continuation of a prior
            ``ListFunctions`` call, and that the system should return
            the next page of data.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token = proto.Field(
        proto.STRING,
        number=3,
    )


class ListFunctionsResponse(proto.Message):
    r"""Response for the ``ListFunctions`` method.

    Attributes:
        functions (Sequence[google.cloud.functions_v1.types.CloudFunction]):
            The functions that match the request.
        next_page_token (str):
            If not empty, indicates that there may be more functions
            that match the request; this value should be passed in a new
            [google.cloud.functions.v1.ListFunctionsRequest][google.cloud.functions.v1.ListFunctionsRequest]
            to get more functions.
        unreachable (Sequence[str]):
            Locations that could not be reached. The
            response does not include any functions from
            these locations.
    """

    @property
    def raw_page(self):
        return self

    functions = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CloudFunction",
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DeleteFunctionRequest(proto.Message):
    r"""Request for the ``DeleteFunction`` method.

    Attributes:
        name (str):
            Required. The name of the function which
            should be deleted.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class CallFunctionRequest(proto.Message):
    r"""Request for the ``CallFunction`` method.

    Attributes:
        name (str):
            Required. The name of the function to be
            called.
        data (str):
            Required. Input to be passed to the function.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    data = proto.Field(
        proto.STRING,
        number=2,
    )


class CallFunctionResponse(proto.Message):
    r"""Response of ``CallFunction`` method.

    Attributes:
        execution_id (str):
            Execution id of function invocation.
        result (str):
            Result populated for successful execution of
            synchronous function. Will not be populated if
            function does not return a result through
            context.
        error (str):
            Either system or user-function generated
            error. Set if execution was not successful.
    """

    execution_id = proto.Field(
        proto.STRING,
        number=1,
    )
    result = proto.Field(
        proto.STRING,
        number=2,
    )
    error = proto.Field(
        proto.STRING,
        number=3,
    )


class GenerateUploadUrlRequest(proto.Message):
    r"""Request of ``GenerateSourceUploadUrl`` method.

    Attributes:
        parent (str):
            The project and location in which the Google Cloud Storage
            signed URL should be generated, specified in the format
            ``projects/*/locations/*``.
        kms_key_name (str):
            Resource name of a KMS crypto key (managed by the user) used
            to encrypt/decrypt function source code objects in staging
            Cloud Storage buckets. When you generate an upload url and
            upload your source code, it gets copied to a staging Cloud
            Storage bucket in an internal regional project. The source
            code is then copied to a versioned directory in the sources
            bucket in the consumer project during the function
            deployment.

            It must match the pattern
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}``.

            The Google Cloud Functions service account
            (service-{project_number}@gcf-admin-robot.iam.gserviceaccount.com)
            must be granted the role 'Cloud KMS CryptoKey
            Encrypter/Decrypter
            (roles/cloudkms.cryptoKeyEncrypterDecrypter)' on the
            Key/KeyRing/Project/Organization (least access preferred).
            GCF will delegate access to the Google Storage service
            account in the internal project.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    kms_key_name = proto.Field(
        proto.STRING,
        number=2,
    )


class GenerateUploadUrlResponse(proto.Message):
    r"""Response of ``GenerateSourceUploadUrl`` method.

    Attributes:
        upload_url (str):
            The generated Google Cloud Storage signed URL
            that should be used for a function source code
            upload. The uploaded file should be a zip
            archive which contains a function.
    """

    upload_url = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateDownloadUrlRequest(proto.Message):
    r"""Request of ``GenerateDownloadUrl`` method.

    Attributes:
        name (str):
            The name of function for which source code
            Google Cloud Storage signed URL should be
            generated.
        version_id (int):
            The optional version of function. If not set,
            default, current version is used.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    version_id = proto.Field(
        proto.UINT64,
        number=2,
    )


class GenerateDownloadUrlResponse(proto.Message):
    r"""Response of ``GenerateDownloadUrl`` method.

    Attributes:
        download_url (str):
            The generated Google Cloud Storage signed URL
            that should be used for function source code
            download.
    """

    download_url = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
