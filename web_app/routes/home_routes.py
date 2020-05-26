# web_app/routes/home_routes.py

from flask import Blueprint, jsonify
import json 
from pdb import set_trace as st
from os.path import join as join_path

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/strains")
def index():
    x = 2 + 2
    # return f"Hello World! {x}"
    with open(join_path('web_app', 'db', 'strains.json')) as f:
        data = json.load(f)
    #breakpoint()
    # temp_var = json.loads("web_app/db/strains.json")
    return jsonify(data)

@home_routes.route("/web_layout_strains")
# creating new json object with 4 columns: name, desc, flavor, effect
def four_col_format():
    with open(join_path('web_app', 'db', 'web_layout_strains.json')) as f:
        data = json.load(f)
    return jsonify(data)

@home_routes.route("/about")
def about():
    return "About me"