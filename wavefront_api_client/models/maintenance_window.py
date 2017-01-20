# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class MaintenanceWindow(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MaintenanceWindow - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'reason': 'str',
            'customer_id': 'str',
            'created_epoch_millis': 'int',
            'updated_epoch_millis': 'int',
            'updater_id': 'str',
            'creator_id': 'str',
            'title': 'str',
            'start_time_in_seconds': 'int',
            'end_time_in_seconds': 'int',
            'relevant_customer_tags': 'list[str]',
            'relevant_host_names': 'list[str]',
            'relevant_host_tags': 'list[str]',
            'relevant_host_tags_anded': 'bool',
            'host_tag_group_host_names_group_anded': 'bool',
            'event_name': 'str',
            'running_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'reason': 'reason',
            'customer_id': 'customerId',
            'created_epoch_millis': 'createdEpochMillis',
            'updated_epoch_millis': 'updatedEpochMillis',
            'updater_id': 'updaterId',
            'creator_id': 'creatorId',
            'title': 'title',
            'start_time_in_seconds': 'startTimeInSeconds',
            'end_time_in_seconds': 'endTimeInSeconds',
            'relevant_customer_tags': 'relevantCustomerTags',
            'relevant_host_names': 'relevantHostNames',
            'relevant_host_tags': 'relevantHostTags',
            'relevant_host_tags_anded': 'relevantHostTagsAnded',
            'host_tag_group_host_names_group_anded': 'hostTagGroupHostNamesGroupAnded',
            'event_name': 'eventName',
            'running_state': 'runningState'
        }

        self._id = None
        self._reason = None
        self._customer_id = None
        self._created_epoch_millis = None
        self._updated_epoch_millis = None
        self._updater_id = None
        self._creator_id = None
        self._title = None
        self._start_time_in_seconds = None
        self._end_time_in_seconds = None
        self._relevant_customer_tags = None
        self._relevant_host_names = None
        self._relevant_host_tags = None
        self._relevant_host_tags_anded = None
        self._host_tag_group_host_names_group_anded = None
        self._event_name = None
        self._running_state = None

    @property
    def id(self):
        """
        Gets the id of this MaintenanceWindow.


        :return: The id of this MaintenanceWindow.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MaintenanceWindow.


        :param id: The id of this MaintenanceWindow.
        :type: str
        """
        self._id = id

    @property
    def reason(self):
        """
        Gets the reason of this MaintenanceWindow.
        The purpose of this maintenance window

        :return: The reason of this MaintenanceWindow.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this MaintenanceWindow.
        The purpose of this maintenance window

        :param reason: The reason of this MaintenanceWindow.
        :type: str
        """
        self._reason = reason

    @property
    def customer_id(self):
        """
        Gets the customer_id of this MaintenanceWindow.


        :return: The customer_id of this MaintenanceWindow.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this MaintenanceWindow.


        :param customer_id: The customer_id of this MaintenanceWindow.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def created_epoch_millis(self):
        """
        Gets the created_epoch_millis of this MaintenanceWindow.


        :return: The created_epoch_millis of this MaintenanceWindow.
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """
        Sets the created_epoch_millis of this MaintenanceWindow.


        :param created_epoch_millis: The created_epoch_millis of this MaintenanceWindow.
        :type: int
        """
        self._created_epoch_millis = created_epoch_millis

    @property
    def updated_epoch_millis(self):
        """
        Gets the updated_epoch_millis of this MaintenanceWindow.


        :return: The updated_epoch_millis of this MaintenanceWindow.
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """
        Sets the updated_epoch_millis of this MaintenanceWindow.


        :param updated_epoch_millis: The updated_epoch_millis of this MaintenanceWindow.
        :type: int
        """
        self._updated_epoch_millis = updated_epoch_millis

    @property
    def updater_id(self):
        """
        Gets the updater_id of this MaintenanceWindow.


        :return: The updater_id of this MaintenanceWindow.
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """
        Sets the updater_id of this MaintenanceWindow.


        :param updater_id: The updater_id of this MaintenanceWindow.
        :type: str
        """
        self._updater_id = updater_id

    @property
    def creator_id(self):
        """
        Gets the creator_id of this MaintenanceWindow.


        :return: The creator_id of this MaintenanceWindow.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """
        Sets the creator_id of this MaintenanceWindow.


        :param creator_id: The creator_id of this MaintenanceWindow.
        :type: str
        """
        self._creator_id = creator_id

    @property
    def title(self):
        """
        Gets the title of this MaintenanceWindow.
        Title of this maintenance window

        :return: The title of this MaintenanceWindow.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this MaintenanceWindow.
        Title of this maintenance window

        :param title: The title of this MaintenanceWindow.
        :type: str
        """
        self._title = title

    @property
    def start_time_in_seconds(self):
        """
        Gets the start_time_in_seconds of this MaintenanceWindow.
        The time in epoch seconds when this maintenance window will start

        :return: The start_time_in_seconds of this MaintenanceWindow.
        :rtype: int
        """
        return self._start_time_in_seconds

    @start_time_in_seconds.setter
    def start_time_in_seconds(self, start_time_in_seconds):
        """
        Sets the start_time_in_seconds of this MaintenanceWindow.
        The time in epoch seconds when this maintenance window will start

        :param start_time_in_seconds: The start_time_in_seconds of this MaintenanceWindow.
        :type: int
        """
        self._start_time_in_seconds = start_time_in_seconds

    @property
    def end_time_in_seconds(self):
        """
        Gets the end_time_in_seconds of this MaintenanceWindow.
        The time in epoch seconds when this maintenance window will end

        :return: The end_time_in_seconds of this MaintenanceWindow.
        :rtype: int
        """
        return self._end_time_in_seconds

    @end_time_in_seconds.setter
    def end_time_in_seconds(self, end_time_in_seconds):
        """
        Sets the end_time_in_seconds of this MaintenanceWindow.
        The time in epoch seconds when this maintenance window will end

        :param end_time_in_seconds: The end_time_in_seconds of this MaintenanceWindow.
        :type: int
        """
        self._end_time_in_seconds = end_time_in_seconds

    @property
    def relevant_customer_tags(self):
        """
        Gets the relevant_customer_tags of this MaintenanceWindow.
        List of alert tags whose matching alerts will be put into maintenance because of this maintenance window

        :return: The relevant_customer_tags of this MaintenanceWindow.
        :rtype: list[str]
        """
        return self._relevant_customer_tags

    @relevant_customer_tags.setter
    def relevant_customer_tags(self, relevant_customer_tags):
        """
        Sets the relevant_customer_tags of this MaintenanceWindow.
        List of alert tags whose matching alerts will be put into maintenance because of this maintenance window

        :param relevant_customer_tags: The relevant_customer_tags of this MaintenanceWindow.
        :type: list[str]
        """
        self._relevant_customer_tags = relevant_customer_tags

    @property
    def relevant_host_names(self):
        """
        Gets the relevant_host_names of this MaintenanceWindow.
        List of source/host names that will be put into maintenance because of this maintenance window

        :return: The relevant_host_names of this MaintenanceWindow.
        :rtype: list[str]
        """
        return self._relevant_host_names

    @relevant_host_names.setter
    def relevant_host_names(self, relevant_host_names):
        """
        Sets the relevant_host_names of this MaintenanceWindow.
        List of source/host names that will be put into maintenance because of this maintenance window

        :param relevant_host_names: The relevant_host_names of this MaintenanceWindow.
        :type: list[str]
        """
        self._relevant_host_names = relevant_host_names

    @property
    def relevant_host_tags(self):
        """
        Gets the relevant_host_tags of this MaintenanceWindow.
        List of source/host tags whose matching sources/hosts will be put into maintenance because of this maintenance window

        :return: The relevant_host_tags of this MaintenanceWindow.
        :rtype: list[str]
        """
        return self._relevant_host_tags

    @relevant_host_tags.setter
    def relevant_host_tags(self, relevant_host_tags):
        """
        Sets the relevant_host_tags of this MaintenanceWindow.
        List of source/host tags whose matching sources/hosts will be put into maintenance because of this maintenance window

        :param relevant_host_tags: The relevant_host_tags of this MaintenanceWindow.
        :type: list[str]
        """
        self._relevant_host_tags = relevant_host_tags

    @property
    def relevant_host_tags_anded(self):
        """
        Gets the relevant_host_tags_anded of this MaintenanceWindow.
        Whether to AND source/host tags listed in relevantHostTags. If true, a source/host must contain all tags in order for the maintenance window to apply.  If false, the tags are OR'ed, and a source/host must contain one of the tags. Default: false

        :return: The relevant_host_tags_anded of this MaintenanceWindow.
        :rtype: bool
        """
        return self._relevant_host_tags_anded

    @relevant_host_tags_anded.setter
    def relevant_host_tags_anded(self, relevant_host_tags_anded):
        """
        Sets the relevant_host_tags_anded of this MaintenanceWindow.
        Whether to AND source/host tags listed in relevantHostTags. If true, a source/host must contain all tags in order for the maintenance window to apply.  If false, the tags are OR'ed, and a source/host must contain one of the tags. Default: false

        :param relevant_host_tags_anded: The relevant_host_tags_anded of this MaintenanceWindow.
        :type: bool
        """
        self._relevant_host_tags_anded = relevant_host_tags_anded

    @property
    def host_tag_group_host_names_group_anded(self):
        """
        Gets the host_tag_group_host_names_group_anded of this MaintenanceWindow.
        If true, a source/host must be in 'relevantHostNames' and have tags matching the specification formed by 'relevantHostTags' and 'relevantHostTagsAnded' in order for this maintenance window to apply. If false, a source/host must either be in 'relevantHostNames' or match 'relevantHostTags' and 'relevantHostTagsAnded'. Default: false

        :return: The host_tag_group_host_names_group_anded of this MaintenanceWindow.
        :rtype: bool
        """
        return self._host_tag_group_host_names_group_anded

    @host_tag_group_host_names_group_anded.setter
    def host_tag_group_host_names_group_anded(self, host_tag_group_host_names_group_anded):
        """
        Sets the host_tag_group_host_names_group_anded of this MaintenanceWindow.
        If true, a source/host must be in 'relevantHostNames' and have tags matching the specification formed by 'relevantHostTags' and 'relevantHostTagsAnded' in order for this maintenance window to apply. If false, a source/host must either be in 'relevantHostNames' or match 'relevantHostTags' and 'relevantHostTagsAnded'. Default: false

        :param host_tag_group_host_names_group_anded: The host_tag_group_host_names_group_anded of this MaintenanceWindow.
        :type: bool
        """
        self._host_tag_group_host_names_group_anded = host_tag_group_host_names_group_anded

    @property
    def event_name(self):
        """
        Gets the event_name of this MaintenanceWindow.
        The name of an event associated with the creation/update of this maintenance window

        :return: The event_name of this MaintenanceWindow.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this MaintenanceWindow.
        The name of an event associated with the creation/update of this maintenance window

        :param event_name: The event_name of this MaintenanceWindow.
        :type: str
        """
        self._event_name = event_name

    @property
    def running_state(self):
        """
        Gets the running_state of this MaintenanceWindow.


        :return: The running_state of this MaintenanceWindow.
        :rtype: str
        """
        return self._running_state

    @running_state.setter
    def running_state(self, running_state):
        """
        Sets the running_state of this MaintenanceWindow.


        :param running_state: The running_state of this MaintenanceWindow.
        :type: str
        """
        allowed_values = ["ONGOING", "PENDING", "ENDED"]
        if running_state not in allowed_values:
            raise ValueError(
                "Invalid value for `running_state`, must be one of {0}"
                .format(allowed_values)
            )
        self._running_state = running_state

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

