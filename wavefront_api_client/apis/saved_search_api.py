# coding: utf-8

"""
SavedSearchApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class SavedSearchApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_saved_search(self, **kwargs):
        """
        Create a saved search
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_saved_search(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SavedSearch body: Example Body: \n<pre>{\n  \"query\": {\n    \"foo\": \"{\\\"searchTerms\\\":[{\\\"type\\\":\\\"freetext\\\",\\\"value\\\":\\\"foo\\\"}]}\"\n  },\n  \"entityType\": \"DASHBOARD\"\n}</pre>
        :return: ResponseContainerSavedSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_saved_search" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/v2/savedsearch'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ResponseContainerSavedSearch',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_saved_search(self, id, **kwargs):
        """
        Delete a specific saved search
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_saved_search(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :return: ResponseContainerSavedSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_saved_search" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_saved_search`")

        resource_path = '/api/v2/savedsearch/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ResponseContainerSavedSearch',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_all_entity_type_saved_searches(self, entitytype, **kwargs):
        """
        Get all saved searches for a specific entity type for a user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_entity_type_saved_searches(entitytype, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str entitytype:  (required)
        :param int offset: 
        :param int limit: 
        :return: ResponseContainerPagedSavedSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entitytype', 'offset', 'limit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_entity_type_saved_searches" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'entitytype' is set
        if ('entitytype' not in params) or (params['entitytype'] is None):
            raise ValueError("Missing the required parameter `entitytype` when calling `get_all_entity_type_saved_searches`")

        resource_path = '/api/v2/savedsearch/type/{entitytype}'.replace('{format}', 'json')
        path_params = {}
        if 'entitytype' in params:
            path_params['entitytype'] = params['entitytype']

        query_params = {}
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'limit' in params:
            query_params['limit'] = params['limit']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ResponseContainerPagedSavedSearch',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_all_saved_searches(self, **kwargs):
        """
        Get all saved searches for a user
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_saved_searches(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int offset: 
        :param int limit: 
        :return: ResponseContainerPagedSavedSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_saved_searches" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/api/v2/savedsearch'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'limit' in params:
            query_params['limit'] = params['limit']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ResponseContainerPagedSavedSearch',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_saved_search(self, id, **kwargs):
        """
        Get a specific saved search
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_saved_search(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :return: ResponseContainerSavedSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_saved_search" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_saved_search`")

        resource_path = '/api/v2/savedsearch/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ResponseContainerSavedSearch',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_saved_search(self, id, **kwargs):
        """
        Update a specific saved search
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_saved_search(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id:  (required)
        :param SavedSearch body: Example Body: \n<pre>{\n  \"query\": {\n    \"foo\": \"{\\\"searchTerms\\\":[{\\\"type\\\":\\\"freetext\\\",\\\"value\\\":\\\"foo\\\"}]}\"\n  },\n  \"entityType\": \"DASHBOARD\"\n}</pre>
        :return: ResponseContainerSavedSearch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_saved_search" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_saved_search`")

        resource_path = '/api/v2/savedsearch/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ResponseContainerSavedSearch',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
