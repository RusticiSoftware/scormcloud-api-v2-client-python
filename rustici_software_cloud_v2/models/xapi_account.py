# coding: utf-8

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.  # noqa: E501

    OpenAPI spec version: 2.0 beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class XapiAccount(object):
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
        'home_page': 'str',
        'name': 'str'
    }

    attribute_map = {
        'home_page': 'homePage',
        'name': 'name'
    }

    def __init__(self, home_page=None, name=None):  # noqa: E501
        """XapiAccount - a model defined in Swagger"""  # noqa: E501

        self._home_page = None
        self._name = None
        self.discriminator = None

        self.home_page = home_page
        self.name = name

    @property
    def home_page(self):
        """Gets the home_page of this XapiAccount.  # noqa: E501


        :return: The home_page of this XapiAccount.  # noqa: E501
        :rtype: str
        """
        return self._home_page

    @home_page.setter
    def home_page(self, home_page):
        """Sets the home_page of this XapiAccount.


        :param home_page: The home_page of this XapiAccount.  # noqa: E501
        :type: str
        """
        if home_page is None:
            raise ValueError("Invalid value for `home_page`, must not be `None`")  # noqa: E501

        self._home_page = home_page

    @property
    def name(self):
        """Gets the name of this XapiAccount.  # noqa: E501


        :return: The name of this XapiAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XapiAccount.


        :param name: The name of this XapiAccount.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(XapiAccount, dict):
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
        if not isinstance(other, XapiAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
