""" Loading moksha-ctl config from file (and the defaults!) """

import os
import sys
import ConfigParser

EXAMPLE_CTL_CONF = """
# An example ~/.moksha/ctl.conf could look like this
[busmon]
venv = fancy-busmon
busmon-src-dir = /home/user/devel/busmon
moksha-src-dir = /home/user/devel/moksha
"""

def load_config(fname="~/.moksha/ctl.conf"):
    """ Load a config file into a dictionary and return it """

    # Defaults
    config_d = {
        'venv': 'busmon',
        'apps-dir': 'moksha/apps',
        'busmon-src-dir': os.getcwd(),
        'moksha-src-dir': os.getcwd() + '/../moksha'
    }

    config = ConfigParser.ConfigParser()

    fname = os.path.expanduser(fname)
    if not os.path.exists(fname):
        print "No such file '%s'" % fname
        print EXAMPLE_CTL_CONF
        sys.exit(1)

    with open(fname) as f:
        config.readfp(f)

    if not config.has_section('busmon'):
        print "'%s' has no [busmon] section" % fname
        print EXAMPLE_CTL_CONF
        sys.exit(1)

    # Extract all defined fields
    for key in ['moksha-src-dir', 'busmon-src-dir', 'venv', 'apps-dir']:
        if config.has_option('busmon', key):
            config_d[key] = config.get('busmon', key)

    return config_d
