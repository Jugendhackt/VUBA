import connexion
import six

from openapi_server.models.bike_ret import BikeRet  # noqa: E501
from openapi_server.models.coordinates import Coordinates  # noqa: E501
from openapi_server import util


def get_bikes_internal(coordinates=None, limit=None):  # noqa: E501
    """Searches for Bikes at a given Loaction

     # noqa: E501

    :param coordinates: coordinates to search at
    :type coordinates: dict | bytes
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: BikeRet
    """
    if connexion.request.is_json:
        coordinates = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
