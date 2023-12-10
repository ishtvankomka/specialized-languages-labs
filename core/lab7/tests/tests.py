import unittest
import requests
from helpers.helpers import make_get_request, wrap_in_list


class WebServiceTest(unittest.TestCase):
    def test_request_exception(self):
        with self.assertRaises(requests.exceptions.RequestException):
            make_get_request('https://random-data-api.com/api/v2/pankakes')

    def test_wrap_in_list_obj(self):
        wrapped = wrap_in_list({})
        self.assertEqual(wrapped, [{}])

    def test_wrap_in_list_arr(self):
        wrapped = wrap_in_list([{}, {}])
        self.assertEqual(wrapped, [{}, {}])

    def test_web_service(self):
        self.test_request_exception()
        self.test_wrap_in_list_obj()
        self.test_wrap_in_list_arr()