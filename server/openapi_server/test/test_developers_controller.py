# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.bike_ret import BikeRet  # noqa: E501
from openapi_server.models.coordinates import Coordinates  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDevelopersController(BaseTestCase):
    """DevelopersController integration test stubs"""

    def test_get_bikes_internal(self):
        """Test case for get_bikes_internal

        Searches for Bikes at a given Loaction
        """
        query_string = [('coordinates', Coordinates()),
                        ('limit', 50)]
        response = self.client.open(
            '/The_Minefighter/VUBA/1.0.0/getBikes',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
