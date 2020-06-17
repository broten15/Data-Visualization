import unittest
import requests

class StatusCodeTestCase(unittest.TestCase):
    """Tests for populart_java_repos"""

    def test_status_code(self):
        """Tests to see if status code from url is 200"""
        url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
        r = requests.get(url)

        self.assertEqual(r.status_code, 200)
        
unittest.main()