"""Health checks for the Harmonizome.
"""


from hyperion import config
import hyperion.tester as tester
from hyperion.checkindexpage import CheckIndexPage


APP_NAME = 'lincsdcic'
EMAIL = config.get('lincsdcic', 'email')


indexPageTest = CheckIndexPage(
    'http://amp.pharm.mssm.edu/PAEA',
    'Error with PAEA',
    EMAIL
)
tester.register_health_check(APP_NAME, indexPageTest)
