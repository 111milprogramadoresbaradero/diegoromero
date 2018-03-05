# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.butaca import Butaca
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_leer_get(self):
        """
        Test case for leer_get

        Lee toda la planta y retorna un html
        """
        query_string = [('accion', 'accion_example'),
                        ('fila', 56),
                        ('columna', 'columna_example')]
        response = self.client.open('/v1/leer',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_menu_get(self):
        """
        Test case for menu_get

        Retorna un menu de opciones para el usuario
        """
        response = self.client.open('/v1/menu',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_planta_cancelar(self):
        """
        Test case for planta_cancelar

        Cancela la butaca ubicada en columna y fila. Retorna -1 si la butaca no pudo ser cancelada y 0 en caso de que se haya cancelado
        """
        query_string = [('fila', 56),
                        ('columna', 'columna_example')]
        response = self.client.open('/v1/planta/cancelar',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_planta_leer_get(self):
        """
        Test case for planta_leer_get

        Retorna el estado de la planta
        """
        query_string = [('fila', 56),
                        ('columna', 'columna_example')]
        response = self.client.open('/v1/planta/leer',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_planta_vender_get(self):
        """
        Test case for planta_vender_get

        Vende la butaca ubicada en columna y fila. Retorna -1 si la butaca no pudo ser vendida y 0 en caso de que se haya vendido
        """
        query_string = [('fila', 56),
                        ('columna', 'columna_example')]
        response = self.client.open('/v1/planta/vender',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
