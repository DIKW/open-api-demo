# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class HuishoudenBrp(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, voornamen: str=None, voorvoegsel_geslachtsnaam: str=None, geslachtsnaam: str=None, voorvoegsel_partnernaam: str=None, partnernaam: str=None, huisnummer: str=None, huisletter: str=None, huisnummer_toevoeging: str=None, huisnummer_aanduiding: str=None, postcode: str=None, geboortedatum: str=None):  # noqa: E501
        """HuishoudenBrp - a model defined in Swagger

        :param voornamen: The voornamen of this HuishoudenBrp.  # noqa: E501
        :type voornamen: str
        :param voorvoegsel_geslachtsnaam: The voorvoegsel_geslachtsnaam of this HuishoudenBrp.  # noqa: E501
        :type voorvoegsel_geslachtsnaam: str
        :param geslachtsnaam: The geslachtsnaam of this HuishoudenBrp.  # noqa: E501
        :type geslachtsnaam: str
        :param voorvoegsel_partnernaam: The voorvoegsel_partnernaam of this HuishoudenBrp.  # noqa: E501
        :type voorvoegsel_partnernaam: str
        :param partnernaam: The partnernaam of this HuishoudenBrp.  # noqa: E501
        :type partnernaam: str
        :param huisnummer: The huisnummer of this HuishoudenBrp.  # noqa: E501
        :type huisnummer: str
        :param huisletter: The huisletter of this HuishoudenBrp.  # noqa: E501
        :type huisletter: str
        :param huisnummer_toevoeging: The huisnummer_toevoeging of this HuishoudenBrp.  # noqa: E501
        :type huisnummer_toevoeging: str
        :param huisnummer_aanduiding: The huisnummer_aanduiding of this HuishoudenBrp.  # noqa: E501
        :type huisnummer_aanduiding: str
        :param postcode: The postcode of this HuishoudenBrp.  # noqa: E501
        :type postcode: str
        :param geboortedatum: The geboortedatum of this HuishoudenBrp.  # noqa: E501
        :type geboortedatum: str
        """
        self.swagger_types = {
            'voornamen': str,
            'voorvoegsel_geslachtsnaam': str,
            'geslachtsnaam': str,
            'voorvoegsel_partnernaam': str,
            'partnernaam': str,
            'huisnummer': str,
            'huisletter': str,
            'huisnummer_toevoeging': str,
            'huisnummer_aanduiding': str,
            'postcode': str,
            'geboortedatum': str
        }

        self.attribute_map = {
            'voornamen': 'voornamen',
            'voorvoegsel_geslachtsnaam': 'voorvoegselGeslachtsnaam',
            'geslachtsnaam': 'geslachtsnaam',
            'voorvoegsel_partnernaam': 'voorvoegselPartnernaam',
            'partnernaam': 'partnernaam',
            'huisnummer': 'huisnummer',
            'huisletter': 'huisletter',
            'huisnummer_toevoeging': 'huisnummerToevoeging',
            'huisnummer_aanduiding': 'huisnummerAanduiding',
            'postcode': 'postcode',
            'geboortedatum': 'geboortedatum'
        }
        self._voornamen = voornamen
        self._voorvoegsel_geslachtsnaam = voorvoegsel_geslachtsnaam
        self._geslachtsnaam = geslachtsnaam
        self._voorvoegsel_partnernaam = voorvoegsel_partnernaam
        self._partnernaam = partnernaam
        self._huisnummer = huisnummer
        self._huisletter = huisletter
        self._huisnummer_toevoeging = huisnummer_toevoeging
        self._huisnummer_aanduiding = huisnummer_aanduiding
        self._postcode = postcode
        self._geboortedatum = geboortedatum

    @classmethod
    def from_dict(cls, dikt) -> 'HuishoudenBrp':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The huishouden_brp of this HuishoudenBrp.  # noqa: E501
        :rtype: HuishoudenBrp
        """
        return util.deserialize_model(dikt, cls)

    @property
    def voornamen(self) -> str:
        """Gets the voornamen of this HuishoudenBrp.


        :return: The voornamen of this HuishoudenBrp.
        :rtype: str
        """
        return self._voornamen

    @voornamen.setter
    def voornamen(self, voornamen: str):
        """Sets the voornamen of this HuishoudenBrp.


        :param voornamen: The voornamen of this HuishoudenBrp.
        :type voornamen: str
        """

        self._voornamen = voornamen

    @property
    def voorvoegsel_geslachtsnaam(self) -> str:
        """Gets the voorvoegsel_geslachtsnaam of this HuishoudenBrp.


        :return: The voorvoegsel_geslachtsnaam of this HuishoudenBrp.
        :rtype: str
        """
        return self._voorvoegsel_geslachtsnaam

    @voorvoegsel_geslachtsnaam.setter
    def voorvoegsel_geslachtsnaam(self, voorvoegsel_geslachtsnaam: str):
        """Sets the voorvoegsel_geslachtsnaam of this HuishoudenBrp.


        :param voorvoegsel_geslachtsnaam: The voorvoegsel_geslachtsnaam of this HuishoudenBrp.
        :type voorvoegsel_geslachtsnaam: str
        """

        self._voorvoegsel_geslachtsnaam = voorvoegsel_geslachtsnaam

    @property
    def geslachtsnaam(self) -> str:
        """Gets the geslachtsnaam of this HuishoudenBrp.


        :return: The geslachtsnaam of this HuishoudenBrp.
        :rtype: str
        """
        return self._geslachtsnaam

    @geslachtsnaam.setter
    def geslachtsnaam(self, geslachtsnaam: str):
        """Sets the geslachtsnaam of this HuishoudenBrp.


        :param geslachtsnaam: The geslachtsnaam of this HuishoudenBrp.
        :type geslachtsnaam: str
        """

        self._geslachtsnaam = geslachtsnaam

    @property
    def voorvoegsel_partnernaam(self) -> str:
        """Gets the voorvoegsel_partnernaam of this HuishoudenBrp.


        :return: The voorvoegsel_partnernaam of this HuishoudenBrp.
        :rtype: str
        """
        return self._voorvoegsel_partnernaam

    @voorvoegsel_partnernaam.setter
    def voorvoegsel_partnernaam(self, voorvoegsel_partnernaam: str):
        """Sets the voorvoegsel_partnernaam of this HuishoudenBrp.


        :param voorvoegsel_partnernaam: The voorvoegsel_partnernaam of this HuishoudenBrp.
        :type voorvoegsel_partnernaam: str
        """

        self._voorvoegsel_partnernaam = voorvoegsel_partnernaam

    @property
    def partnernaam(self) -> str:
        """Gets the partnernaam of this HuishoudenBrp.


        :return: The partnernaam of this HuishoudenBrp.
        :rtype: str
        """
        return self._partnernaam

    @partnernaam.setter
    def partnernaam(self, partnernaam: str):
        """Sets the partnernaam of this HuishoudenBrp.


        :param partnernaam: The partnernaam of this HuishoudenBrp.
        :type partnernaam: str
        """

        self._partnernaam = partnernaam

    @property
    def huisnummer(self) -> str:
        """Gets the huisnummer of this HuishoudenBrp.


        :return: The huisnummer of this HuishoudenBrp.
        :rtype: str
        """
        return self._huisnummer

    @huisnummer.setter
    def huisnummer(self, huisnummer: str):
        """Sets the huisnummer of this HuishoudenBrp.


        :param huisnummer: The huisnummer of this HuishoudenBrp.
        :type huisnummer: str
        """

        self._huisnummer = huisnummer

    @property
    def huisletter(self) -> str:
        """Gets the huisletter of this HuishoudenBrp.


        :return: The huisletter of this HuishoudenBrp.
        :rtype: str
        """
        return self._huisletter

    @huisletter.setter
    def huisletter(self, huisletter: str):
        """Sets the huisletter of this HuishoudenBrp.


        :param huisletter: The huisletter of this HuishoudenBrp.
        :type huisletter: str
        """

        self._huisletter = huisletter

    @property
    def huisnummer_toevoeging(self) -> str:
        """Gets the huisnummer_toevoeging of this HuishoudenBrp.


        :return: The huisnummer_toevoeging of this HuishoudenBrp.
        :rtype: str
        """
        return self._huisnummer_toevoeging

    @huisnummer_toevoeging.setter
    def huisnummer_toevoeging(self, huisnummer_toevoeging: str):
        """Sets the huisnummer_toevoeging of this HuishoudenBrp.


        :param huisnummer_toevoeging: The huisnummer_toevoeging of this HuishoudenBrp.
        :type huisnummer_toevoeging: str
        """

        self._huisnummer_toevoeging = huisnummer_toevoeging

    @property
    def huisnummer_aanduiding(self) -> str:
        """Gets the huisnummer_aanduiding of this HuishoudenBrp.


        :return: The huisnummer_aanduiding of this HuishoudenBrp.
        :rtype: str
        """
        return self._huisnummer_aanduiding

    @huisnummer_aanduiding.setter
    def huisnummer_aanduiding(self, huisnummer_aanduiding: str):
        """Sets the huisnummer_aanduiding of this HuishoudenBrp.


        :param huisnummer_aanduiding: The huisnummer_aanduiding of this HuishoudenBrp.
        :type huisnummer_aanduiding: str
        """

        self._huisnummer_aanduiding = huisnummer_aanduiding

    @property
    def postcode(self) -> str:
        """Gets the postcode of this HuishoudenBrp.


        :return: The postcode of this HuishoudenBrp.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode: str):
        """Sets the postcode of this HuishoudenBrp.


        :param postcode: The postcode of this HuishoudenBrp.
        :type postcode: str
        """

        self._postcode = postcode

    @property
    def geboortedatum(self) -> str:
        """Gets the geboortedatum of this HuishoudenBrp.


        :return: The geboortedatum of this HuishoudenBrp.
        :rtype: str
        """
        return self._geboortedatum

    @geboortedatum.setter
    def geboortedatum(self, geboortedatum: str):
        """Sets the geboortedatum of this HuishoudenBrp.


        :param geboortedatum: The geboortedatum of this HuishoudenBrp.
        :type geboortedatum: str
        """

        self._geboortedatum = geboortedatum
