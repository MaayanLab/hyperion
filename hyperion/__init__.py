"""Configures Hyperion at start up.

__authors__ = "Gregory Gundersen"
__credits__ = "Ma'ayan Lab, Icahn School of Medicine at Mount Sinai"
__contact__ = "avi.maayan@mssm.edu"
"""


import logging
import sys
import configparser

from flask import Flask

import hyperion.tester as tester


config = configparser.ConfigParser()
config.read('hyperion/hyperion.ini')

static_url_path = '/%s/static' % config.get('general', 'app_name')
app = Flask(__name__, static_url_path=static_url_path, static_folder='static')

logging.basicConfig(stream=sys.stderr)

# Connect to DB here, if necessary.

# Import these after connecting to the DB, if necessary.
from hyperion.endpoints.base import base
app.register_blueprint(base)

# Import health checkers and then start. Each app is responsible for
# registering its health checks in its __init__.py file.
import hyperion.apps.chea
import hyperion.apps.enrichr
import hyperion.apps.genes2networks
import hyperion.apps.geo2enrichr
import hyperion.apps.harmonizome
import hyperion.apps.kea
import hyperion.apps.l1000cds2
import hyperion.apps.lincsdcic
import hyperion.apps.paea
tester.start()
