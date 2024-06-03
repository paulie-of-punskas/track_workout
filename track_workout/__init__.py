from flask import Flask
app = Flask(__name__)

import os
import track_workout.views

basedir = os.getcwd()