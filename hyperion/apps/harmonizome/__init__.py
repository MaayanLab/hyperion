"""Health checks for the Harmonizome.
"""


from hyperion import config
import hyperion.tester as reg
from hyperion.apps.harmonizome.checkgeneendpoint import CheckGeneEndpoint
from hyperion.apps.harmonizome.checkindexpage import CheckIndexPage


APP_NAME = 'harmonizome'
EMAIL = config['harmonizome']['email']


reg.register_health_check(APP_NAME, CheckGeneEndpoint(EMAIL))
reg.register_health_check(APP_NAME, CheckIndexPage(EMAIL))