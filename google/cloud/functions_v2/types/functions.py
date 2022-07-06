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
from google.protobuf import any_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.functions.v2",
    manifest={
        "Environment",
        "Function",
        "StateMessage",
        "StorageSource",
        "RepoSource",
        "Source",
        "SourceProvenance",
        "BuildConfig",
        "ServiceConfig",
        "SecretEnvVar",
        "SecretVolume",
        "EventTrigger",
        "EventFilter",
        "GetFunctionRequest",
        "ListFunctionsRequest",
        "ListFunctionsResponse",
        "CreateFunctionRequest",
        "UpdateFunctionRequest",
        "DeleteFunctionRequest",
        "GenerateUploadUrlRequest",
        "GenerateUploadUrlResponse",
        "GenerateDownloadUrlRequest",
        "GenerateDownloadUrlResponse",
        "ListRuntimesRequest",
        "ListRuntimesResponse",
        "OperationMetadata",
        "Stage",
    },
)


class Environment(proto.Enum):
    r"""The environment the function is hosted on."""
    ENVIRONMENT_UNSPECIFIED = 0
    GEN_1 = 1
    GEN_2 = 2


class Function(proto.Message):
    r"""Describes a Cloud Function that contains user computation
    executed in response to an event. It encapsulates function and
    trigger configurations.

    Attributes:
        name (str):
            A user-defined name of the function. Function names must be
            unique globally and match pattern
            ``projects/*/locations/*/functions/*``
        environment (google.cloud.functions_v2.types.Environment):
            Describe whether the function is gen1 or
            gen2.
        description (str):
            User-provided description of a function.
        build_config (google.cloud.functions_v2.types.BuildConfig):
            Describes the Build step of the function that
            builds a container from the given source.
        service_config (google.cloud.functions_v2.types.ServiceConfig):
            Describes the Service being deployed.
            Currently deploys services to Cloud Run (fully
            managed).
        event_trigger (google.cloud.functions_v2.types.EventTrigger):
            An Eventarc trigger managed by Google Cloud
            Functions that fires events in response to a
            condition in another service.
        state (google.cloud.functions_v2.types.Function.State):
            Output only. State of the function.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of a
            Cloud Function.
        labels (Mapping[str, str]):
            Labels associated with this Cloud Function.
        state_messages (Sequence[google.cloud.functions_v2.types.StateMessage]):
            Output only. State Messages for this Cloud
            Function.
    """

    class State(proto.Enum):
        r"""Describes the current state of the function."""
        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        FAILED = 2
        DEPLOYING = 3
        DELETING = 4
        UNKNOWN = 5

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    environment = proto.Field(
        proto.ENUM,
        number=10,
        enum="Environment",
    )
    description = proto.Field(
        proto.STRING,
        number=2,
    )
    build_config = proto.Field(
        proto.MESSAGE,
        number=3,
        message="BuildConfig",
    )
    service_config = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ServiceConfig",
    )
    event_trigger = proto.Field(
        proto.MESSAGE,
        number=5,
        message="EventTrigger",
    )
    state = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    labels = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    state_messages = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="StateMessage",
    )


class StateMessage(proto.Message):
    r"""Informational messages about the state of the Cloud Function
    or Operation.

    Attributes:
        severity (google.cloud.functions_v2.types.StateMessage.Severity):
            Severity of the state message.
        type_ (str):
            One-word CamelCase type of the state message.
        message (str):
            The message.
    """

    class Severity(proto.Enum):
        r"""Severity of the state message."""
        SEVERITY_UNSPECIFIED = 0
        ERROR = 1
        WARNING = 2
        INFO = 3

    severity = proto.Field(
        proto.ENUM,
        number=1,
        enum=Severity,
    )
    type_ = proto.Field(
        proto.STRING,
        number=2,
    )
    message = proto.Field(
        proto.STRING,
        number=3,
    )


class StorageSource(proto.Message):
    r"""Location of the source in an archive file in Google Cloud
    Storage.

    Attributes:
        bucket (str):
            Google Cloud Storage bucket containing the source (see
            `Bucket Name
            Requirements <https://cloud.google.com/storage/docs/bucket-naming#requirements>`__).
        object_ (str):
            Google Cloud Storage object containing the source.

            This object must be a gzipped archive file (``.tar.gz``)
            containing source to build.
        generation (int):
            Google Cloud Storage generation for the
            object. If the generation is omitted, the latest
            generation will be used.
    """

    bucket = proto.Field(
        proto.STRING,
        number=1,
    )
    object_ = proto.Field(
        proto.STRING,
        number=2,
    )
    generation = proto.Field(
        proto.INT64,
        number=3,
    )


class RepoSource(proto.Message):
    r"""Location of the source in a Google Cloud Source Repository.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        branch_name (str):
            Regex matching branches to build.
            The syntax of the regular expressions accepted
            is the syntax accepted by RE2 and described at
            https://github.com/google/re2/wiki/Syntax

            This field is a member of `oneof`_ ``revision``.
        tag_name (str):
            Regex matching tags to build.
            The syntax of the regular expressions accepted
            is the syntax accepted by RE2 and described at
            https://github.com/google/re2/wiki/Syntax

            This field is a member of `oneof`_ ``revision``.
        commit_sha (str):
            Explicit commit SHA to build.

            This field is a member of `oneof`_ ``revision``.
        project_id (str):
            ID of the project that owns the Cloud Source
            Repository. If omitted, the project ID
            requesting the build is assumed.
        repo_name (str):
            Name of the Cloud Source Repository.
        dir_ (str):
            Directory, relative to the source root, in which to run the
            build.

            This must be a relative path. If a step's ``dir`` is
            specified and is an absolute path, this value is ignored for
            that step's execution. eg. helloworld (no leading slash
            allowed)
        invert_regex (bool):
            Only trigger a build if the revision regex
            does NOT match the revision regex.
    """

    branch_name = proto.Field(
        proto.STRING,
        number=3,
        oneof="revision",
    )
    tag_name = proto.Field(
        proto.STRING,
        number=4,
        oneof="revision",
    )
    commit_sha = proto.Field(
        proto.STRING,
        number=5,
        oneof="revision",
    )
    project_id = proto.Field(
        proto.STRING,
        number=1,
    )
    repo_name = proto.Field(
        proto.STRING,
        number=2,
    )
    dir_ = proto.Field(
        proto.STRING,
        number=6,
    )
    invert_regex = proto.Field(
        proto.BOOL,
        number=7,
    )


class Source(proto.Message):
    r"""The location of the function source code.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        storage_source (google.cloud.functions_v2.types.StorageSource):
            If provided, get the source from this
            location in Google Cloud Storage.

            This field is a member of `oneof`_ ``source``.
        repo_source (google.cloud.functions_v2.types.RepoSource):
            If provided, get the source from this
            location in a Cloud Source Repository.

            This field is a member of `oneof`_ ``source``.
    """

    storage_source = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source",
        message="StorageSource",
    )
    repo_source = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="RepoSource",
    )


class SourceProvenance(proto.Message):
    r"""Provenance of the source. Ways to find the original source,
    or verify that some source was used for this build.

    Attributes:
        resolved_storage_source (google.cloud.functions_v2.types.StorageSource):
            A copy of the build's ``source.storage_source``, if exists,
            with any generations resolved.
        resolved_repo_source (google.cloud.functions_v2.types.RepoSource):
            A copy of the build's ``source.repo_source``, if exists,
            with any revisions resolved.
    """

    resolved_storage_source = proto.Field(
        proto.MESSAGE,
        number=1,
        message="StorageSource",
    )
    resolved_repo_source = proto.Field(
        proto.MESSAGE,
        number=2,
        message="RepoSource",
    )


class BuildConfig(proto.Message):
    r"""Describes the Build step of the function that builds a
    container from the given source.

    Attributes:
        build (str):
            Output only. The Cloud Build name of the
            latest successful deployment of the function.
        runtime (str):
            The runtime in which to run the function. Required when
            deploying a new function, optional when updating an existing
            function. For a complete list of possible choices, see the
            ```gcloud`` command
            reference <https://cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime>`__.
        entry_point (str):
            The name of the function (as defined in source code) that
            will be executed. Defaults to the resource name suffix, if
            not specified. For backward compatibility, if function with
            given name is not found, then the system will try to use
            function named "function". For Node.js this is name of a
            function exported by the module specified in
            ``source_location``.
        source (google.cloud.functions_v2.types.Source):
            The location of the function source code.
        source_provenance (google.cloud.functions_v2.types.SourceProvenance):
            Output only. A permanent fixed identifier for
            source.
        worker_pool (str):
            Name of the Cloud Build Custom Worker Pool that should be
            used to build the function. The format of this field is
            ``projects/{project}/locations/{region}/workerPools/{workerPool}``
            where {project} and {region} are the project id and region
            respectively where the worker pool is defined and
            {workerPool} is the short name of the worker pool.

            If the project id is not the same as the function, then the
            Cloud Functions Service Agent
            (service-<project_number>@gcf-admin-robot.iam.gserviceaccount.com)
            must be granted the role Cloud Build Custom Workers Builder
            (roles/cloudbuild.customworkers.builder) in the project.
        environment_variables (Mapping[str, str]):
            User-provided build-time environment
            variables for the function
        docker_repository (str):
            Optional. User managed repository created in Artifact
            Registry optionally with a customer managed encryption key.
            This is the repository to which the function docker image
            will be pushed after it is built by Cloud Build. If
            unspecified, GCF will create and use a repository named
            'gcf-artifacts' for every deployed region.

            It must match the pattern
            ``projects/{project}/locations/{location}/repositories/{repository}``.

            Cross-project repositories are not supported. Cross-location
            repositories are not supported. Repository format must be
            'DOCKER'.
    """

    build = proto.Field(
        proto.STRING,
        number=1,
    )
    runtime = proto.Field(
        proto.STRING,
        number=2,
    )
    entry_point = proto.Field(
        proto.STRING,
        number=3,
    )
    source = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Source",
    )
    source_provenance = proto.Field(
        proto.MESSAGE,
        number=8,
        message="SourceProvenance",
    )
    worker_pool = proto.Field(
        proto.STRING,
        number=5,
    )
    environment_variables = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    docker_repository = proto.Field(
        proto.STRING,
        number=7,
    )


class ServiceConfig(proto.Message):
    r"""Describes the Service being deployed.
    Currently Supported : Cloud Run (fully managed).

    Attributes:
        service (str):
            Output only. Name of the service associated with a Function.
            The format of this field is
            ``projects/{project}/locations/{region}/services/{service}``
        timeout_seconds (int):
            The function execution timeout. Execution is
            considered failed and can be terminated if the
            function is not completed at the end of the
            timeout period. Defaults to 60 seconds.
        available_memory (str):
            The amount of memory available for a
            function. Defaults to 256M. Supported units are
            k, M, G, Mi, Gi. If no unit is supplied the
            value is interpreted as bytes.
            See
            https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/api/resource/quantity.go
            a full description.
        environment_variables (Mapping[str, str]):
            Environment variables that shall be available
            during function execution.
        max_instance_count (int):
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
        min_instance_count (int):
            The limit on the minimum number of function
            instances that may coexist at a given time.

            Function instances are kept in idle state for a
            short period after they finished executing the
            request to reduce cold start time for subsequent
            requests. Setting a minimum instance count will
            ensure that the given number of instances are
            kept running in idle state always. This can help
            with cold start times when jump in incoming
            request count occurs after the idle instance
            would have been stopped in the default case.
        vpc_connector (str):
            The Serverless VPC Access connector that this cloud function
            can connect to. The format of this field is
            ``projects/*/locations/*/connectors/*``.
        vpc_connector_egress_settings (google.cloud.functions_v2.types.ServiceConfig.VpcConnectorEgressSettings):
            The egress settings for the connector,
            controlling what traffic is diverted through it.
        ingress_settings (google.cloud.functions_v2.types.ServiceConfig.IngressSettings):
            The ingress settings for the function,
            controlling what traffic can reach it.
        uri (str):
            Output only. URI of the Service deployed.
        service_account_email (str):
            The email of the service's service account. If empty,
            defaults to
            ``{project_number}-compute@developer.gserviceaccount.com``.
        all_traffic_on_latest_revision (bool):
            Whether 100% of traffic is routed to the
            latest revision. On CreateFunction and
            UpdateFunction, when set to true, the revision
            being deployed will serve 100% of traffic,
            ignoring any traffic split settings, if any. On
            GetFunction, true will be returned if the latest
            revision is serving 100% of traffic.
        secret_environment_variables (Sequence[google.cloud.functions_v2.types.SecretEnvVar]):
            Secret environment variables configuration.
        secret_volumes (Sequence[google.cloud.functions_v2.types.SecretVolume]):
            Secret volumes configuration.
        revision (str):
            Output only. The name of service revision.
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

    service = proto.Field(
        proto.STRING,
        number=1,
    )
    timeout_seconds = proto.Field(
        proto.INT32,
        number=2,
    )
    available_memory = proto.Field(
        proto.STRING,
        number=13,
    )
    environment_variables = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    max_instance_count = proto.Field(
        proto.INT32,
        number=5,
    )
    min_instance_count = proto.Field(
        proto.INT32,
        number=12,
    )
    vpc_connector = proto.Field(
        proto.STRING,
        number=6,
    )
    vpc_connector_egress_settings = proto.Field(
        proto.ENUM,
        number=7,
        enum=VpcConnectorEgressSettings,
    )
    ingress_settings = proto.Field(
        proto.ENUM,
        number=8,
        enum=IngressSettings,
    )
    uri = proto.Field(
        proto.STRING,
        number=9,
    )
    service_account_email = proto.Field(
        proto.STRING,
        number=10,
    )
    all_traffic_on_latest_revision = proto.Field(
        proto.BOOL,
        number=16,
    )
    secret_environment_variables = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message="SecretEnvVar",
    )
    secret_volumes = proto.RepeatedField(
        proto.MESSAGE,
        number=19,
        message="SecretVolume",
    )
    revision = proto.Field(
        proto.STRING,
        number=18,
    )


class SecretEnvVar(proto.Message):
    r"""Configuration for a secret environment variable. It has the
    information necessary to fetch the secret value from secret
    manager and expose it as an environment variable.

    Attributes:
        key (str):
            Name of the environment variable.
        project_id (str):
            Project identifier (preferably project number
            but can also be the project ID) of the project
            that contains the secret. If not set, it is
            assumed that the secret is in the same project
            as the function.
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
    application container.

    Attributes:
        mount_path (str):
            The path within the container to mount the secret volume.
            For example, setting the mount_path as ``/etc/secrets``
            would mount the secret value files under the
            ``/etc/secrets`` directory. This directory will also be
            completely shadowed and unavailable to mount any other
            secrets. Recommended mount path: /etc/secrets
        project_id (str):
            Project identifier (preferably project number
            but can also be the project ID) of the project
            that contains the secret. If not set, it is
            assumed that the secret is in the same project
            as the function.
        secret (str):
            Name of the secret in secret manager (not the
            full resource name).
        versions (Sequence[google.cloud.functions_v2.types.SecretVolume.SecretVersion]):
            List of secret versions to mount for this secret. If empty,
            the ``latest`` version of the secret will be made available
            in a file named after the secret under the mount point.
    """

    class SecretVersion(proto.Message):
        r"""Configuration for a single version.

        Attributes:
            version (str):
                Version of the secret (version number or the string
                'latest'). It is preferable to use ``latest`` version with
                secret volumes as secret value changes are reflected
                immediately.
            path (str):
                Relative path of the file under the mount path where the
                secret value for this version will be fetched and made
                available. For example, setting the mount_path as
                '/etc/secrets' and path as ``secret_foo`` would mount the
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


class EventTrigger(proto.Message):
    r"""Describes EventTrigger, used to request events to be sent
    from another service.

    Attributes:
        trigger (str):
            Output only. The resource name of the Eventarc trigger. The
            format of this field is
            ``projects/{project}/locations/{region}/triggers/{trigger}``.
        trigger_region (str):
            The region that the trigger will be in. The
            trigger will only receive events originating in
            this region. It can be the same region as the
            function, a different region or multi-region, or
            the global region. If not provided, defaults to
            the same region as the function.
        event_type (str):
            Required. The type of event to observe. For example:
            ``google.cloud.audit.log.v1.written`` or
            ``google.cloud.pubsub.topic.v1.messagePublished``.
        event_filters (Sequence[google.cloud.functions_v2.types.EventFilter]):
            Criteria used to filter events.
        pubsub_topic (str):
            Optional. The name of a Pub/Sub topic in the same project
            that will be used as the transport topic for the event
            delivery. Format: ``projects/{project}/topics/{topic}``.

            This is only valid for events of type
            ``google.cloud.pubsub.topic.v1.messagePublished``. The topic
            provided here will not be deleted at function deletion.
        service_account_email (str):
            Optional. The email of the trigger's service account. The
            service account must have permission to invoke Cloud Run
            services, the permission is ``run.routes.invoke``. If empty,
            defaults to the Compute Engine default service account:
            ``{project_number}-compute@developer.gserviceaccount.com``.
        retry_policy (google.cloud.functions_v2.types.EventTrigger.RetryPolicy):
            Optional. If unset, then defaults to ignoring
            failures (i.e. not retrying them).
        channel (str):
            Optional. The name of the channel associated with the
            trigger in
            ``projects/{project}/locations/{location}/channels/{channel}``
            format. You must provide a channel to receive events from
            Eventarc SaaS partners.
    """

    class RetryPolicy(proto.Enum):
        r"""Describes the retry policy in case of function's execution
        failure. Retried execution is charged as any other execution.
        """
        RETRY_POLICY_UNSPECIFIED = 0
        RETRY_POLICY_DO_NOT_RETRY = 1
        RETRY_POLICY_RETRY = 2

    trigger = proto.Field(
        proto.STRING,
        number=1,
    )
    trigger_region = proto.Field(
        proto.STRING,
        number=2,
    )
    event_type = proto.Field(
        proto.STRING,
        number=3,
    )
    event_filters = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="EventFilter",
    )
    pubsub_topic = proto.Field(
        proto.STRING,
        number=5,
    )
    service_account_email = proto.Field(
        proto.STRING,
        number=6,
    )
    retry_policy = proto.Field(
        proto.ENUM,
        number=7,
        enum=RetryPolicy,
    )
    channel = proto.Field(
        proto.STRING,
        number=8,
    )


class EventFilter(proto.Message):
    r"""Filters events based on exact matches on the CloudEvents
    attributes.

    Attributes:
        attribute (str):
            Required. The name of a CloudEvents
            attribute.
        value (str):
            Required. The value for the attribute.
        operator (str):
            Optional. The operator used for matching the events with the
            value of the filter. If not specified, only events that have
            an exact key-value pair specified in the filter are matched.
            The only allowed value is ``match-path-pattern``.
    """

    attribute = proto.Field(
        proto.STRING,
        number=1,
    )
    value = proto.Field(
        proto.STRING,
        number=2,
    )
    operator = proto.Field(
        proto.STRING,
        number=3,
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
            Required. The project and location from which the function
            should be listed, specified in the format
            ``projects/*/locations/*`` If you want to list functions in
            all locations, use "-" in place of a location. When listing
            functions in all locations, if one or more location(s) are
            unreachable, the response will contain functions from all
            reachable locations along with the names of any unreachable
            locations.
        page_size (int):
            Maximum number of functions to return per
            call.
        page_token (str):
            The value returned by the last ``ListFunctionsResponse``;
            indicates that this is a continuation of a prior
            ``ListFunctions`` call, and that the system should return
            the next page of data.
        filter (str):
            The filter for Functions that match the
            filter expression, following the syntax outlined
            in https://google.aip.dev/160.
        order_by (str):
            The sorting order of the resources returned.
            Value should be a comma separated list of
            fields. The default sorting oder is ascending.
            See https://google.aip.dev/132#ordering.
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
    filter = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by = proto.Field(
        proto.STRING,
        number=5,
    )


class ListFunctionsResponse(proto.Message):
    r"""Response for the ``ListFunctions`` method.

    Attributes:
        functions (Sequence[google.cloud.functions_v2.types.Function]):
            The functions that match the request.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
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
        message="Function",
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateFunctionRequest(proto.Message):
    r"""Request for the ``CreateFunction`` method.

    Attributes:
        parent (str):
            Required. The project and location in which the function
            should be created, specified in the format
            ``projects/*/locations/*``
        function (google.cloud.functions_v2.types.Function):
            Required. Function to be created.
        function_id (str):
            The ID to use for the function, which will become the final
            component of the function's resource name.

            This value should be 4-63 characters, and valid characters
            are /[a-z][0-9]-/.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    function = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Function",
    )
    function_id = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateFunctionRequest(proto.Message):
    r"""Request for the ``UpdateFunction`` method.

    Attributes:
        function (google.cloud.functions_v2.types.Function):
            Required. New version of the function.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
            If no field mask is provided, all provided
            fields in the request will be updated.
    """

    function = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Function",
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
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


class GenerateUploadUrlRequest(proto.Message):
    r"""Request of ``GenerateSourceUploadUrl`` method.

    Attributes:
        parent (str):
            Required. The project and location in which the Google Cloud
            Storage signed URL should be generated, specified in the
            format ``projects/*/locations/*``.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateUploadUrlResponse(proto.Message):
    r"""Response of ``GenerateSourceUploadUrl`` method.

    Attributes:
        upload_url (str):
            The generated Google Cloud Storage signed URL
            that should be used for a function source code
            upload. The uploaded file should be a zip
            archive which contains a function.
        storage_source (google.cloud.functions_v2.types.StorageSource):
            The location of the source code in the upload bucket.

            Once the archive is uploaded using the ``upload_url`` use
            this field to set the
            ``function.build_config.source.storage_source`` during
            CreateFunction and UpdateFunction.

            Generation defaults to 0, as Cloud Storage provides a new
            generation only upon uploading a new object or version of an
            object.
    """

    upload_url = proto.Field(
        proto.STRING,
        number=1,
    )
    storage_source = proto.Field(
        proto.MESSAGE,
        number=2,
        message="StorageSource",
    )


class GenerateDownloadUrlRequest(proto.Message):
    r"""Request of ``GenerateDownloadUrl`` method.

    Attributes:
        name (str):
            Required. The name of function for which
            source code Google Cloud Storage signed URL
            should be generated.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
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


class ListRuntimesRequest(proto.Message):
    r"""Request for the ``ListRuntimes`` method.

    Attributes:
        parent (str):
            Required. The project and location from which the runtimes
            should be listed, specified in the format
            ``projects/*/locations/*``
        filter (str):
            The filter for Runtimes that match the filter
            expression, following the syntax outlined in
            https://google.aip.dev/160.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    filter = proto.Field(
        proto.STRING,
        number=2,
    )


class ListRuntimesResponse(proto.Message):
    r"""Response for the ``ListRuntimes`` method.

    Attributes:
        runtimes (Sequence[google.cloud.functions_v2.types.ListRuntimesResponse.Runtime]):
            The runtimes that match the request.
    """

    class RuntimeStage(proto.Enum):
        r"""The various stages that a runtime can be in."""
        RUNTIME_STAGE_UNSPECIFIED = 0
        DEVELOPMENT = 1
        ALPHA = 2
        BETA = 3
        GA = 4
        DEPRECATED = 5
        DECOMMISSIONED = 6

    class Runtime(proto.Message):
        r"""Describes a runtime and any special information (e.g.,
        deprecation status) related to it.

        Attributes:
            name (str):
                The name of the runtime, e.g., 'go113',
                'nodejs12', etc.
            display_name (str):
                The user facing name, eg 'Go 1.13', 'Node.js
                12', etc.
            stage (google.cloud.functions_v2.types.ListRuntimesResponse.RuntimeStage):
                The stage of life this runtime is in, e.g.,
                BETA, GA, etc.
            warnings (Sequence[str]):
                Warning messages, e.g., a deprecation
                warning.
            environment (google.cloud.functions_v2.types.Environment):
                The environment for the runtime.
        """

        name = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name = proto.Field(
            proto.STRING,
            number=5,
        )
        stage = proto.Field(
            proto.ENUM,
            number=2,
            enum="ListRuntimesResponse.RuntimeStage",
        )
        warnings = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        environment = proto.Field(
            proto.ENUM,
            number=4,
            enum="Environment",
        )

    runtimes = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Runtime,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation finished running.
        target (str):
            Server-defined resource path for the target
            of the operation.
        verb (str):
            Name of the verb executed by the operation.
        status_detail (str):
            Human-readable status of the operation, if
            any.
        cancel_requested (bool):
            Identifies whether the user has requested cancellation of
            the operation. Operations that have successfully been
            cancelled have [Operation.error][] value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            API version used to start the operation.
        request_resource (google.protobuf.any_pb2.Any):
            The original request that started the
            operation.
        stages (Sequence[google.cloud.functions_v2.types.Stage]):
            Mechanism for reporting in-progress stages
    """

    create_time = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target = proto.Field(
        proto.STRING,
        number=3,
    )
    verb = proto.Field(
        proto.STRING,
        number=4,
    )
    status_detail = proto.Field(
        proto.STRING,
        number=5,
    )
    cancel_requested = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version = proto.Field(
        proto.STRING,
        number=7,
    )
    request_resource = proto.Field(
        proto.MESSAGE,
        number=8,
        message=any_pb2.Any,
    )
    stages = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="Stage",
    )


class Stage(proto.Message):
    r"""Each Stage of the deployment process

    Attributes:
        name (google.cloud.functions_v2.types.Stage.Name):
            Name of the Stage. This will be unique for
            each Stage.
        message (str):
            Message describing the Stage
        state (google.cloud.functions_v2.types.Stage.State):
            Current state of the Stage
        resource (str):
            Resource of the Stage
        resource_uri (str):
            Link to the current Stage resource
        state_messages (Sequence[google.cloud.functions_v2.types.StateMessage]):
            State messages from the current Stage.
    """

    class Name(proto.Enum):
        r"""Possible names for a Stage"""
        NAME_UNSPECIFIED = 0
        ARTIFACT_REGISTRY = 1
        BUILD = 2
        SERVICE = 3
        TRIGGER = 4
        SERVICE_ROLLBACK = 5
        TRIGGER_ROLLBACK = 6

    class State(proto.Enum):
        r"""Possible states for a Stage"""
        STATE_UNSPECIFIED = 0
        NOT_STARTED = 1
        IN_PROGRESS = 2
        COMPLETE = 3

    name = proto.Field(
        proto.ENUM,
        number=1,
        enum=Name,
    )
    message = proto.Field(
        proto.STRING,
        number=2,
    )
    state = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    resource = proto.Field(
        proto.STRING,
        number=4,
    )
    resource_uri = proto.Field(
        proto.STRING,
        number=5,
    )
    state_messages = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="StateMessage",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
