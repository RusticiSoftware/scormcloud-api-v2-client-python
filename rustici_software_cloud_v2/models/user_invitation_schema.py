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


class UserInvitationSchema(object):
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
        'email': 'str',
        'url': 'str',
        'is_started': 'bool',
        'updated': 'datetime',
        'registration_id': 'str',
        'registration_report': 'UserInvitationSchemaRegistrationReport'
    }

    attribute_map = {
        'email': 'email',
        'url': 'url',
        'is_started': 'isStarted',
        'updated': 'updated',
        'registration_id': 'registrationId',
        'registration_report': 'registrationReport'
    }

    def __init__(self, email=None, url=None, is_started=None, updated=None, registration_id=None, registration_report=None):  # noqa: E501
        """UserInvitationSchema - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._url = None
        self._is_started = None
        self._updated = None
        self._registration_id = None
        self._registration_report = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if url is not None:
            self.url = url
        if is_started is not None:
            self.is_started = is_started
        if updated is not None:
            self.updated = updated
        if registration_id is not None:
            self.registration_id = registration_id
        if registration_report is not None:
            self.registration_report = registration_report

    @property
    def email(self):
        """Gets the email of this UserInvitationSchema.  # noqa: E501

        The email of the user who took an invitation.  # noqa: E501

        :return: The email of this UserInvitationSchema.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserInvitationSchema.

        The email of the user who took an invitation.  # noqa: E501

        :param email: The email of this UserInvitationSchema.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def url(self):
        """Gets the url of this UserInvitationSchema.  # noqa: E501

        The URL which the user would follow to take the invitation.  # noqa: E501

        :return: The url of this UserInvitationSchema.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this UserInvitationSchema.

        The URL which the user would follow to take the invitation.  # noqa: E501

        :param url: The url of this UserInvitationSchema.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def is_started(self):
        """Gets the is_started of this UserInvitationSchema.  # noqa: E501

        A boolean flag stating if the user has started the invitation.  # noqa: E501

        :return: The is_started of this UserInvitationSchema.  # noqa: E501
        :rtype: bool
        """
        return self._is_started

    @is_started.setter
    def is_started(self, is_started):
        """Sets the is_started of this UserInvitationSchema.

        A boolean flag stating if the user has started the invitation.  # noqa: E501

        :param is_started: The is_started of this UserInvitationSchema.  # noqa: E501
        :type: bool
        """

        self._is_started = is_started

    @property
    def updated(self):
        """Gets the updated of this UserInvitationSchema.  # noqa: E501

        :return: The updated of this UserInvitationSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this UserInvitationSchema.

        :param updated: The updated of this UserInvitationSchema.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def registration_id(self):
        """Gets the registration_id of this UserInvitationSchema.  # noqa: E501

        The id of the registration which was created from the user being invited.  # noqa: E501

        :return: The registration_id of this UserInvitationSchema.  # noqa: E501
        :rtype: str
        """
        return self._registration_id

    @registration_id.setter
    def registration_id(self, registration_id):
        """Sets the registration_id of this UserInvitationSchema.

        The id of the registration which was created from the user being invited.  # noqa: E501

        :param registration_id: The registration_id of this UserInvitationSchema.  # noqa: E501
        :type: str
        """

        self._registration_id = registration_id

    @property
    def registration_report(self):
        """Gets the registration_report of this UserInvitationSchema.  # noqa: E501

        :return: The registration_report of this UserInvitationSchema.  # noqa: E501
        :rtype: UserInvitationSchemaRegistrationReport
        """
        return self._registration_report

    @registration_report.setter
    def registration_report(self, registration_report):
        """Sets the registration_report of this UserInvitationSchema.

        :param registration_report: The registration_report of this UserInvitationSchema.  # noqa: E501
        :type: UserInvitationSchemaRegistrationReport
        """

        self._registration_report = registration_report

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
        if issubclass(UserInvitationSchema, dict):
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
        if not isinstance(other, UserInvitationSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
