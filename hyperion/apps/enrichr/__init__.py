"""Health checks for Enrichr.
"""


from hyperion import config
import hyperion.tester as tester
from hyperion.checkindexpage import CheckIndexPage


APP_NAME = 'enrichr'
EMAIL = config.get('enrichr', 'email')


indexPageTest = CheckIndexPage(
    'http://amp.pharm.mssm.edu/Enrichr',
    'Error with Enrichr',
    EMAIL
)
tester.register_health_check(APP_NAME, indexPageTest)
