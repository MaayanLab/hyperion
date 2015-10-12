"""Configures Hyperion at start up.

__authors__ = "Gregory Gundersen"
__credits__ = "Ma'ayan Lab, Icahn School of Medicine at Mount Sinai"
__contact__ = "avi.maayan@mssm.edu"
"""


import logging
import sys
import configparser

from flask import Flask

import hyperion.tester as reg


config = configparser.ConfigParser()
config.read('hyperion/app.ini')

static_url_path = '/%s/static' % config['DEFAULT']['app_name']
app = Flask(__name__, static_url_path=static_url_path, static_folder='static')

if not config.getboolean('DEFAULT', 'debug'):
    # Configure Apache logging.
    logging.basicConfig(stream=sys.stderr)
else:
    print('Starting in DEBUG mode')

# Connect to DB here, if necessary.

# Import these after connecting to the DB, if necessary.
from hyperion.endpoints.base import base
app.register_blueprint(base)

# Import health checkers and start checking.
import hyperion.apps.harmonizome
reg.start()
