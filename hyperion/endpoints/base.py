"""Serves most static pages.

__authors__ = "Gregory Gundersen"
__credits__ = "Ma'ayan Lab, Icahn School of Medicine at Mount Sinai"
__contact__ = "avi.maayan@mssm.edu"
"""


from flask import Blueprint, render_template

from hyperion import config
import hyperion.tester as tester


base = Blueprint('base', __name__, url_prefix=config['DEFAULT']['base_url'])


@base.route('')
def index_page():
    results = tester.get_status()
    #return render_template('index.html')
    import json
    return json.dumps(results)