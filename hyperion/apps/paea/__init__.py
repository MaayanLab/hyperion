"""Health checks for PAEA.
"""


from hyperion import config
import hyperion.tester as tester
from hyperion.checkindexpage import CheckIndexPage


APP_NAME = 'paea'
EMAIL = config.get('paea', 'email')


indexPageTest = CheckIndexPage(
    'http://amp.pharm.mssm.edu/PAEA',
    'Error with PAEA',
    EMAIL
)
tester.register_health_check(APP_NAME, indexPageTest)