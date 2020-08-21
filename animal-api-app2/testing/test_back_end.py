import requests
import unittest

from flask import url_for
from flask_testing import TestCase

from applications import app

class TestBase(TestCase):

    def create_app(self):
        return app

class TestViews(TestBase):

    def test_animalpage_view(self):
        """
        Tests that the animal page is accessible
        """
        response = self.client.get(url_for('getAnimal'))
        self.assertEqual(response.status_code, 200)

    def test_noisepage_view(self):
        """
        Tests that the noise page is accessible
        """
        response = self.client.post(url_for('getNoise'))
        self.assertEqual(response.status_code, 200)

    def test_noisepage_dog(self):
        """
        Tests that when dog is sent, we get the result of Woof!
        """
        response = self.client.post(url_for('getNoise'), data="Dog")
        self.assertIn(b'Woof!', response.data)

    def test_noisepage_cat(self):
        """
        Tests that when cat is sent, we get the result of Meow!
        """
        response = self.client.post(url_for('getNoise'), data="Cat")
        self.assertIn(b'Meow!', response.data)


    def test_noisepage_cow(self):
        """
        Tests that when cow is sent, we get the result of Moo!
        """
        response = self.client.post(url_for('getNoise'), data="Cow")
        self.assertIn(b'Moo!', response.data)

    def test_noisepage_mouse(self):
        """
        Tests that when mouse is sent, we get the result of Squeak!
        """
        response = self.client.post(url_for('getNoise'), data="Mouse")
        self.assertIn(b'Squeak!', response.data)

    def test_noisepage_sheep(self):
        """
        Tests that when sheep is sent, we get the result of Baa!
        """
        response = self.client.post(url_for('getNoise'), data="Sheep")
        self.assertIn(b'Baa!', response.data)

    def test_noisepage_horse(self):
        """
        Tests that when horse is sent, we get the result of Neigh!
        """
        response = self.client.post(url_for('getNoise'), data="Horse")
        self.assertIn(b'Neigh!', response.data)
