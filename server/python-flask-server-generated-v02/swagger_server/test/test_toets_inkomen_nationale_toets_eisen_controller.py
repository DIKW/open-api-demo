# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.huishouden import Huishouden  # noqa: E501
from swagger_server.models.toets_resultaat import ToetsResultaat  # noqa: E501
from swagger_server.test import BaseTestCase


class TestToetsInkomenNationaleToetsEisenController(BaseTestCase):
    """ToetsInkomenNationaleToetsEisenController integration test stubs"""

    def test_huurder_nationale_inkomenstoets_post(self):
        """Test case for huurder_nationale_inkomenstoets_post

        Toetst inkomen van huurder volgens de geldende nationale toetsingskader
        """
        body = Huishouden()
        response = self.client.open(
            '//huurder/nationale_inkomenstoets/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
