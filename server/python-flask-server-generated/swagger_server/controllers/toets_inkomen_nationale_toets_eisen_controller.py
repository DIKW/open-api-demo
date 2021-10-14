import connexion
import six

from swagger_server.models.huishouden import Huishouden  # noqa: E501
from swagger_server.models.toets_resultaat import ToetsResultaat  # noqa: E501
from swagger_server import util


def huurder_nationale_inkomenstoets_post(body):  # noqa: E501
    """Toetst inkomen van huurder volgens de geldende nationale toetsingskader

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ToetsResultaat
    """
    if connexion.request.is_json:
        body = Huishouden.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
