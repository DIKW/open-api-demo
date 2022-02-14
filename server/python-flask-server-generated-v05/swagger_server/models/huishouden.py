# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.inkomen import Inkomen  # noqa: F401,E501
from swagger_server import util


class Huishouden(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, inkomens: List[Inkomen]=None, inkomens_ondertekend: List[str]=None, controleer_handtekening: bool=False, aantal_meeverhuizende_kinderen: int=None, kale_huur: int=None):  # noqa: E501
        """Huishouden - a model defined in Swagger

        :param inkomens: The inkomens of this Huishouden.  # noqa: E501
        :type inkomens: List[Inkomen]
        :param inkomens_ondertekend: The inkomens_ondertekend of this Huishouden.  # noqa: E501
        :type inkomens_ondertekend: List[str]
        :param controleer_handtekening: The controleer_handtekening of this Huishouden.  # noqa: E501
        :type controleer_handtekening: bool
        :param aantal_meeverhuizende_kinderen: The aantal_meeverhuizende_kinderen of this Huishouden.  # noqa: E501
        :type aantal_meeverhuizende_kinderen: int
        :param kale_huur: The kale_huur of this Huishouden.  # noqa: E501
        :type kale_huur: int
        """
        self.swagger_types = {
            'inkomens': List[Inkomen],
            'inkomens_ondertekend': List[str],
            'controleer_handtekening': bool,
            'aantal_meeverhuizende_kinderen': int,
            'kale_huur': int
        }

        self.attribute_map = {
            'inkomens': 'inkomens',
            'inkomens_ondertekend': 'inkomensOndertekend',
            'controleer_handtekening': 'controleerHandtekening',
            'aantal_meeverhuizende_kinderen': 'aantalMeeverhuizendeKinderen',
            'kale_huur': 'kaleHuur'
        }
        self._inkomens = inkomens
        self._inkomens_ondertekend = inkomens_ondertekend
        self._controleer_handtekening = controleer_handtekening
        self._aantal_meeverhuizende_kinderen = aantal_meeverhuizende_kinderen
        self._kale_huur = kale_huur

    @classmethod
    def from_dict(cls, dikt) -> 'Huishouden':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The huishouden of this Huishouden.  # noqa: E501
        :rtype: Huishouden
        """
        return util.deserialize_model(dikt, cls)

    @property
    def inkomens(self) -> List[Inkomen]:
        """Gets the inkomens of this Huishouden.


        :return: The inkomens of this Huishouden.
        :rtype: List[Inkomen]
        """
        return self._inkomens

    @inkomens.setter
    def inkomens(self, inkomens: List[Inkomen]):
        """Sets the inkomens of this Huishouden.


        :param inkomens: The inkomens of this Huishouden.
        :type inkomens: List[Inkomen]
        """

        self._inkomens = inkomens

    @property
    def inkomens_ondertekend(self) -> List[str]:
        """Gets the inkomens_ondertekend of this Huishouden.


        :return: The inkomens_ondertekend of this Huishouden.
        :rtype: List[str]
        """
        return self._inkomens_ondertekend

    @inkomens_ondertekend.setter
    def inkomens_ondertekend(self, inkomens_ondertekend: List[str]):
        """Sets the inkomens_ondertekend of this Huishouden.


        :param inkomens_ondertekend: The inkomens_ondertekend of this Huishouden.
        :type inkomens_ondertekend: List[str]
        """

        self._inkomens_ondertekend = inkomens_ondertekend

    @property
    def controleer_handtekening(self) -> bool:
        """Gets the controleer_handtekening of this Huishouden.


        :return: The controleer_handtekening of this Huishouden.
        :rtype: bool
        """
        return self._controleer_handtekening

    @controleer_handtekening.setter
    def controleer_handtekening(self, controleer_handtekening: bool):
        """Sets the controleer_handtekening of this Huishouden.


        :param controleer_handtekening: The controleer_handtekening of this Huishouden.
        :type controleer_handtekening: bool
        """

        self._controleer_handtekening = controleer_handtekening

    @property
    def aantal_meeverhuizende_kinderen(self) -> int:
        """Gets the aantal_meeverhuizende_kinderen of this Huishouden.


        :return: The aantal_meeverhuizende_kinderen of this Huishouden.
        :rtype: int
        """
        return self._aantal_meeverhuizende_kinderen

    @aantal_meeverhuizende_kinderen.setter
    def aantal_meeverhuizende_kinderen(self, aantal_meeverhuizende_kinderen: int):
        """Sets the aantal_meeverhuizende_kinderen of this Huishouden.


        :param aantal_meeverhuizende_kinderen: The aantal_meeverhuizende_kinderen of this Huishouden.
        :type aantal_meeverhuizende_kinderen: int
        """

        self._aantal_meeverhuizende_kinderen = aantal_meeverhuizende_kinderen

    @property
    def kale_huur(self) -> int:
        """Gets the kale_huur of this Huishouden.


        :return: The kale_huur of this Huishouden.
        :rtype: int
        """
        return self._kale_huur

    @kale_huur.setter
    def kale_huur(self, kale_huur: int):
        """Sets the kale_huur of this Huishouden.


        :param kale_huur: The kale_huur of this Huishouden.
        :type kale_huur: int
        """

        self._kale_huur = kale_huur