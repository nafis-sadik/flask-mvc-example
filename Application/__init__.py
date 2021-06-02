from flask import Flask
__version__ = '0.1'


app = Flask('Application')
app.config['SECRET_KEY'] = 'random'
app.debug = True
from Application.Controllers import *
