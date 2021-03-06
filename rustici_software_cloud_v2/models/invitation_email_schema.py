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


class InvitationEmailSchema(object):
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
        'subject': 'str',
        'body': 'str',
        'addresses': 'list[str]'
    }

    attribute_map = {
        'subject': 'subject',
        'body': 'body',
        'addresses': 'addresses'
    }

    def __init__(self, subject=None, body=None, addresses=None):  # noqa: E501
        """InvitationEmailSchema - a model defined in Swagger"""  # noqa: E501

        self._subject = None
        self._body = None
        self._addresses = None
        self.discriminator = None

        if subject is not None:
            self.subject = subject
        if body is not None:
            self.body = body
        self.addresses = addresses

    @property
    def subject(self):
        """Gets the subject of this InvitationEmailSchema.  # noqa: E501

        The subject line for the email.  # noqa: E501

        :return: The subject of this InvitationEmailSchema.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this InvitationEmailSchema.

        The subject line for the email.  # noqa: E501

        :param subject: The subject of this InvitationEmailSchema.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def body(self):
        """Gets the body of this InvitationEmailSchema.  # noqa: E501

        The body of the email.  # noqa: E501

        :return: The body of this InvitationEmailSchema.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this InvitationEmailSchema.

        The body of the email.  # noqa: E501

        :param body: The body of this InvitationEmailSchema.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def addresses(self):
        """Gets the addresses of this InvitationEmailSchema.  # noqa: E501

        A comma separated list of email addresses to which this invitation will be sent.  NOTE: registrations with automatically be create for each of these e-mail addresses.  # noqa: E501

        :return: The addresses of this InvitationEmailSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this InvitationEmailSchema.

        A comma separated list of email addresses to which this invitation will be sent.  NOTE: registrations with automatically be create for each of these e-mail addresses.  # noqa: E501

        :param addresses: The addresses of this InvitationEmailSchema.  # noqa: E501
        :type: list[str]
        """
        if addresses is None:
            raise ValueError("Invalid value for `addresses`, must not be `None`")  # noqa: E501

        self._addresses = addresses

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
        if issubclass(InvitationEmailSchema, dict):
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
        if not isinstance(other, InvitationEmailSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
