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


class PrivateInvitationSchema(object):
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
        'id': 'str',
        'course_id': 'str',
        'allow_launch': 'bool',
        'invitation_email': 'InvitationEmailSchema',
        'create_date': 'datetime',
        'updated': 'datetime',
        'post_back': 'PostBackSchema',
        'expiration_date': 'datetime',
        'registration_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'course_id': 'courseId',
        'allow_launch': 'allowLaunch',
        'invitation_email': 'invitationEmail',
        'create_date': 'createDate',
        'updated': 'updated',
        'post_back': 'postBack',
        'expiration_date': 'expirationDate',
        'registration_count': 'registrationCount'
    }

    def __init__(self, id=None, course_id=None, allow_launch=None, invitation_email=None, create_date=None, updated=None, post_back=None, expiration_date=None, registration_count=None):  # noqa: E501
        """PrivateInvitationSchema - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._course_id = None
        self._allow_launch = None
        self._invitation_email = None
        self._create_date = None
        self._updated = None
        self._post_back = None
        self._expiration_date = None
        self._registration_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if course_id is not None:
            self.course_id = course_id
        if allow_launch is not None:
            self.allow_launch = allow_launch
        if invitation_email is not None:
            self.invitation_email = invitation_email
        if create_date is not None:
            self.create_date = create_date
        if updated is not None:
            self.updated = updated
        if post_back is not None:
            self.post_back = post_back
        if expiration_date is not None:
            self.expiration_date = expiration_date
        if registration_count is not None:
            self.registration_count = registration_count

    @property
    def id(self):
        """Gets the id of this PrivateInvitationSchema.  # noqa: E501

        The invitationId for this invitation.  # noqa: E501

        :return: The id of this PrivateInvitationSchema.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrivateInvitationSchema.

        The invitationId for this invitation.  # noqa: E501

        :param id: The id of this PrivateInvitationSchema.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def course_id(self):
        """Gets the course_id of this PrivateInvitationSchema.  # noqa: E501

        Course Id for this Invitation.  # noqa: E501

        :return: The course_id of this PrivateInvitationSchema.  # noqa: E501
        :rtype: str
        """
        return self._course_id

    @course_id.setter
    def course_id(self, course_id):
        """Sets the course_id of this PrivateInvitationSchema.

        Course Id for this Invitation.  # noqa: E501

        :param course_id: The course_id of this PrivateInvitationSchema.  # noqa: E501
        :type: str
        """

        self._course_id = course_id

    @property
    def allow_launch(self):
        """Gets the allow_launch of this PrivateInvitationSchema.  # noqa: E501

        If true, then new registrations can be created for this dispatch.  # noqa: E501

        :return: The allow_launch of this PrivateInvitationSchema.  # noqa: E501
        :rtype: bool
        """
        return self._allow_launch

    @allow_launch.setter
    def allow_launch(self, allow_launch):
        """Sets the allow_launch of this PrivateInvitationSchema.

        If true, then new registrations can be created for this dispatch.  # noqa: E501

        :param allow_launch: The allow_launch of this PrivateInvitationSchema.  # noqa: E501
        :type: bool
        """

        self._allow_launch = allow_launch

    @property
    def invitation_email(self):
        """Gets the invitation_email of this PrivateInvitationSchema.  # noqa: E501


        :return: The invitation_email of this PrivateInvitationSchema.  # noqa: E501
        :rtype: InvitationEmailSchema
        """
        return self._invitation_email

    @invitation_email.setter
    def invitation_email(self, invitation_email):
        """Sets the invitation_email of this PrivateInvitationSchema.


        :param invitation_email: The invitation_email of this PrivateInvitationSchema.  # noqa: E501
        :type: InvitationEmailSchema
        """

        self._invitation_email = invitation_email

    @property
    def create_date(self):
        """Gets the create_date of this PrivateInvitationSchema.  # noqa: E501

        The create date for the invitation  # noqa: E501

        :return: The create_date of this PrivateInvitationSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this PrivateInvitationSchema.

        The create date for the invitation  # noqa: E501

        :param create_date: The create_date of this PrivateInvitationSchema.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def updated(self):
        """Gets the updated of this PrivateInvitationSchema.  # noqa: E501


        :return: The updated of this PrivateInvitationSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this PrivateInvitationSchema.


        :param updated: The updated of this PrivateInvitationSchema.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

    @property
    def post_back(self):
        """Gets the post_back of this PrivateInvitationSchema.  # noqa: E501

        Specifies a URL for which to post activity and status data in real time as the course is completed  # noqa: E501

        :return: The post_back of this PrivateInvitationSchema.  # noqa: E501
        :rtype: PostBackSchema
        """
        return self._post_back

    @post_back.setter
    def post_back(self, post_back):
        """Sets the post_back of this PrivateInvitationSchema.

        Specifies a URL for which to post activity and status data in real time as the course is completed  # noqa: E501

        :param post_back: The post_back of this PrivateInvitationSchema.  # noqa: E501
        :type: PostBackSchema
        """

        self._post_back = post_back

    @property
    def expiration_date(self):
        """Gets the expiration_date of this PrivateInvitationSchema.  # noqa: E501

        The date this invitation will expire and can not be launched (formatted yyyyMMddHHmmss in UTC time).  # noqa: E501

        :return: The expiration_date of this PrivateInvitationSchema.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this PrivateInvitationSchema.

        The date this invitation will expire and can not be launched (formatted yyyyMMddHHmmss in UTC time).  # noqa: E501

        :param expiration_date: The expiration_date of this PrivateInvitationSchema.  # noqa: E501
        :type: datetime
        """

        self._expiration_date = expiration_date

    @property
    def registration_count(self):
        """Gets the registration_count of this PrivateInvitationSchema.  # noqa: E501

        The count of registrations for this invitation  # noqa: E501

        :return: The registration_count of this PrivateInvitationSchema.  # noqa: E501
        :rtype: int
        """
        return self._registration_count

    @registration_count.setter
    def registration_count(self, registration_count):
        """Sets the registration_count of this PrivateInvitationSchema.

        The count of registrations for this invitation  # noqa: E501

        :param registration_count: The registration_count of this PrivateInvitationSchema.  # noqa: E501
        :type: int
        """

        self._registration_count = registration_count

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
        if issubclass(PrivateInvitationSchema, dict):
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
        if not isinstance(other, PrivateInvitationSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
