# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.persoon import Persoon  # noqa: F401,E501
from swagger_server import util


class ToetsResultaatMetKaleHuur(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, personen: List[Persoon]=None, toets_resultaat: bool=None, tijdstempel: str=None, jwt: str=None):  # noqa: E501
        """ToetsResultaatMetKaleHuur - a model defined in Swagger

        :param personen: The personen of this ToetsResultaatMetKaleHuur.  # noqa: E501
        :type personen: List[Persoon]
        :param toets_resultaat: The toets_resultaat of this ToetsResultaatMetKaleHuur.  # noqa: E501
        :type toets_resultaat: bool
        :param tijdstempel: The tijdstempel of this ToetsResultaatMetKaleHuur.  # noqa: E501
        :type tijdstempel: str
        :param jwt: The jwt of this ToetsResultaatMetKaleHuur.  # noqa: E501
        :type jwt: str
        """
        self.swagger_types = {
            'personen': List[Persoon],
            'toets_resultaat': bool,
            'tijdstempel': str,
            'jwt': str
        }

        self.attribute_map = {
            'personen': 'personen',
            'toets_resultaat': 'toets-resultaat',
            'tijdstempel': 'tijdstempel',
            'jwt': 'jwt'
        }
        self._personen = personen
        self._toets_resultaat = toets_resultaat
        self._tijdstempel = tijdstempel
        self._jwt = jwt

    @classmethod
    def from_dict(cls, dikt) -> 'ToetsResultaatMetKaleHuur':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The toets-resultaat-met-kale-huur of this ToetsResultaatMetKaleHuur.  # noqa: E501
        :rtype: ToetsResultaatMetKaleHuur
        """
        return util.deserialize_model(dikt, cls)

    @property
    def personen(self) -> List[Persoon]:
        """Gets the personen of this ToetsResultaatMetKaleHuur.


        :return: The personen of this ToetsResultaatMetKaleHuur.
        :rtype: List[Persoon]
        """
        return self._personen

    @personen.setter
    def personen(self, personen: List[Persoon]):
        """Sets the personen of this ToetsResultaatMetKaleHuur.


        :param personen: The personen of this ToetsResultaatMetKaleHuur.
        :type personen: List[Persoon]
        """

        self._personen = personen

    @property
    def toets_resultaat(self) -> bool:
        """Gets the toets_resultaat of this ToetsResultaatMetKaleHuur.


        :return: The toets_resultaat of this ToetsResultaatMetKaleHuur.
        :rtype: bool
        """
        return self._toets_resultaat

    @toets_resultaat.setter
    def toets_resultaat(self, toets_resultaat: bool):
        """Sets the toets_resultaat of this ToetsResultaatMetKaleHuur.


        :param toets_resultaat: The toets_resultaat of this ToetsResultaatMetKaleHuur.
        :type toets_resultaat: bool
        """

        self._toets_resultaat = toets_resultaat

    @property
    def tijdstempel(self) -> str:
        """Gets the tijdstempel of this ToetsResultaatMetKaleHuur.


        :return: The tijdstempel of this ToetsResultaatMetKaleHuur.
        :rtype: str
        """
        return self._tijdstempel

    @tijdstempel.setter
    def tijdstempel(self, tijdstempel: str):
        """Sets the tijdstempel of this ToetsResultaatMetKaleHuur.


        :param tijdstempel: The tijdstempel of this ToetsResultaatMetKaleHuur.
        :type tijdstempel: str
        """

        self._tijdstempel = tijdstempel

    @property
    def jwt(self) -> str:
        """Gets the jwt of this ToetsResultaatMetKaleHuur.


        :return: The jwt of this ToetsResultaatMetKaleHuur.
        :rtype: str
        """
        return self._jwt

    @jwt.setter
    def jwt(self, jwt: str):
        """Sets the jwt of this ToetsResultaatMetKaleHuur.


        :param jwt: The jwt of this ToetsResultaatMetKaleHuur.
        :type jwt: str
        """

        self._jwt = jwt
