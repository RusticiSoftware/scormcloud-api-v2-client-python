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


class XapiAttachment(object):
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
        'usage_type': 'str',
        'display': 'dict(str, str)',
        'description': 'dict(str, str)',
        'content_type': 'str',
        'length': 'int',
        'sha2': 'str',
        'file_url': 'str'
    }

    attribute_map = {
        'usage_type': 'usageType',
        'display': 'display',
        'description': 'description',
        'content_type': 'contentType',
        'length': 'length',
        'sha2': 'sha2',
        'file_url': 'fileUrl'
    }

    def __init__(self, usage_type=None, display=None, description=None, content_type=None, length=None, sha2=None, file_url=None):  # noqa: E501
        """XapiAttachment - a model defined in Swagger"""  # noqa: E501

        self._usage_type = None
        self._display = None
        self._description = None
        self._content_type = None
        self._length = None
        self._sha2 = None
        self._file_url = None
        self.discriminator = None

        self.usage_type = usage_type
        self.display = display
        if description is not None:
            self.description = description
        self.content_type = content_type
        self.length = length
        self.sha2 = sha2
        if file_url is not None:
            self.file_url = file_url

    @property
    def usage_type(self):
        """Gets the usage_type of this XapiAttachment.  # noqa: E501


        :return: The usage_type of this XapiAttachment.  # noqa: E501
        :rtype: str
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        """Sets the usage_type of this XapiAttachment.


        :param usage_type: The usage_type of this XapiAttachment.  # noqa: E501
        :type: str
        """
        if usage_type is None:
            raise ValueError("Invalid value for `usage_type`, must not be `None`")  # noqa: E501

        self._usage_type = usage_type

    @property
    def display(self):
        """Gets the display of this XapiAttachment.  # noqa: E501


        :return: The display of this XapiAttachment.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this XapiAttachment.


        :param display: The display of this XapiAttachment.  # noqa: E501
        :type: dict(str, str)
        """
        if display is None:
            raise ValueError("Invalid value for `display`, must not be `None`")  # noqa: E501

        self._display = display

    @property
    def description(self):
        """Gets the description of this XapiAttachment.  # noqa: E501


        :return: The description of this XapiAttachment.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XapiAttachment.


        :param description: The description of this XapiAttachment.  # noqa: E501
        :type: dict(str, str)
        """

        self._description = description

    @property
    def content_type(self):
        """Gets the content_type of this XapiAttachment.  # noqa: E501


        :return: The content_type of this XapiAttachment.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this XapiAttachment.


        :param content_type: The content_type of this XapiAttachment.  # noqa: E501
        :type: str
        """
        if content_type is None:
            raise ValueError("Invalid value for `content_type`, must not be `None`")  # noqa: E501

        self._content_type = content_type

    @property
    def length(self):
        """Gets the length of this XapiAttachment.  # noqa: E501


        :return: The length of this XapiAttachment.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this XapiAttachment.


        :param length: The length of this XapiAttachment.  # noqa: E501
        :type: int
        """
        if length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501

        self._length = length

    @property
    def sha2(self):
        """Gets the sha2 of this XapiAttachment.  # noqa: E501


        :return: The sha2 of this XapiAttachment.  # noqa: E501
        :rtype: str
        """
        return self._sha2

    @sha2.setter
    def sha2(self, sha2):
        """Sets the sha2 of this XapiAttachment.


        :param sha2: The sha2 of this XapiAttachment.  # noqa: E501
        :type: str
        """
        if sha2 is None:
            raise ValueError("Invalid value for `sha2`, must not be `None`")  # noqa: E501

        self._sha2 = sha2

    @property
    def file_url(self):
        """Gets the file_url of this XapiAttachment.  # noqa: E501


        :return: The file_url of this XapiAttachment.  # noqa: E501
        :rtype: str
        """
        return self._file_url

    @file_url.setter
    def file_url(self, file_url):
        """Sets the file_url of this XapiAttachment.


        :param file_url: The file_url of this XapiAttachment.  # noqa: E501
        :type: str
        """

        self._file_url = file_url

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
        if issubclass(XapiAttachment, dict):
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
        if not isinstance(other, XapiAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
