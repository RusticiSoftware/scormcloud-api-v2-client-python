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


class XapiActivity(object):
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
        'object_type': 'str',
        'id': 'str',
        'definition': 'XapiActivityDefinition'
    }

    attribute_map = {
        'object_type': 'objectType',
        'id': 'id',
        'definition': 'definition'
    }

    def __init__(self, object_type='Activity', id=None, definition=None):  # noqa: E501
        """XapiActivity - a model defined in Swagger"""  # noqa: E501

        self._object_type = None
        self._id = None
        self._definition = None
        self.discriminator = None

        if object_type is not None:
            self.object_type = object_type
        self.id = id
        if definition is not None:
            self.definition = definition

    @property
    def object_type(self):
        """Gets the object_type of this XapiActivity.  # noqa: E501

        :return: The object_type of this XapiActivity.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this XapiActivity.

        :param object_type: The object_type of this XapiActivity.  # noqa: E501
        :type: str
        """

        self._object_type = object_type

    @property
    def id(self):
        """Gets the id of this XapiActivity.  # noqa: E501

        :return: The id of this XapiActivity.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XapiActivity.

        :param id: The id of this XapiActivity.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def definition(self):
        """Gets the definition of this XapiActivity.  # noqa: E501

        :return: The definition of this XapiActivity.  # noqa: E501
        :rtype: XapiActivityDefinition
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this XapiActivity.

        :param definition: The definition of this XapiActivity.  # noqa: E501
        :type: XapiActivityDefinition
        """

        self._definition = definition

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
        if issubclass(XapiActivity, dict):
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
        if not isinstance(other, XapiActivity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
