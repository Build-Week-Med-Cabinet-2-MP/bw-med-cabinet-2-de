from StrainRecommendation import StrainRecommendation as SR
from pdb import set_trace as st
import numpy as np


df_cols = ['Ammonia','Apple','Apricot','Berry','Blue Cheese','Blueberry','Cheese','Chemical','Chestnut','Citrus','Coffee','Diesel','Earthly','Flowery','Grape','Grapefruit','Honey','Lavender','Lemon','Lime','Mango','Mint','Nutty','Orange','Pepper','Pine','Pineapple','Plum','Pungent','Sage','Skunk','Spicy/Herbal','Strawberry','Sweet','Tar','Tea','Tobacco','Tree Fruit','Tropical','Vanilla','Woody','Aroused','Creative','Energetic','Euphoric','Focused','Giggly','Happy','Hungry','Relaxed','Sleepy','Talkative','Tingly','Uplifted','Hybrid','Indica', 'Sativa']

input_dict = {
    "Flavors": ["Blueberry", "Apple", "Skunk"],
    "Effects": ["Focused", "Happy", "Relaxed"]
}


def input_encoder(input_dict, df_cols):
    """
    Takes in a dictionary of flavors and effects and a list of dataframe features.
    Returns the input as a one-hot encoded list
    """
    input_list = [val for sublist in input_dict for val in input_dict[sublist]] 
    one_hot_inputs = [0] * len(df_cols)
    for i in range(len(df_cols)):
        if df_cols[i] in input_list:
            one_hot_inputs[i] = 1
    return np.array(one_hot_inputs)


model_input = input_encoder(input_dict, df_cols)

model = SR()

model.knn_predict(model_input)

jsonify(xx.to_dict())
