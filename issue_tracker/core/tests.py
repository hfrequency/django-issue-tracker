from django.utils import unittest
from django.test.client import Client
import logging

log = logging.getLogger('simple') 

class CoreTest(unittest.TestCase):
    def setUp(self):
        log.debug("setting up core tests")
        self.client = Client()

    def test_get_responses(self):
        log.debug("calling test_get_responses")
        # c.post('/login/', {'name': 'fred', 'passwd': 'secret'})
        response = self.client.post('/register/')
        self.assertEqual(response.status_code, 200)

    def test_redirect_project(self):
        # We're not logged in, so this page should redirect.
        log.debug("calling test_redirect_project")
        response = self.client.post('/projects/')
        self.assertGreaterEqual(response.status_code, 300)

    def test_redirect_issues(self):
        # We're not logged in, so this page should redirect.
        log.debug("calling test_redirect_issues")
        response = self.client.post('/issues/0')
        self.assertGreaterEqual(response.status_code, 300)

    def test_redirect_comments(self):
        log.debug("calling test_redirect_comments")
        response = self.client.post('/comments/0/0')
        self.assertGreaterEqual(response.status_code, 300)
         
