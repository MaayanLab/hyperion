"""Health checks for Enrichr.
"""


from hyperion import config
import hyperion.tester as tester
from hyperion.checkindexpage import CheckIndexPage
from hyperion.apps.geo2enrichr.checkresultspage import CheckResultsPage


APP_NAME = 'geo2enrichr'
EMAIL = config.get('geo2enrichr', 'email')


indexPageTest = CheckIndexPage(
    'http://amp.pharm.mssm.edu/g2e',
    'Error with GEO2Enrichr',
    EMAIL
)
tester.register_health_check(APP_NAME, indexPageTest)
tester.register_health_check(APP_NAME, CheckResultsPage(EMAIL))
