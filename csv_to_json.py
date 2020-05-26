import pandas as pd
import json

strains = pd.read_csv('https://raw.githubusercontent.com/Build-Week-Med-Cabinet-2-MP/bw-med-cabinet-2-ml/data-generation/data/CLEAN_WMS_2020_05_24.csv')

strains.to_json('strains.json', orient='records')

# for brandon
for_brandon = pd.read_csv('forbrandon.csv')

for_brandon.to_json('for_brandon.json', orient='records')
