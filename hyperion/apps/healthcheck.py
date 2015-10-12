"""Abstract class to which all health check objects must adhere.
"""


from abc import ABCMeta, abstractmethod, abstractproperty


class HealthCheck(object):
    __metaclass__ = ABCMeta

    def __init__(self, interval_secs, time_passed):
        self.interval_secs = interval_secs
        self.time_passed = time_passed

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