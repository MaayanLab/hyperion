"""Checks the Harmonizome's gene entity API endpoint.
"""


import requests

from hyperion.healthcheck import HealthCheck


class CheckIndexPage(HealthCheck):

    def __init__(self, url, subject, email, message='The index page is unresponsive', name='Index page'):
        self.url = url
        self.subject = subject
        self.message = message
        self.email = email
        self.name_ = name
        super(self.__class__, self).__init__()

    def is_healthy(self):
        data = requests.get(self.url)
        if data.status_code != 200:
            return False
        return True

    @property
    def name(self):
        return self.name_
