"""Health checks for the Harmonizome.
"""


from hyperion import config
import hyperion.tester as tester
from hyperion.apps.harmonizome.checkgeneendpoint import CheckGeneEndpoint
from hyperion.apps.harmonizome.checkindexpage import CheckIndexPage


APP_NAME = 'harmonizome'
EMAIL = config.get('harmonizome', 'email')


tester.register_health_check(APP_NAME, CheckGeneEndpoint(EMAIL))
tester.register_health_check(APP_NAME, CheckIndexPage(EMAIL))