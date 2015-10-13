"""Health checks for the L1000CDS2.
"""


from hyperion import config
import hyperion.tester as tester
from hyperion.checkindexpage import CheckIndexPage


APP_NAME = 'docent3'
EMAIL = config.get('docent3', 'email')


test = CheckIndexPage(
    'http://amp.pharm.mssm.edu/docent3/',
    'Error with Docent 3',
    EMAIL
)
tester.register_health_check(APP_NAME, test)
