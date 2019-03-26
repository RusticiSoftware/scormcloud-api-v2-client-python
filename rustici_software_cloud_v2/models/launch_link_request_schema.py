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

from rustici_software_cloud_v2.models.item_value_pair_schema import ItemValuePairSchema  # noqa: F401,E501


class LaunchLinkRequestSchema(object):
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
        'expiry': 'int',
        'redirect_on_exit_url': 'str',
        'tracking': 'bool',
        'start_sco': 'str',
        'culture': 'str',
        'css_url': 'str',
        'learner_tags': 'list[str]',
        'course_tags': 'list[str]',
        'registration_tags': 'list[str]',
        'additionalvalues': 'list[ItemValuePairSchema]'
    }

    attribute_map = {
        'expiry': 'expiry',
        'redirect_on_exit_url': 'redirectOnExitUrl',
        'tracking': 'tracking',
        'start_sco': 'startSco',
        'culture': 'culture',
        'css_url': 'cssUrl',
        'learner_tags': 'learnerTags',
        'course_tags': 'courseTags',
        'registration_tags': 'registrationTags',
        'additionalvalues': 'additionalvalues'
    }

    def __init__(self, expiry=120, redirect_on_exit_url=None, tracking=True, start_sco=None, culture=None, css_url=None, learner_tags=None, course_tags=None, registration_tags=None, additionalvalues=None):  # noqa: E501
        """LaunchLinkRequestSchema - a model defined in Swagger"""  # noqa: E501

        self._expiry = None
        self._redirect_on_exit_url = None
        self._tracking = None
        self._start_sco = None
        self._culture = None
        self._css_url = None
        self._learner_tags = None
        self._course_tags = None
        self._registration_tags = None
        self._additionalvalues = None
        self.discriminator = None

        if expiry is not None:
            self.expiry = expiry
        if redirect_on_exit_url is not None:
            self.redirect_on_exit_url = redirect_on_exit_url
        if tracking is not None:
            self.tracking = tracking
        if start_sco is not None:
            self.start_sco = start_sco
        if culture is not None:
            self.culture = culture
        if css_url is not None:
            self.css_url = css_url
        if learner_tags is not None:
            self.learner_tags = learner_tags
        if course_tags is not None:
            self.course_tags = course_tags
        if registration_tags is not None:
            self.registration_tags = registration_tags
        if additionalvalues is not None:
            self.additionalvalues = additionalvalues

    @property
    def expiry(self):
        """Gets the expiry of this LaunchLinkRequestSchema.  # noqa: E501

        Number of seconds from now this link will expire in. Defaults to 120s. Range 10s:300s  # noqa: E501

        :return: The expiry of this LaunchLinkRequestSchema.  # noqa: E501
        :rtype: int
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this LaunchLinkRequestSchema.

        Number of seconds from now this link will expire in. Defaults to 120s. Range 10s:300s  # noqa: E501

        :param expiry: The expiry of this LaunchLinkRequestSchema.  # noqa: E501
        :type: int
        """

        self._expiry = expiry

    @property
    def redirect_on_exit_url(self):
        """Gets the redirect_on_exit_url of this LaunchLinkRequestSchema.  # noqa: E501

        The URL the application should redirect to when the learner exits a course. If not specified, configured value will be used.  # noqa: E501

        :return: The redirect_on_exit_url of this LaunchLinkRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._redirect_on_exit_url

    @redirect_on_exit_url.setter
    def redirect_on_exit_url(self, redirect_on_exit_url):
        """Sets the redirect_on_exit_url of this LaunchLinkRequestSchema.

        The URL the application should redirect to when the learner exits a course. If not specified, configured value will be used.  # noqa: E501

        :param redirect_on_exit_url: The redirect_on_exit_url of this LaunchLinkRequestSchema.  # noqa: E501
        :type: str
        """

        self._redirect_on_exit_url = redirect_on_exit_url

    @property
    def tracking(self):
        """Gets the tracking of this LaunchLinkRequestSchema.  # noqa: E501

        Should this launch be tracked? If false, Engine will avoid tracking to the extent possible for the standard being used.  # noqa: E501

        :return: The tracking of this LaunchLinkRequestSchema.  # noqa: E501
        :rtype: bool
        """
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        """Sets the tracking of this LaunchLinkRequestSchema.

        Should this launch be tracked? If false, Engine will avoid tracking to the extent possible for the standard being used.  # noqa: E501

        :param tracking: The tracking of this LaunchLinkRequestSchema.  # noqa: E501
        :type: bool
        """

        self._tracking = tracking

    @property
    def start_sco(self):
        """Gets the start_sco of this LaunchLinkRequestSchema.  # noqa: E501

        For SCORM, SCO identifier to override launch, overriding the normal sequencing.  # noqa: E501

        :return: The start_sco of this LaunchLinkRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._start_sco

    @start_sco.setter
    def start_sco(self, start_sco):
        """Sets the start_sco of this LaunchLinkRequestSchema.

        For SCORM, SCO identifier to override launch, overriding the normal sequencing.  # noqa: E501

        :param start_sco: The start_sco of this LaunchLinkRequestSchema.  # noqa: E501
        :type: str
        """

        self._start_sco = start_sco

    @property
    def culture(self):
        """Gets the culture of this LaunchLinkRequestSchema.  # noqa: E501

        This parameter should specify a culture code. If specified, and supported, the navigation and alerts in the player will be displayed in the associated language. If not specified, the locale of the user’s browser will be used.  # noqa: E501

        :return: The culture of this LaunchLinkRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._culture

    @culture.setter
    def culture(self, culture):
        """Sets the culture of this LaunchLinkRequestSchema.

        This parameter should specify a culture code. If specified, and supported, the navigation and alerts in the player will be displayed in the associated language. If not specified, the locale of the user’s browser will be used.  # noqa: E501

        :param culture: The culture of this LaunchLinkRequestSchema.  # noqa: E501
        :type: str
        """

        self._culture = culture

    @property
    def css_url(self):
        """Gets the css_url of this LaunchLinkRequestSchema.  # noqa: E501

        A Url pointing to custom css for the player to use.  # noqa: E501

        :return: The css_url of this LaunchLinkRequestSchema.  # noqa: E501
        :rtype: str
        """
        return self._css_url

    @css_url.setter
    def css_url(self, css_url):
        """Sets the css_url of this LaunchLinkRequestSchema.

        A Url pointing to custom css for the player to use.  # noqa: E501

        :param css_url: The css_url of this LaunchLinkRequestSchema.  # noqa: E501
        :type: str
        """

        self._css_url = css_url

    @property
    def learner_tags(self):
        """Gets the learner_tags of this LaunchLinkRequestSchema.  # noqa: E501


        :return: The learner_tags of this LaunchLinkRequestSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._learner_tags

    @learner_tags.setter
    def learner_tags(self, learner_tags):
        """Sets the learner_tags of this LaunchLinkRequestSchema.


        :param learner_tags: The learner_tags of this LaunchLinkRequestSchema.  # noqa: E501
        :type: list[str]
        """

        self._learner_tags = learner_tags

    @property
    def course_tags(self):
        """Gets the course_tags of this LaunchLinkRequestSchema.  # noqa: E501


        :return: The course_tags of this LaunchLinkRequestSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._course_tags

    @course_tags.setter
    def course_tags(self, course_tags):
        """Sets the course_tags of this LaunchLinkRequestSchema.


        :param course_tags: The course_tags of this LaunchLinkRequestSchema.  # noqa: E501
        :type: list[str]
        """

        self._course_tags = course_tags

    @property
    def registration_tags(self):
        """Gets the registration_tags of this LaunchLinkRequestSchema.  # noqa: E501


        :return: The registration_tags of this LaunchLinkRequestSchema.  # noqa: E501
        :rtype: list[str]
        """
        return self._registration_tags

    @registration_tags.setter
    def registration_tags(self, registration_tags):
        """Sets the registration_tags of this LaunchLinkRequestSchema.


        :param registration_tags: The registration_tags of this LaunchLinkRequestSchema.  # noqa: E501
        :type: list[str]
        """

        self._registration_tags = registration_tags

    @property
    def additionalvalues(self):
        """Gets the additionalvalues of this LaunchLinkRequestSchema.  # noqa: E501


        :return: The additionalvalues of this LaunchLinkRequestSchema.  # noqa: E501
        :rtype: list[ItemValuePairSchema]
        """
        return self._additionalvalues

    @additionalvalues.setter
    def additionalvalues(self, additionalvalues):
        """Sets the additionalvalues of this LaunchLinkRequestSchema.


        :param additionalvalues: The additionalvalues of this LaunchLinkRequestSchema.  # noqa: E501
        :type: list[ItemValuePairSchema]
        """

        self._additionalvalues = additionalvalues

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
        if issubclass(LaunchLinkRequestSchema, dict):
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
        if not isinstance(other, LaunchLinkRequestSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
