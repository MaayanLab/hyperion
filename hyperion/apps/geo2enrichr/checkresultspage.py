"""Checks the Harmonizome's gene entity API endpoint.
"""


import requests

from hyperion.healthcheck import HealthCheck


class CheckResultsPage(HealthCheck):

    url = 'http://amp.pharm.mssm.edu/g2e/results/9124905f88'
    subject = 'Error with GEO2Enrichr'
    message = 'The results page is broken.'
    name = 'Results page'

    def __init__(self, email):
        self.email = email
        super(self.__class__, self).__init__()

    def is_healthy(self):
        data = requests.get(self.url)
        if data.status_code != 200:
            return False
        return True
