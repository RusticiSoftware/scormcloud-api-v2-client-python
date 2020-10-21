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


class MetadataSchema(object):
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
        'title': 'str',
        'title_language': 'str',
        'description': 'str',
        'description_language': 'str',
        'duration': 'str',
        'typical_time': 'str',
        'keywords': 'list[str]'
    }

    attribute_map = {
        'title': 'title',
        'title_language': 'titleLanguage',
        'description': 'description',
        'description_language': 'descriptionLanguage',
        'duration': 'duration',
        'typical_time': 'typicalTime',
        'keywords': 'keywords'
    }

    def __init__(self, title=None, title_language=None, description=None, description_language=None, duration=None, typical_time=None, keywords=None):  # noqa: E501
        """MetadataSchema - a model defined in Swagger"""  # noqa: E501

        self._title = None
        self._title_language = None
        self._description = None
        self._description_language = None
        self._duration = None
        self._typical_time = None
        self._keywords = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if title_language is not None:
            self.title_language = title_language
        if description is not None:
            self.description = description
        if description_language is not None:
            self.description_language = description_language
        if duration is not None:
            self.duration = duration
        if typical_time is not None:
            self.typical_time = typical_time
        if keywords is not None:
            self.keywords = keywords

    @property
    def title(self):
        """Gets the title of this MetadataSchema.  # noqa: E501


        :return: The title of this MetadataSchema.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MetadataSchema.


        :param title: The title of this MetadataSchema.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def title_language(self):
        """Gets the title_language of this MetadataSchema.  # noqa: E501


        :return: The title_language of this MetadataSchema.  # noqa: E501
        :rtype: str
        """
        return self._title_language

    @title_language.setter
    def title_language(self, title_language):
        """Sets the title_language of this MetadataSchema.


        :param title_language: The title_language of this MetadataSchema.  # noqa: E501
        :type: str
        """

        self._title_language = title_language

    @property
    def description(self):
        """Gets the description of this MetadataSchema.  # noqa: E501


        :return: The description of this MetadataSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MetadataSchema.


        :param description: The description of this MetadataSchema.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def description_language(self):
        """Gets the description_language of this MetadataSchema.  # noqa: E501


        :return: The description_language of this MetadataSchema.  # noqa: E501
        :rtype: str
        """
        return self._description_language

    @description_language.setter
    def description_language(self, description_language):
        """Sets the description_language of this MetadataSchema.


        :param description_language: The description_language of this MetadataSchema.  # noqa: E501
        :type: str
        """

        self._description_language = description_language

    @property
    def duration(self):
        """Gets the duration of this MetadataSchema.  # noqa: E501


        :return: The duration of this MetadataSchema.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this MetadataSchema.


        :param duration: The duration of this MetadataSchema.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def typical_time(self):
        """Gets the typical_time of this MetadataSchema.  # noqa: E501


        :return: The typical_time of this MetadataSchema.  # noqa: E501
        :rtype: str
        """
        return self._typical_time

    @typical_time.setter
    def typical_time(self, typical_time):
        """Sets the typical_time of this MetadataSchema.


        :param typical_time: The typical_time of this MetadataSchema.  # noqa: E501
        :type: str
        """

        self._typical_time = typical_time

    @property
    def keywords(self):
        """Gets the keywords of this MetadataSchema.  # noqa: E501


        :return: The keywords of this MetadataSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this MetadataSchema.


        :param keywords: The keywords of this MetadataSchema.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

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
        if issubclass(MetadataSchema, dict):
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
        if not isinstance(other, MetadataSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
