"""Checks the Harmonizome's gene entity API endpoint.
"""


import json
import requests

from hyperion.healthcheck import HealthCheck
import hyperion.notifier as notifier


class CheckSearch(HealthCheck):

    url = 'http://amp.pharm.mssm.edu/Harmonizome/search?q=STAT3'
    subject = 'Error with the Harmonizome'
    message = 'The search endpoint is down.'
    name = 'Search page'

    def __init__(self, email):
        self.email = email
        super(self.__class__, self).__init__()

    def is_healthy(self):
        data = requests.get(self.url)
        if not 'STAT3' in data.text:
            return False
        return True

    def on_fail(self):
        notifier.send(self.email, self.subject, self.message)
