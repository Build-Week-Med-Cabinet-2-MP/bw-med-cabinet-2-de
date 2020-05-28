# web_app/routes/test_routes.py

from flask import Blueprint, jsonify, request
import json
from pdb import set_trace as st
from os.path import join as join_path
import pandas as pd
import numpy as np
from web_app.ml_models.StrainRecommendation import StrainRecommendation as SR


# creates blueprint object from this file
test_routes = Blueprint("test_routes", __name__)

@test_routes.route("/test")
def unittest_output():
    '''
    Takes in unittest output and displays it
    '''
    return "TODO"