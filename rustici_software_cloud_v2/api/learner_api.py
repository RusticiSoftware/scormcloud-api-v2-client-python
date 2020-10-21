# coding: utf-8

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: systems@rusticisoftware.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from rustici_software_cloud_v2.api_client import ApiClient


class LearnerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_all_learner_data(self, learner_id, user_email, **kwargs):  # noqa: E501
        """Deletes all of the information associated with a learner in an application, by learner id.   # noqa: E501

        Deletes all of the information associated with a learner in an application, by learner id. This is meant for use with complying with GDPR requests from learners.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_all_learner_data(learner_id, user_email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str learner_id: The id of the learner for which to remove all data from an application (required)
        :param str user_email: The email of the user initiating this request on behalf of the learner being deleted. This must be a valid primary email address for a SCORM Cloud realm which this application is in. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_all_learner_data_with_http_info(learner_id, user_email, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_all_learner_data_with_http_info(learner_id, user_email, **kwargs)  # noqa: E501
            return data

    def delete_all_learner_data_with_http_info(self, learner_id, user_email, **kwargs):  # noqa: E501
        """Deletes all of the information associated with a learner in an application, by learner id.   # noqa: E501

        Deletes all of the information associated with a learner in an application, by learner id. This is meant for use with complying with GDPR requests from learners.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_all_learner_data_with_http_info(learner_id, user_email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str learner_id: The id of the learner for which to remove all data from an application (required)
        :param str user_email: The email of the user initiating this request on behalf of the learner being deleted. This must be a valid primary email address for a SCORM Cloud realm which this application is in. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['learner_id', 'user_email']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_all_learner_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'learner_id' is set
        if ('learner_id' not in params or
                params['learner_id'] is None):
            raise ValueError("Missing the required parameter `learner_id` when calling `delete_all_learner_data`")  # noqa: E501
        # verify the required parameter 'user_email' is set
        if ('user_email' not in params or
                params['user_email'] is None):
            raise ValueError("Missing the required parameter `user_email` when calling `delete_all_learner_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'learner_id' in params:
            path_params['learnerId'] = params['learner_id']  # noqa: E501

        query_params = []
        if 'user_email' in params:
            query_params.append(('userEmail', params['user_email']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']  # noqa: E501

        return self.api_client.call_api(
            '/learner/{learnerId}/delete-information', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_learner_tags(self, learner_id, tags, **kwargs):  # noqa: E501
        """Delete the tags for this learner   # noqa: E501

        Delete the tags for this learner   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_learner_tags(learner_id, tags, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str learner_id: The id of the learner for which to remove all data from an application (required)
        :param TagListSchema tags: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_learner_tags_with_http_info(learner_id, tags, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_learner_tags_with_http_info(learner_id, tags, **kwargs)  # noqa: E501
            return data

    def delete_learner_tags_with_http_info(self, learner_id, tags, **kwargs):  # noqa: E501
        """Delete the tags for this learner   # noqa: E501

        Delete the tags for this learner   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_learner_tags_with_http_info(learner_id, tags, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str learner_id: The id of the learner for which to remove all data from an application (required)
        :param TagListSchema tags: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['learner_id', 'tags']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_learner_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'learner_id' is set
        if ('learner_id' not in params or
                params['learner_id'] is None):
            raise ValueError("Missing the required parameter `learner_id` when calling `delete_learner_tags`")  # noqa: E501
        # verify the required parameter 'tags' is set
        if ('tags' not in params or
                params['tags'] is None):
            raise ValueError("Missing the required parameter `tags` when calling `delete_learner_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'learner_id' in params:
            path_params['learnerId'] = params['learner_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tags' in params:
            body_params = params['tags']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']  # noqa: E501

        return self.api_client.call_api(
            '/learner/{learnerId}/tags', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_learner_tags(self, learner_id, **kwargs):  # noqa: E501
        """Get the tags for this learner   # noqa: E501

        Get the tags for this learner   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_learner_tags(learner_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str learner_id: The id of the learner for which to remove all data from an application (required)
        :return: TagListSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_learner_tags_with_http_info(learner_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_learner_tags_with_http_info(learner_id, **kwargs)  # noqa: E501
            return data

    def get_learner_tags_with_http_info(self, learner_id, **kwargs):  # noqa: E501
        """Get the tags for this learner   # noqa: E501

        Get the tags for this learner   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_learner_tags_with_http_info(learner_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str learner_id: The id of the learner for which to remove all data from an application (required)
        :return: TagListSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['learner_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_learner_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'learner_id' is set
        if ('learner_id' not in params or
                params['learner_id'] is None):
            raise ValueError("Missing the required parameter `learner_id` when calling `get_learner_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'learner_id' in params:
            path_params['learnerId'] = params['learner_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']  # noqa: E501

        return self.api_client.call_api(
            '/learner/{learnerId}/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TagListSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_learner_tags(self, learner_id, tags, **kwargs):  # noqa: E501
        """Set the tags for this learner   # noqa: E501

        Set the tags for this learner   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_learner_tags(learner_id, tags, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str learner_id: The id of the learner for which to remove all data from an application (required)
        :param TagListSchema tags: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_learner_tags_with_http_info(learner_id, tags, **kwargs)  # noqa: E501
        else:
            (data) = self.put_learner_tags_with_http_info(learner_id, tags, **kwargs)  # noqa: E501
            return data

    def put_learner_tags_with_http_info(self, learner_id, tags, **kwargs):  # noqa: E501
        """Set the tags for this learner   # noqa: E501

        Set the tags for this learner   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_learner_tags_with_http_info(learner_id, tags, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str learner_id: The id of the learner for which to remove all data from an application (required)
        :param TagListSchema tags: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['learner_id', 'tags']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_learner_tags" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'learner_id' is set
        if ('learner_id' not in params or
                params['learner_id'] is None):
            raise ValueError("Missing the required parameter `learner_id` when calling `put_learner_tags`")  # noqa: E501
        # verify the required parameter 'tags' is set
        if ('tags' not in params or
                params['tags'] is None):
            raise ValueError("Missing the required parameter `tags` when calling `put_learner_tags`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'learner_id' in params:
            path_params['learnerId'] = params['learner_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tags' in params:
            body_params = params['tags']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']  # noqa: E501

        return self.api_client.call_api(
            '/learner/{learnerId}/tags', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_learner_tags_batch(self, batch, **kwargs):  # noqa: E501
        """Sets all of the provided tags on all of the provided learners  # noqa: E501

        Sets all of the provided tags on all of the provided learners   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_learner_tags_batch(batch, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BatchTagsSchema batch: Object representing an array of ids to apply an array of tags to. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_learner_tags_batch_with_http_info(batch, **kwargs)  # noqa: E501
        else:
            (data) = self.put_learner_tags_batch_with_http_info(batch, **kwargs)  # noqa: E501
            return data

    def put_learner_tags_batch_with_http_info(self, batch, **kwargs):  # noqa: E501
        """Sets all of the provided tags on all of the provided learners  # noqa: E501

        Sets all of the provided tags on all of the provided learners   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_learner_tags_batch_with_http_info(batch, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BatchTagsSchema batch: Object representing an array of ids to apply an array of tags to. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['batch']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_learner_tags_batch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'batch' is set
        if ('batch' not in params or
                params['batch'] is None):
            raise ValueError("Missing the required parameter `batch` when calling `put_learner_tags_batch`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'batch' in params:
            body_params = params['batch']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']  # noqa: E501

        return self.api_client.call_api(
            '/learner/tags', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_learner_info(self, learner_id, learner_info, **kwargs):  # noqa: E501
        """Update a learner's info on all of their registrations.  # noqa: E501

        A learner in SCORM Cloud is not an entity on its own.  In fact, learners only exist as information on individual registrations. This method will update the information on each of the registrations that the provided `learnerId` is attached to.  You may update any of the values available in the LearnerSchema which is posted.  Any values you do not wish to alter, omit from the post.  Depending on the field, providing something like an empty string may have unintended consequences.  Lastly, it's important to note that this method is asynchronous.  A success status will be returned, and that signifies that a background process has been spun up to alter the learner's info.  As such, you may find a short period of delay in seeing the changes shown on all registrations.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_learner_info(learner_id, learner_info, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str learner_id: The id of the learner to be updated (required)
        :param LearnerSchema learner_info: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_learner_info_with_http_info(learner_id, learner_info, **kwargs)  # noqa: E501
        else:
            (data) = self.update_learner_info_with_http_info(learner_id, learner_info, **kwargs)  # noqa: E501
            return data

    def update_learner_info_with_http_info(self, learner_id, learner_info, **kwargs):  # noqa: E501
        """Update a learner's info on all of their registrations.  # noqa: E501

        A learner in SCORM Cloud is not an entity on its own.  In fact, learners only exist as information on individual registrations. This method will update the information on each of the registrations that the provided `learnerId` is attached to.  You may update any of the values available in the LearnerSchema which is posted.  Any values you do not wish to alter, omit from the post.  Depending on the field, providing something like an empty string may have unintended consequences.  Lastly, it's important to note that this method is asynchronous.  A success status will be returned, and that signifies that a background process has been spun up to alter the learner's info.  As such, you may find a short period of delay in seeing the changes shown on all registrations.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_learner_info_with_http_info(learner_id, learner_info, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str learner_id: The id of the learner to be updated (required)
        :param LearnerSchema learner_info: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['learner_id', 'learner_info']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_learner_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'learner_id' is set
        if ('learner_id' not in params or
                params['learner_id'] is None):
            raise ValueError("Missing the required parameter `learner_id` when calling `update_learner_info`")  # noqa: E501
        # verify the required parameter 'learner_info' is set
        if ('learner_info' not in params or
                params['learner_info'] is None):
            raise ValueError("Missing the required parameter `learner_info` when calling `update_learner_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'learner_id' in params:
            path_params['learnerId'] = params['learner_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'learner_info' in params:
            body_params = params['learner_info']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APP_NORMAL', 'OAUTH']  # noqa: E501

        return self.api_client.call_api(
            '/learner/{learnerId}/updateInfo', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
