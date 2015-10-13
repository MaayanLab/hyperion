"""Checks the Harmonizome's gene entity API endpoint.
"""


import json
import requests

from hyperion.healthcheck import HealthCheck
import hyperion.notifier as notifier


class CheckGeneEndpoint(HealthCheck):

    url = 'http://amp.pharm.mssm.edu/Harmonizome/api/1.0/gene/STAT3'
    subject = 'Error with the Harmonizome'
    message = 'The endpoint /api/1.0/gene/STAT3 is down.'
    name = 'STAT3 endpoint'

    def __init__(self, email):
        self.email = email
        super(self.__class__, self).__init__()

    def is_healthy(self):
        data = requests.get(self.url)
        data = json.loads(data.text)
        if not data['symbol'] or data['symbol'] != 'STAT3':
            return False
        return True
