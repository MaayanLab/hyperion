"""Checks the Harmonizome's gene entity API endpoint.
"""


import requests

from hyperion.healthcheck import HealthCheck
import hyperion.notifier as notifier


class CheckIndexPage(HealthCheck):

    url = 'http://amp.pharm.mssm.edu/Harmonizome'
    subject = 'Error with the Harmonizome'
    message = 'The index page is unresponsive.'
    name = 'Index page'

    def __init__(self, email):
        CHECK_EVERY_SECS = 3600
        self.email = email
        super(self.__class__, self).__init__(CHECK_EVERY_SECS)

    def is_healthy(self):
        data = requests.get(self.url)
        if data.status_code != 200 or not 'harmonizome' in data.text:
            return False
        return True

    def on_fail(self):
        notifier.send(self.email, self.subject, self.message)
