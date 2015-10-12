"""Checks the Harmonizome's gene entity API endpoint.
"""


import json
import requests

from hyperion.healthcheck import HealthCheck
import hyperion.notifier as notifier


class CheckGeneEndpoint(HealthCheck):

    email = 'gregory.gundersen@mssm.edu'
    url = 'http://amp.pharm.mssm.edu/Harmonizome/api/1.0/gene/STAT3'
    subject = 'Error with the Harmonizome'
    message = 'The /api/1.0/gene/STAT3 endpoint is down.'

    def __init__(self):
        CHECK_EVERY_SECS = 3600
        super(self.__class__, self).__init__(CHECK_EVERY_SECS)
        self.name = 'STAT 3 endpoint'

    def is_healthy(self):
        data = requests.get(self.url)
        data = json.loads(data.text)
        if not data['symbol'] or data['symbol'] != 'STAT3':
            return False
        return True

    def on_fail(self):
        notifier.send(self.email, self.subject, self.message)
