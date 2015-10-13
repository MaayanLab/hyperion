"""Health checks for the L1000CDS2.
"""


from hyperion import config
import hyperion.tester as tester
from hyperion.apps.paea.checkindexpage import CheckIndexPage


APP_NAME = 'paea'
EMAIL = config.get('paea', 'email')


tester.register_health_check(APP_NAME, CheckIndexPage(EMAIL))