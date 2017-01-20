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


class SearchQuery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SearchQuery - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'key': 'str',
            'value': 'str',
            'matching_method': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'value': 'value',
            'matching_method': 'matchingMethod'
        }

        self._key = None
        self._value = None
        self._matching_method = None

    @property
    def key(self):
        """
        Gets the key of this SearchQuery.
        The entity facet (key) by which to search.  Valid keys are any property keys returned by the JSON representation of the entity.  Examples are 'creatorId', 'name', etc.  The following special key keywords are also valid:  'tags' performs a search on entity tags, 'tagpath' performs a hierarchical search on tags, with  periods (.) as path level separators.  'freetext' performs a free text search across many fields of the entity

        :return: The key of this SearchQuery.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this SearchQuery.
        The entity facet (key) by which to search.  Valid keys are any property keys returned by the JSON representation of the entity.  Examples are 'creatorId', 'name', etc.  The following special key keywords are also valid:  'tags' performs a search on entity tags, 'tagpath' performs a hierarchical search on tags, with  periods (.) as path level separators.  'freetext' performs a free text search across many fields of the entity

        :param key: The key of this SearchQuery.
        :type: str
        """
        self._key = key

    @property
    def value(self):
        """
        Gets the value of this SearchQuery.
        The entity facet value for which to search

        :return: The value of this SearchQuery.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SearchQuery.
        The entity facet value for which to search

        :param value: The value of this SearchQuery.
        :type: str
        """
        self._value = value

    @property
    def matching_method(self):
        """
        Gets the matching_method of this SearchQuery.
        The method by which search matching is performed.  Default: CONTAINS

        :return: The matching_method of this SearchQuery.
        :rtype: str
        """
        return self._matching_method

    @matching_method.setter
    def matching_method(self, matching_method):
        """
        Sets the matching_method of this SearchQuery.
        The method by which search matching is performed.  Default: CONTAINS

        :param matching_method: The matching_method of this SearchQuery.
        :type: str
        """
        allowed_values = ["CONTAINS", "STARTSWITH", "EXACT", "TAGPATH"]
        if matching_method not in allowed_values:
            raise ValueError(
                "Invalid value for `matching_method`, must be one of {0}"
                .format(allowed_values)
            )
        self._matching_method = matching_method

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

