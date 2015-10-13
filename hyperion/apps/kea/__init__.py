"""Health checks for KEA.
"""


from hyperion import config
import hyperion.tester as tester
from hyperion.checkindexpage import CheckIndexPage


APP_NAME = 'kea'
EMAIL = config.get('apps', 'email')


indexPageTest = CheckIndexPage(
    'http://amp.pharm.mssm.edu/lib/kea.jsp',
    'Error with KEA',
    EMAIL
)
tester.register_health_check(APP_NAME, indexPageTest)
