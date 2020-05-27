# web_app/routes/home_routes.py

from flask import Blueprint, jsonify, request
from flask_migrate import Migrate
import psycopg2 as psy
from psycopg2.extras import execute_values
from sqlalchemy import create_engine
from dotenv import load_dotenv
import json 
from pdb import set_trace as st
from os.path import join as join_path
import pandas as pd

load_dotenv()
home_routes = Blueprint("home_routes", __name__)
migrate = Migrate()

DATABASE_URL = os.getenv(DATABASE_URL, default="try_again")

df_cols = ['Ammonia','Apple','Apricot','Berry','Blue Cheese','Blueberry','Cheese','Chemical','Chestnut','Citrus','Coffee','Diesel','Earthly','Flowery','Grape','Grapefruit','Honey','Lavender','Lemon','Lime','Mango','Mint','Nutty','Orange','Pepper','Pine','Pineapple','Plum','Pungent','Sage','Skunk','Spicy/Herbal','Tropical','Vanilla','Woody','Aroused','Creative','Energetic','Euphoric','Focused','Giggly','Happy','Hungry','Relaxed','Sleepy','Talkative','Tingly','Uplifted','Hybrid','Indica']

# get dict from ML guys
# convert dict to .json object
# backend can get .json from url/model
@home_routes.route("/model", methods=["POST"])
def receive_inputs():
    '''
    Takes form (.json object) from front-end and converts into dict for ML
    '''
    form_data = dict(request.form)
    return form_data

def input_encoder(input_dict, df_cols):
    """
    Takes in a dictionary of flavors and effects and a list of dataframe features.
    Returns the input as a one-hot encoded list
    """
    # Convert dictionary values for both flavors and effects to a single list
    input_list = [val for sublist in input_dict for val in input_dict[sublist]] 
    # create a list of 0's with the same length as the dataframe features
    one_hot_inputs = [0] * len(df_cols)
    # Loop through list of features. If the feature is in our list of inputs, 
    # assign the corresponding index in the one_hot_input list a value of 1.
    for i in range(len(df_cols)):
        if df_cols[i] in input_list:
        one_hot_inputs[i] = 1
    return one_hot_inputs
    print(input_encoder(inputs, df_cols))

def final_output():
    '''
    Takes model output (dict?), converts to .json object
    '''
    input_dict = receive_inputs()
    encoded_input = input_dict(input_dict, df_cols)
    model_output = model.predict(encoded_input)
    decoded_output= decoded_output(model_output, df_cols)
    return jsonify(decoded_output)


@home_routes.route("/refresh")
def create_db()
    '''
    Creates and connects to postgresql db
    '''

    engine = create_engine(DATABASE_URL, echo=False)
    gres_conn = psy.connect(dbname=DB_NAME, user=DB_USER, password=DB_PW, host=DB_HOST)

# route for strains (pre-data)
@home_routes.route("/strains")
def index():
    '''
    Opens file, converts ot .json object and returns it
    '''
    with open(join_path('web_app', 'db', 'strains.json')) as f:
        data = json.load(f)
    #breakpoint()
    # temp_var = json.loads("web_app/db/strains.json")
    return jsonify(data)

@home_routes.route("/web_layout_strains")

def four_col_format():
    '''
    Creatis new .json object with 4 columns: 
    name, desc, flavor, effect
    '''
    with open(join_path('web_app', 'db', 'web_layout_strains.json')) as f:
        data = json.load(f)
    return jsonify(data)

@home_routes.route("/about")
def about():
    return "A Flask App for Medicine Cabinet"