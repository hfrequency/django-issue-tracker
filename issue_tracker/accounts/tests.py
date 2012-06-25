from django.utils import unittest
from django.test.client import Client

class AccountTest(unittest.TestCase):
    def setUp(self):
        print("setting up account tests")
        self.client = Client()

    def test_login(self):
        print("calling test_login")
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

