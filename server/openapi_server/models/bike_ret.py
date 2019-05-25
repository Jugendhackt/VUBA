# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class BikeRet(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bikes=None):  # noqa: E501
        """BikeRet - a model defined in OpenAPI

        :param bikes: The bikes of this BikeRet.  # noqa: E501
        :type bikes: List[Bike]
        """
        self.openapi_types = {
            'bikes': List[Bike]
        }

        self.attribute_map = {
            'bikes': 'Bikes'
        }

        self._bikes = bikes

    @classmethod
    def from_dict(cls, dikt) -> 'BikeRet':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BikeRet of this BikeRet.  # noqa: E501
        :rtype: BikeRet
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bikes(self):
        """Gets the bikes of this BikeRet.


        :return: The bikes of this BikeRet.
        :rtype: List[Bike]
        """
        return self._bikes

    @bikes.setter
    def bikes(self, bikes):
        """Sets the bikes of this BikeRet.


        :param bikes: The bikes of this BikeRet.
        :type bikes: List[Bike]
        """
        if bikes is None:
            raise ValueError("Invalid value for `bikes`, must not be `None`")  # noqa: E501

        self._bikes = bikes
