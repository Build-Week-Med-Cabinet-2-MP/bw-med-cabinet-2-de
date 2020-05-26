import pandas as pd
import json

strains = pd.read_csv('https://raw.githubusercontent.com/Build-Week-Med-Cabinet-2-MP/bw-med-cabinet-2-ml/data-generation/data/CLEAN_WMS_2020_05_24.csv')

strains.to_json('strains.json', orient='records')

# for brandon
def list_convert(string):
    return eval(string)

for_brandon = pd.read_csv('forbrandon.csv')

for_brandon['flavors'] = for_brandon.apply(lambda x: list_convert(x['flavors']), axis=1)

for_brandon['effects'] = for_brandon.apply(lambda x: list_convert(x['effects']), axis=1)

for_brandon.to_json('web_layout_strains.json', orient='records')