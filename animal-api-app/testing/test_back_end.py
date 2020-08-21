import requests 
import unittest

from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from applications import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Testing if homepage is accessible
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_animalpage_view(self):
        """
        Testing if the animal page is accessible
        """
        with patch('requests.get') as g:
            with patch('requests.post') as p:
                g.return_value.text = "Dog"
                p.return_value.text = "Woof!"

                response = self.client.get(url_for('animal'))
                self.assertIn(b'Dog',response.data)
                self.assertIn(b'Woof!',response.data)
                self.assertEqual(response.status_code, 200)
