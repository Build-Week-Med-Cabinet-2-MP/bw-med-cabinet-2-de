# web_app/routes/home_routes.py

from flask import Blueprint, jsonify
import json 
from pdb import set_trace as st

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
def index():
    x = 2 + 2
    # return f"Hello World! {x}"
    with open("web_app/db/strains.json") as f:
        data = json.load(f)
    # st()
    # temp_var = json.loads("web_app/db/strains.json")
    return jsonify(data)


@home_routes.route("/about")
def about():
    return "About me"