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


class ImportJobResultSchema(object):
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
        'job_id': 'str',
        'status': 'str',
        'message': 'str',
        'import_result': 'ImportResultSchema'
    }

    attribute_map = {
        'job_id': 'jobId',
        'status': 'status',
        'message': 'message',
        'import_result': 'importResult'
    }

    def __init__(self, job_id=None, status=None, message=None, import_result=None):  # noqa: E501
        """ImportJobResultSchema - a model defined in Swagger"""  # noqa: E501

        self._job_id = None
        self._status = None
        self._message = None
        self._import_result = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if import_result is not None:
            self.import_result = import_result

    @property
    def job_id(self):
        """Gets the job_id of this ImportJobResultSchema.  # noqa: E501


        :return: The job_id of this ImportJobResultSchema.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ImportJobResultSchema.


        :param job_id: The job_id of this ImportJobResultSchema.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def status(self):
        """Gets the status of this ImportJobResultSchema.  # noqa: E501


        :return: The status of this ImportJobResultSchema.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ImportJobResultSchema.


        :param status: The status of this ImportJobResultSchema.  # noqa: E501
        :type: str
        """
        allowed_values = ["RUNNING", "COMPLETE", "ERROR"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def message(self):
        """Gets the message of this ImportJobResultSchema.  # noqa: E501


        :return: The message of this ImportJobResultSchema.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ImportJobResultSchema.


        :param message: The message of this ImportJobResultSchema.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def import_result(self):
        """Gets the import_result of this ImportJobResultSchema.  # noqa: E501


        :return: The import_result of this ImportJobResultSchema.  # noqa: E501
        :rtype: ImportResultSchema
        """
        return self._import_result

    @import_result.setter
    def import_result(self, import_result):
        """Sets the import_result of this ImportJobResultSchema.


        :param import_result: The import_result of this ImportJobResultSchema.  # noqa: E501
        :type: ImportResultSchema
        """

        self._import_result = import_result

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
        if issubclass(ImportJobResultSchema, dict):
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
        if not isinstance(other, ImportJobResultSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
