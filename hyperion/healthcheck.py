"""Abstract class to which all health check objects must adhere.
"""


from abc import ABCMeta, abstractmethod

from hyperion import config


DEBUG = config.getboolean('DEFAULT', 'debug')
MIN_INTERVAL = 1 if DEBUG else 60


class HealthCheck(object):
    __metaclass__ = ABCMeta

    def __init__(self, interval_secs):
        if interval_secs < MIN_INTERVAL:
            raise ValueError('Health checks cannot be performed more than once per minute.')

        self.interval_secs = interval_secs
        self.time_passed = 0
        self.already_notified = False

    @abstractmethod
    def is_healthy(self):
        pass

    @abstractmethod
    def on_fail(self):
        pass

    def interval_secs(self):
        return self.interval_secs

    def time_passed(self):
        return self.time_passed

    def reset(self):
        self.time_passed = 0