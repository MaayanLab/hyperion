"""Health checks for the L1000CDS2.
"""


from hyperion import config
import hyperion.tester as tester
from hyperion.checkindexpage import CheckIndexPage


APP_NAME = 'l1000cds2'
EMAIL = config.get('l1000cds2', 'email')


indexPageTest = CheckIndexPage(
    'http://www.lincs-dcic.org/',
    'Error with the LINCS DCIC website',
    EMAIL
)
tester.register_health_check(APP_NAME, indexPageTest)