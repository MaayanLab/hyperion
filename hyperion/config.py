"""Handles all application configurations.

__authors__ = "Gregory Gundersen"
__credits__ = "Ma'ayan Lab, Icahn School of Medicine at Mount Sinai"
__contact__ = "avi.maayan@mssm.edu"
"""


import os


class Config(object):

    with open('hyperion/app.conf') as f:
        lines = [x for x in f.read().split('\n')]

    DEBUG = lines[0] == 'True'
    SERVER_ROOT = os.path.dirname(os.getcwd()) + '/hyperion/hyperion'

    BASE_URL = '/hyperion'