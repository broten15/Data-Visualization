import unittest
from get_country_code import get_cc


class GetCcTestCase(unittest.TestCase):
    """Tests for get_country_code.py"""

    def test_get_cc(self):
        """Test that get_cc() gets the right code from COUNTRIES"""
        country_name = 'Canada'
        code = get_cc(country_name)
        
        self.assertEqual(code, 'ca')

unittest.main()