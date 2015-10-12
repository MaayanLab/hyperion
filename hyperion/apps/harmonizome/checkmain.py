
from hyperion.apps.healthcheck import HealthCheck

class CheckMain(HealthCheck):

    def __init__(self, name, interval_secs):
        super(self.__class__, self).__init__(interval_secs, 0)
        self.name = name

    def is_healthy(self):
        print('checking ' + self.name)
        return True

    def on_fail(self):
        print('failed')