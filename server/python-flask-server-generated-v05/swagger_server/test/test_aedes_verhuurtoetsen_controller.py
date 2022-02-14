# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.huishouden import Huishouden  # noqa: E501
from swagger_server.models.toets_resultaat_lokale_binding import ToetsResultaatLokaleBinding  # noqa: E501
from swagger_server.models.toets_resultaat_met_kale_huur import ToetsResultaatMetKaleHuur  # noqa: E501
from swagger_server.models.toets_resultaat_segmenten import ToetsResultaatSegmenten  # noqa: E501
from swagger_server.models.woonduren_inner import WoondurenInner  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAEDESVerhuurtoetsenController(BaseTestCase):
    """AEDESVerhuurtoetsenController integration test stubs"""

    def test_aedes_verhuurtoets_lokale_bindings_toets_post(self):
        """Test case for aedes_verhuurtoets_lokale_bindings_toets_post

        Toetst woonduur volgens lokaal geldende toetsingskader
        """
        body = [WoondurenInner()]
        response = self.client.open(
            '//aedes/verhuurtoets/lokale-bindings-toets/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_aedes_verhuurtoets_passendheidstoets_bri_met_kale_huur_post(self):
        """Test case for aedes_verhuurtoets_passendheidstoets_bri_met_kale_huur_post

        Toetst kale huur volgens het geldende nationale toetsingskader
        """
        body = Huishouden()
        response = self.client.open(
            '//aedes/verhuurtoets/passendheidstoets-bri-met-kale-huur/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_aedes_verhuurtoets_passendheidstoets_bri_segmenten_post(self):
        """Test case for aedes_verhuurtoets_passendheidstoets_bri_segmenten_post

        Toetst verhuursegmenten van huurder(s) volgens het geldende nationale toetsingskader
        """
        body = Huishouden()
        response = self.client.open(
            '//aedes/verhuurtoets/passendheidstoets-bri-segmenten/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
