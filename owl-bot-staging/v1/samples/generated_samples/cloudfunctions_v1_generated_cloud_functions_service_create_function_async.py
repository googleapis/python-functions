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
# Generated code. DO NOT EDIT!
#
# Snippet for CreateFunction
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-functions


# [START cloudfunctions_v1_generated_CloudFunctionsService_CreateFunction_async]
from google.cloud import functions_v1


async def sample_create_function():
    # Create a client
    client = functions_v1.CloudFunctionsServiceAsyncClient()

    # Initialize request argument(s)
    function = functions_v1.CloudFunction()
    function.source_archive_url = "source_archive_url_value"

    request = functions_v1.CreateFunctionRequest(
        location="location_value",
        function=function,
    )

    # Make the request
    operation = client.create_function(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)

# [END cloudfunctions_v1_generated_CloudFunctionsService_CreateFunction_async]