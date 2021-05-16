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
from typing import (
    Any,
    AsyncIterable,
    Awaitable,
    Callable,
    Iterable,
    Sequence,
    Tuple,
    Optional,
)

from google.cloud.functions_v1.types import functions


class ListFunctionsPager:
    """A pager for iterating through ``list_functions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.functions_v1.types.ListFunctionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``functions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListFunctions`` requests and continue to iterate
    through the ``functions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.functions_v1.types.ListFunctionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., functions.ListFunctionsResponse],
        request: functions.ListFunctionsRequest,
        response: functions.ListFunctionsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.functions_v1.types.ListFunctionsRequest):
                The initial request object.
            response (google.cloud.functions_v1.types.ListFunctionsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = functions.ListFunctionsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[functions.ListFunctionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[functions.CloudFunction]:
        for page in self.pages:
            yield from page.functions

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListFunctionsAsyncPager:
    """A pager for iterating through ``list_functions`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.functions_v1.types.ListFunctionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``functions`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListFunctions`` requests and continue to iterate
    through the ``functions`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.functions_v1.types.ListFunctionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[functions.ListFunctionsResponse]],
        request: functions.ListFunctionsRequest,
        response: functions.ListFunctionsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.functions_v1.types.ListFunctionsRequest):
                The initial request object.
            response (google.cloud.functions_v1.types.ListFunctionsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = functions.ListFunctionsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[functions.ListFunctionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[functions.CloudFunction]:
        async def async_generator():
            async for page in self.pages:
                for response in page.functions:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
