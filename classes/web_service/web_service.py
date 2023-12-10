import requests
from helpers.helpers import make_get_request


class WebService:
    def __init__(self, route, size):
        """ 
        class for getting data from random data api.
        """
        self.route = route
        self.size = size

    def set_route(self, val):
        self.route = val

    def set_size(self, val):
        self.size = val

    def get_data(self):
        """
        method which makes api get requests
        """
        try:
            url = 'https://random-data-api.com/api/v2/' + self.route
            if self.size > 1:
                url += '?size=' + str(self.size)
            response = make_get_request(url)
            return response
        except requests.exceptions.RequestException:
            return {}
