from django.test import TestCase
from .utility import *


class TestUtilities(TestCase):

    def test_today(self):
        hoy = dt.now()
        self.assertEqual(hoy.day, return_today())
