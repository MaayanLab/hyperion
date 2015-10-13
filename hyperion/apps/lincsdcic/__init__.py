"""Health checks for the LINCS DCIC website.
"""


from hyperion import config
import hyperion.tester as tester
from hyperion.checkindexpage import CheckIndexPage


APP_NAME = 'lincsdcic'
EMAIL = config.get('lincsdcic', 'email')


indexPageTest = CheckIndexPage(
    'http://lincs-dcic.org/#/',
    'Error with the LINCS DCIC website',
    EMAIL
)
tester.register_health_check(APP_NAME, indexPageTest)
