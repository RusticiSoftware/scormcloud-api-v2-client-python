# coding: utf-8

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: systems@rusticisoftware.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class XapiStatementPipePutSchema(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'source': 'XapiEndpointSchema',
        'target': 'XapiEndpointSchema'
    }

    attribute_map = {
        'source': 'source',
        'target': 'target'
    }

    def __init__(self, source=None, target=None):  # noqa: E501
        """XapiStatementPipePutSchema - a model defined in Swagger"""  # noqa: E501

        self._source = None
        self._target = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if target is not None:
            self.target = target

    @property
    def source(self):
        """Gets the source of this XapiStatementPipePutSchema.  # noqa: E501


        :return: The source of this XapiStatementPipePutSchema.  # noqa: E501
        :rtype: XapiEndpointSchema
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this XapiStatementPipePutSchema.


        :param source: The source of this XapiStatementPipePutSchema.  # noqa: E501
        :type: XapiEndpointSchema
        """

        self._source = source

    @property
    def target(self):
        """Gets the target of this XapiStatementPipePutSchema.  # noqa: E501


        :return: The target of this XapiStatementPipePutSchema.  # noqa: E501
        :rtype: XapiEndpointSchema
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this XapiStatementPipePutSchema.


        :param target: The target of this XapiStatementPipePutSchema.  # noqa: E501
        :type: XapiEndpointSchema
        """

        self._target = target

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(XapiStatementPipePutSchema, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, XapiStatementPipePutSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
