"""
    Regionalatlas-API

    API zum [Regionalatlas Deutschland](https://regionalatlas.statistikportal.de/#) der statistischen Ämter des Bundes und der Länder.   Der Regionalatlas Deutschland der Statistischen Ämter des Bundes und der Länder visualisiert aktuell laut [statistischem Bundesamt](https://www.destatis.de/DE/Service/Statistik-Visualisiert/_inhalt.html) mehr als 160 Indikatoren aus 20 Themenbereichen für Bundesländer, Regierungsbezirke, Kreisfreie Städte und Landkreise. Grundlage des Regionalatlas ist die Regionaldatenbank Deutschland.    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""

import unittest

from deutschland.Regionalatlas.api.default_api import DefaultApi  # noqa: E501

from deutschland import Regionalatlas


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_query(self):
        """Test case for query

        query  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
