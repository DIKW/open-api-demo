import connexion
import six

from swagger_server.models.huishouden import Huishouden  # noqa: E501
from swagger_server.models.toets_resultaat_lokale_binding import ToetsResultaatLokaleBinding  # noqa: E501
from swagger_server.models.toets_resultaat_met_kale_huur import ToetsResultaatMetKaleHuur  # noqa: E501
from swagger_server.models.toets_resultaat_segmenten import ToetsResultaatSegmenten  # noqa: E501
from swagger_server.models.woonduren_inner import WoondurenInner  # noqa: E501
from swagger_server import util


def aedes_verhuurtoets_lokale_bindings_toets_post(body):  # noqa: E501
    """Toetst woonduur volgens lokaal geldende toetsingskader

     # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: ToetsResultaatLokaleBinding
    """
    if connexion.request.is_json:
        body = [WoondurenInner.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def aedes_verhuurtoets_passendheidstoets_bri_met_kale_huur_post(body):  # noqa: E501
    """Toetst kale huur volgens het geldende nationale toetsingskader

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ToetsResultaatMetKaleHuur
    """
    if connexion.request.is_json:
        body = Huishouden.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def aedes_verhuurtoets_passendheidstoets_bri_segmenten_post(body):  # noqa: E501
    """Toetst verhuursegmenten van huurder(s) volgens het geldende nationale toetsingskader

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: ToetsResultaatSegmenten
    """
    if connexion.request.is_json:
        body = Huishouden.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
