from flask import render_template, request
from flaskApp import app
#from flaskApp.templates import *

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

import json, os, datetime
from dotenv import load_dotenv

# --- Home --- #
@app.route('/')
def home():
  return "Hello World!"
