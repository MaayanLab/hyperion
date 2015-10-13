"""Health checks for Enrichr.
"""


from hyperion import config
import hyperion.tester as tester
from hyperion.apps.harmonizome.checkindexpage import CheckIndexPage


APP_NAME = 'enrichr'
EMAIL = config.get('enrichr', 'email')


tester.register_health_check(APP_NAME, CheckIndexPage(EMAIL))