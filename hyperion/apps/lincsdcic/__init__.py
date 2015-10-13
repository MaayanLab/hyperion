"""Health checks for the Harmonizome.
"""


from hyperion import config
import hyperion.tester as tester
from hyperion.apps.lincsdcic.checkindexpage import CheckIndexPage


APP_NAME = 'lincsdcic'
EMAIL = config.get('lincsdcic', 'email')


tester.register_health_check(APP_NAME, CheckIndexPage(EMAIL))