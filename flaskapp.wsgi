#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,'/var/www/FlaskApp/')
sys.path.insert(0,'/var/www/FlaskApp/FlaskApp/')

from FlaskApp import app as application
application.secret_key = '123lesterabc'

