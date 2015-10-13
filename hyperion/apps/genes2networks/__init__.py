"""Health checks for the Genes2Networks.
"""


from hyperion import config
import hyperion.tester as tester
from hyperion.checkindexpage import CheckIndexPage


APP_NAME = 'genes2networks'
EMAIL = config.get('apps', 'email')


indexPageTest = CheckIndexPage(
    'http://actin.pharm.mssm.edu/genes2networks/',
    'Error with Genes2Networks',
    EMAIL
)
tester.register_health_check(APP_NAME, indexPageTest)