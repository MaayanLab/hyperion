"""Health checks for the L1000CDS2.
"""


from hyperion import config
import hyperion.tester as tester
from hyperion.apps.l1000cds2.checkindexpage import CheckIndexPage


APP_NAME = 'l1000cds2'
EMAIL = config.get('l1000cds2', 'email')


tester.register_health_check(APP_NAME, CheckIndexPage(EMAIL))